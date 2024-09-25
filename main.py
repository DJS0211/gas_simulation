from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QToolButton, QAbstractButton, QWidgetAction, QMenu, QComboBox, QGraphicsDropShadowEffect
from PySide6.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView
from PySide6.QtGui import QGuiApplication, QColor, QPalette, QAction, QIcon, QDesktopServices,QFont,QBrush,QPen,QCursor
from mainwindow import Ui_MainWindow
from IGBP_range import Ui_Frame
from albedo_range import Ui_Frame_albedo
import sys
import py4cats
import matplotlib.pyplot as plt
import numpy as np	
import math
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
from PySide6.QtCharts import QChart,QChartView,QAbstractAxis,QAbstractSeries,QValueAxis,QLineSeries,QSplineSeries
from PySide6.QtCore import QMargins,Qt,QRectF
import subprocess
import mol_tau_file
import re
import shutil
import os
from netCDF4 import Dataset
import debugpy
import time
import dill as pickle
import copy
from py4cats.art.xSection import xsArray
# # 指定字体名称
# rcParams['font.family'] = 'Arial'

class window(QtWidgets.QMainWindow, Ui_MainWindow):
    # 定义自定义信号
    landSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 设置ComboBox的样式表
        # self.comboBox.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }")
        # self.comboBox_2.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }") 
        # self.comboBox_3.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }")

        # 连接start按钮，触发LBLRTM模型
        # 之所以startLBLRTM后面不能加()，是因为当使用connect方法连接一个信号到一个槽时，应该传递槽函数本身作为参数，而不是立马调用函数（即不加括号）
        self.pushButton_start.clicked.connect(self.startLBLRTM)
        # 连接stop按钮
        self.pushButton_stop.clicked.connect(self.stopLBLRTM)
        # “廓线选择”切换温湿压数据
        self.comboBox_3.currentTextChanged.connect(self.change_atmosphere)
        # 设置界面边界
        self.setContentsMargins(10,10,10,10)
        # 设置表格行列等宽并自适应变换大小
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 怎么都无法改变光标的样式，疯了
        # # 设置鼠标跟踪，以便在鼠标移动到边界时捕获MouseMove事件
        # self.setMouseTracking(True)
        # # 设置按钮点击效果
        # self.pushButton_start.clicked.connect(self.changeButtonStyle)
        # # 定义鼠标形状字典
        # self.cursor_map={
        #     (0,0) : Qt.CursorShape.SizeFDiagCursor, # 左上区域
        #     (1,0) : Qt.CursorShape.SizeVerCursor,   # 中上区域
        #     (2,0) : Qt.CursorShape.SizeBDiagCursor, # 右上区域
        #     (0,1) : Qt.CursorShape.SizeHorCursor,   # 中左区域
        #     (1,1) : Qt.CursorShape.ArrowCursor,     # 中间区域
        #     (2,1) : Qt.CursorShape.SizeHorCursor,   # 中右区域
        #     (0,2) : Qt.CursorShape.SizeBDiagCursor, # 左下区域
        #     (1,2) : Qt.CursorShape.SizeVerCursor,   # 中下区域
        #     (2,2) : Qt.CursorShape.SizeFDiagCursor  # 右下区域
        # }

        # 将地表类型和地表反射率下拉框的改变与槽函数相连(共用一个子窗口)
        self.comboBox_5.currentIndexChanged.connect(self.check_index_type)
        self.comboBox_7.currentIndexChanged.connect(self.check_index_albedo)

    def startLBLRTM(self):
        # 更新进度条
        self.progressBar.setValue(0)
        # MainWindow 的这些组件是在主线程中创建的，所以需要确保所有与 GUI 相关的操作都在主线程中执行
        # 读取界面参数
        gas = MainWindow.comboBox.currentText() #气体
        # 五院老师要求在界面上将波数改成波长，所以这里进行一下转换
        wav_min = round(1/(float(MainWindow.lineEdit_34.text()) * 10**(-7)),3) #波数最小值
        wav_max = round(1/(float(MainWindow.lineEdit_33.text()) * 10**(-7)),3) #波数最大值
        print(wav_min,wav_max)
        spec_Res = float(MainWindow.lineEdit_35.text()) #光谱分辨率
        line_data = './HITRAN_data/HITRAN_' + gas + '_all.par' #HITRAN线数据
        profile_num = MainWindow.comboBox_3.currentText()
        mls_data = './USS/USS_' + profile_num + '.xy' #廓线数据
        # 读取参数传给libradtran计算辐射强度
        albedo_value = float(MainWindow.lineEdit_50.text()) # 反照率
        sza = float(MainWindow.lineEdit_45.text()) # 太阳天顶角
        phi0 = float(MainWindow.lineEdit_42.text()) # 太阳方位角
        umu = float(MainWindow.lineEdit_44.text()) # 观测天顶角的余弦值
        phi = float(MainWindow.lineEdit_41.text()) # 观测方位角
        vis = float(MainWindow.lineEdit_55.text()) # 能见度
        ssa = float(MainWindow.lineEdit_59.text()) # 气溶胶单次散射反照率
        gg = float(MainWindow.lineEdit_51.text()) # 气溶胶非对称因子
        # 读取光源为主动光源时的参数
        sslidar_area = float(MainWindow.lineEdit_2.text()) # 探测器面积
        sslidar_energy = float(MainWindow.lineEdit.text()) # 激光脉冲能量
        sslidar_eff= float(MainWindow.lineEdit_3.text()) # 探测器效率
        sslidar_pos = float(MainWindow.lineEdit_4.text()) # 探测器高度
        sslidar_range = float(MainWindow.lineEdit_5.text()) # 单层高度
        sslidar_nranges = int(MainWindow.lineEdit_6.text()) # 探测层数
        # 读取大气模式
        mode_dict = {
            0: 'User_defined',
            1: 'Clear',
            2: 'Cloud',
            3: 'Dust',
            4: 'Slight_haze',
            5: 'Moderate_haze',
            6: 'Heavy_haze'
        }
        atm_mode = mode_dict.get(MainWindow.comboBox_2.currentIndex()) # 大气模式
        
        # 读取tab_Widget现在所处的tab
        tab = MainWindow.tabWidget.currentIndex()
        # 读取地表类型
        surface_type = MainWindow.comboBox_5.currentIndex()
        # 读取地表反射率-数据类型选择
        albedo_type = MainWindow.comboBox_7.currentIndex()
        # 读取光源
        source_type = 1 if MainWindow.comboBox_6.currentIndex() == 0 else 2
        # 读取参数生成狭缝函数
        slit_type = 1 if MainWindow.comboBox_4.currentText == '高斯' else 2 if MainWindow.comboBox_4.currentText == '三角' else 3
        FWHM = float(MainWindow.lineEdit_54.text())

        # 创建线程实例时传递参数
        # profile_num代表UI界面选择的默认廓线文件
        self.lblrtm_thread = LBLRTMThread(gas, wav_min, wav_max, spec_Res, line_data, mls_data, profile_num, albedo_value, sza, phi0, umu, phi, slit_type, FWHM, vis, atm_mode, 
                                          tab, surface_type, albedo_type, ssa, gg, source_type, sslidar_area, sslidar_energy, sslidar_eff, sslidar_pos, sslidar_range, sslidar_nranges)
        # 连接信号与槽
        self.lblrtm_thread.resultReady.connect(self.simu_output)
        self.lblrtm_thread.progressChanged.connect(self.update_progressbar)
        self.lblrtm_thread.tableChanged.connect(self.update_table)
        self.lblrtm_thread.tableChanged_2.connect(self.update_table_2)
        self.lblrtm_thread.clear_signal.connect(self.clear_output)
        
        # 启动线程来运行LBLRTM函数
        self.lblrtm_thread.start()
    
    def stopLBLRTM(self):
        # 终止线程的运行
        if self.lblrtm_thread.isRunning():
            self.lblrtm_thread.stop()
    
    # 处理计算结果的槽函数，用于更新UI界面碳卫星模拟输出
    @QtCore.Slot(tuple) # @QtCore.Slot() 是一个装饰器，用于将一个普通的 Python 方法标记为一个槽函数（slot）;这种装饰器语法是可选的，但它有助于提高代码的可读性和表现性。
    def simu_output(self, chart_data):
        chart_od_data, chart_tran_data, chart_radiance_data = chart_data
        # 使用接收到的数据创建和更新 QChart 对象
        chart_od = chart_draw('光学厚度', *chart_od_data, r'Wavenumber / cm<sup>-1</sup>', 'TOD')
        self.profile_TOD .setChart(chart_od)
        chart_tran = chart_draw('透过率', *chart_tran_data, r'Wavenumber / cm<sup>-1</sup>', 'Transmittance')
        self.profile_tran.setChart(chart_tran)
        # 当光源是主动光源时，就不用画辐亮度的图
        if MainWindow.comboBox_6.currentIndex() == 0:
            chart_radiance = chart_draw('辐亮度', *chart_radiance_data, r'Wavenumber / cm<sup>-1</sup>', 'Radiance')
            self.profile_radiance.setChart(chart_radiance)
    
    # 用于清理输出的图片和数据表格(当批量计算时)
    def clear_output(self):
        # 设置为空的 QChart 对象
        self.profile_TOD.setChart(QChart())
        self.profile_tran.setChart(QChart())
        self.profile_radiance.setChart(QChart())
        # 清空表格内容，但保留行和列的结构
        # 清除指定单元格的内容
        rows_to_clear = [1, 3, 5, 7, 9, 11]
        for row in rows_to_clear:
            self.tableWidget.takeItem(row, 0)  # 清除指定行，第0列的内容
        self.tableWidget_2.clearContents()
    
    # 用于更新UI界面大气模式
    def change_atmosphere(self):
        mls_data = './USS/USS_' + MainWindow.comboBox_3.currentText() + '.xy' #廓线数据
        mls = py4cats.vmrRead(mls_data)
        # 绘制大气模式-温度图
        chart_tem = chart_draw('温度',mls['T'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Temperature / K','Altitude / km')
        MainWindow.profile_Tem.setChart(chart_tem)
        # 绘制大气模式-湿度图
        chart_hum = chart_draw('湿度',mls['H2O'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Humidity / cm<sup>-3</sup>','Altitude / km')
        MainWindow.profile_Hum.setChart(chart_hum)
        # 绘制大气模式-压强图
        chart_pre = chart_draw('压强',mls['p'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Pressure / Pa','Altitude / km')
        MainWindow.profile_Pre.setChart(chart_pre)
    
    # 槽函数，用于更新进度条
    def update_progressbar(self, progress):
        self.progressBar.setValue(progress)
    
    # 槽函数，用于更新表格1
    def update_table(self, table_data):
        max_TOA,min_TOA,median_TOA,max_TOD,min_TOD,median_TOD = table_data
        # 设置字体大小为12，表格内容居中，数字保留5位小数
        font = QFont()
        font.setPointSize(12)
        widget_max_TOA = QTableWidgetItem(str(round(max_TOA,5)))
        widget_max_TOA.setTextAlignment(Qt.AlignCenter)
        widget_max_TOA.setFont(font)
        widget_min_TOA = QTableWidgetItem(str(round(min_TOA,5)))
        widget_min_TOA.setTextAlignment(Qt.AlignCenter)
        widget_min_TOA.setFont(font)
        widget_median_TOA = QTableWidgetItem(str(round(median_TOA,5)))
        widget_median_TOA.setTextAlignment(Qt.AlignCenter)
        widget_median_TOA.setFont(font)
        widget_max_TOD = QTableWidgetItem(str(round(max_TOD,5)))
        widget_max_TOD.setTextAlignment(Qt.AlignCenter)
        widget_max_TOD.setFont(font)
        widget_min_TOD = QTableWidgetItem(str(round(min_TOD,5)))
        widget_min_TOD.setTextAlignment(Qt.AlignCenter)
        widget_min_TOD.setFont(font)
        widget_median_TOD = QTableWidgetItem(str(round(median_TOD,5)))
        widget_median_TOD.setTextAlignment(Qt.AlignCenter)
        widget_median_TOD.setFont(font)

        self.tableWidget.setItem(1,0,widget_max_TOA)
        self.tableWidget.setItem(3,0,widget_min_TOA)
        self.tableWidget.setItem(5,0,widget_median_TOA)
        self.tableWidget.setItem(7,0,widget_max_TOD)
        self.tableWidget.setItem(9,0,widget_min_TOD)
        self.tableWidget.setItem(11,0,widget_median_TOD)
    
    def update_table_2(self,table_data_2):
        column2,column3 = table_data_2
        self.tableWidget_2.setRowCount(len(column2))
        font = QFont()
        font.setPointSize(12)
        for i in range(len(column2)):
            widget_wav = QTableWidgetItem(str(round(column2[i],5)))
            widget_wav.setTextAlignment(Qt.AlignCenter)
            widget_wav.setFont(font)
            self.tableWidget_2.setItem(i,0,widget_wav)
            widget_TOA = QTableWidgetItem(str(round(column3[i],5)))
            widget_TOA.setTextAlignment(Qt.AlignCenter)
            widget_TOA.setFont(font)
            self.tableWidget_2.setItem(i,1,widget_TOA)

    def check_index_type(self):
        # 检查地表类型下拉框的currentIndex，如果是17，则显示根据经纬度选择地表类型的子窗体
        if self.comboBox_5.currentIndex() == 17:
            Subwindow_IGBP.move(MainWindow.x()+MainWindow.width(),MainWindow.y())
            Subwindow_IGBP.show()
        else: 
            Subwindow_IGBP.hide()

    def check_index_albedo(self):
        # 检查地表反射率下拉框的currentIndex，如果是1，则显示根据经纬度选择地表反射率的子窗体
        if self.comboBox_7.currentIndex() == 1:
            Subwindow_albedo.move(MainWindow.x()+MainWindow.width(),MainWindow.y())
            Subwindow_albedo.show()
        else: 
            Subwindow_albedo.hide()
    
    # def changeButtonStyle(self):
    #     # 创建一个阴影效果的实例
    #     shadow_effect = QGraphicsDropShadowEffect()
    #     shadow_effect.setBlurRadius(10) # 设置阴影的模糊半径
    #     shadow_effect.setColor(QColor(255, 0, 0, 60))  # 设置阴影的颜色和透明度
    #     shadow_effect.setOffset(5,5)
    #     # 将阴影效果应用到按钮上
    #     self.pushButton_start.setGraphicsEffect(shadow_effect)
    
    # 怎么都无法改变光标的样式，疯了
    # def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
    #     super().mouseMoveEvent(event)
    #     # 获取界面边界大小
    #     margin_width = 20
    #     # 获取鼠标位置
    #     cursor_x = event.position().x()
    #     cursor_y = event.position().y()
    #     # 获取窗口大小
    #     window_width = self.width()
    #     window_height = self.height()
    #     # 确定鼠标位置所在区域
    #     x_index = 0 if cursor_x < margin_width else 2 if cursor_x > window_width - margin_width else 1
    #     y_index = 0 if cursor_y < margin_width else 2 if cursor_y > window_height - margin_width else 1
    #     # 设置鼠标形状
    #     self.setCursor(self.cursor_map[(x_index,y_index)])

class window_IGBP(QtWidgets.QFrame, Ui_Frame):
    # # 定义一个点击确定键的信号
    # confirmClicked = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("设置地表类型经纬度范围")
        self.resize(300,100)
        self.pushButton.clicked.connect(self.IGBP_confirm)

    def IGBP_confirm(self):
        # # 发射信号
        # self.confirmClicked.emit()
        # 不关闭子窗口，打印一行字表示经纬度设置成功
        print("地表类型经纬度设置成功!")

class window_albedo(QtWidgets.QFrame, Ui_Frame_albedo):
    # # 定义一个点击确定键的信号
    # confirmClicked = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("设置地表反射率经纬度范围")
        self.resize(300,100)
        self.pushButton.clicked.connect(self.albedo_confirm)

    def albedo_confirm(self):
        # # 发射信号
        # self.confirmClicked.emit()
        # 不关闭子窗口，打印一行字表示经纬度设置成功
        print("地表反射率经纬度设置成功!")
    
class LBLRTMThread(QtCore.QThread):
    # 定义一个带有结果的信号
    resultReady = QtCore.Signal(tuple)
    # 定义更新进度条的信号
    progressChanged = QtCore.Signal(int)
    # 定义更新表格1的信号
    tableChanged = QtCore.Signal(tuple)
    # 定义更新表格2的信号
    tableChanged_2 = QtCore.Signal(tuple)
    # 定义清理输出的图片和数据表格的信号
    clear_signal = QtCore.Signal()

    def __init__(self, gas, wav_min, wav_max, spec_Res, line_data, mls_data, profile_num, albedo_value, sza, phi0, umu, phi, slit_type, FWHM, vis, 
                 atm_mode, tab, surface_type, albedo_type, ssa, gg, source_type, sslidar_area, sslidar_energy, sslidar_eff, sslidar_pos, sslidar_range, sslidar_nranges):
        super().__init__()  # 调用父类的初始化方法
        self.gas = gas
        self.wav_min = wav_min
        self.wav_max = wav_max
        self.spec_Res = spec_Res
        self.line_data = line_data
        self.mls_data = mls_data
        self.profile_num = profile_num
        self.albedo_value = albedo_value
        self.sza = sza
        self.phi0 = phi0
        self.umu = umu
        self.phi = phi
        self.slit_type = slit_type
        self.FWHM = FWHM
        self.vis = vis
        self.atm_mode = atm_mode
        self.tab = tab
        self.surface_type = surface_type
        self.albedo_type = albedo_type
        self.ssa = ssa
        self.gg = gg
        self.source_type = source_type
        self.sslidar_area = sslidar_area
        self.sslidar_energy = sslidar_energy
        self.sslidar_eff = sslidar_eff
        self.sslidar_pos = sslidar_pos
        self.sslidar_range = sslidar_range
        self.sslidar_nranges = sslidar_nranges
        # 设置一个终止线程的标志
        self.stop_requested = False

    def run(self):
        # 首先检查终止线程的标志
        if not self.stop_requested:   
            # 解决调试过程中无法停在QThread里的断点的问题，当不调试时记得注释掉这一行
            # debugpy.debug_this_thread()

            dictLineLists = py4cats.higstract(self.line_data,(self.wav_min,self.wav_max))
            mls = py4cats.atmRead(self.mls_data,extract=self.gas)
            # # 读取吸收截面查找表
            # with open('xs_Array.pkl','rb') as f:
            #     xs_Array = pickle.load(f)
            # # 根据波数范围截取吸收截面数据
            # truncated_xsArray = []  # 用于存储截取后的数组
            # # 遍历 xs_Array 中的每个元素
            # for xs in xs_Array:
            #     truncated_array = manual_deepcopy(xs)
            #     truncated_array = truncated_array.truncate((self.wav_min,self.wav_max))
            #     truncated_xsArray.append(truncated_array)  # 将截取后的结果添加到列表中
            # # 找到与大气数据对应的吸收截面数据
            # matched_xsArray = search_matched_xsArray(mls,truncated_xsArray)
            # 计算光学厚度、透过率
            # dodList = py4cats.lbl2od(mls,dictLineLists,sampling=0.1, nGrids=1)
            dodList = py4cats.lbl2od(mls,dictLineLists)
            todList = py4cats.dod2tod(dodList)

            # radNadir_0 = py4cats.dod2ri(dodList, obsAngle=180, tSurface='BoA',space=-6000) # 因为太阳被形容为温度为6000K的黑体，所以space=-6000代表太阳光谱，这个space变量也可以是文件名，即可从文件中读取辐射光谱
            # radNadir = radNadir_0.convolve(self.spec_Res, 'G') # 卷积操作

            # 更新进度条并检查终止线程的标志
            if self.check_stop_requested(progress=10): 
                return

            # 计算辐射强度
            # 读取内容至字典中
            variables = {}
            filename = './typical_INP/' + self.atm_mode + '.INP'
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.split(' ')
                    # 分情况部署字典的键和值
                    if parts[0] == 'aerosol_modify':
                        parts[0] = parts[0] + ' ' + parts[1] + ' ' + parts[2]
                        variables[parts[0]] = parts[3]
                    elif parts[0] == 'sslidar':
                        parts[0] = parts[0] + ' ' + parts[1]
                        variables[parts[0]] = parts[2]
                    else :
                        variables[parts[0]] = ' '.join(parts[1:])
            # 为防止出现波数起始值不统一的情况，直接使用todList的波数值，即原始线数据的实际波数值，不使用UI界面上读取的波数值
            # 同时需要注意，这里的波长值必须与太阳光谱kurudz_0.01nm.txt里的波长值完全一致，不然Libradtran无法运行
            column_kurudz_wav = []
            # 读取太阳光谱kurudz_0.01nm.txt里的波长值
            with open('kurudz_0.01nm.txt','r') as f:
                lines = f.readlines()
                for line in lines :
                    parts = line.split()
                    if not parts[0].startswith('#'):
                        column_kurudz_wav.append(float(parts[0]))
            # 找到第一个大于wavelength_min的波长值(这一行很耗时间)
            # wavelength_min_input = min([wav for wav in column_kurudz_wav if wav > 1/(todList.grid()[-1]*10**(-7))])
            # # 找到第一个小于wavelength_max的波长值(这一行很耗时间)
            # wavelength_max_input = max([wav for wav in column_kurudz_wav if wav < 1/(todList.grid()[0]*10**(-7))])
            # 找到大于wavelength_min且最接近的波长
            wavelength_min_threshold = 1 / (todList.grid()[-1] * 10**(-7))
            wavelength_min_input = min((wav for wav in column_kurudz_wav if wav > wavelength_min_threshold),
                           key=lambda x: abs(x - wavelength_min_threshold))

            # 找到小于wavelength_max且最接近的波长
            wavelength_max_threshold = 1 / (todList.grid()[0] * 10**(-7))
            wavelength_max_input = min((wav for wav in column_kurudz_wav if wav < wavelength_max_threshold),
                                    key=lambda x: abs(x - wavelength_max_threshold))

            # 更新进度条并检查终止线程的标志
            if self.check_stop_requested(progress=30): 
                return

            # 根据UI界面的参数修改INP文件
            variables['wavelength'] = str(wavelength_min_input) + ' ' + str(wavelength_max_input)
            variables['sza'] = int(self.sza)
            variables['phi0'] = self.phi0
            variables['umu'] = self.umu
            variables['phi'] = self.phi
            variables['atmosphere_file'] = './dat/USS_' + self.profile_num + '.dat'
            variables['mol_tau_file'] = 'abs ' + 'mol_tau_file_' + self.gas +'.txt'
            # 这一块的代码可以优化一下，更简洁地根据所选典型场景来设置参数
            # 典型场景的visibility先固定好，后期优化代码后可以给个范围供用户调整
            if 'User_defined' in self.atm_mode:
                variables['aerosol_visibility'] = self.vis
                variables['aerosol_modify ssa set'] = self.ssa
                variables['aerosol_modify gg set'] = self.gg

            # 如果光源为主动光源，则修改rte_solver,删除output_user lambda wavenumber uu和slit_function_file,并且读取sslidar相关参数值(注意要保留source solar)
            if self.source_type == 2:
                variables['rte_solver'] = 'sslidar'
                del variables['output_user']
                del variables['slit_function_file']
                variables['sslidar area'] = self.sslidar_area
                variables['sslidar E0'] = self.sslidar_energy
                variables['sslidar eff'] = self.sslidar_eff
                variables['sslidar position'] = self.sslidar_pos
                variables['sslidar_nranges'] = self.sslidar_nranges
                variables['sslidar range'] = self.sslidar_range
            
            # 计算分子光学厚度
            mol_tau_file.mol_tau(self,self.gas,self.wav_min,self.wav_max,self.line_data,self.mls_data,self.profile_num,self.stop_requested)
            # 更新进度条并检查终止线程的标志
            if self.check_stop_requested(progress=50): 
                return
            
            # 生成狭缝函数(光谱响应函数)
            run_command(f"../../libRadtran2.0.5/libRadtran-2.0.5/bin/make_slitfunction -f {self.FWHM} -r 0.01 -t {self.slit_type} > slit.dat")
            # 更新进度条并检查终止线程的标志
            if self.check_stop_requested(progress=70): 
                return
            
            # 把所有参数都读取完成之后，再进行批量计算的相关操作
            # 判断现在设置的是地表类型还是地表反射率
            if self.tab == 0: ## 设置地表类型
                if self.surface_type == 17:
                    EW_hemis = 'E' if Subwindow_IGBP.comboBox.currentIndex() == 0 else 'W'
                    NS_hemis = 'N' if Subwindow_IGBP.comboBox_2.currentIndex() == 0 else 'S' 
                    lat = float(Subwindow_IGBP.lineEdit_2.text())
                    lon = float(Subwindow_IGBP.lineEdit.text())
                    variables['latitude'] = NS_hemis + ' ' + lat
                    variables['longitude'] = EW_hemis + ' ' + lon
                    variables['albedo_library'] = 'IGBP'
                    variables['surface_type_map'] = 'IGBP.nc'
                else :
                    variables['albedo_library'] = 'IGBP'
                    variables['brdf_rpv_type'] = self.surface_type + 1
            elif self.tab == 1:  ## 设置地表反射率
                if self.albedo_type == 0:
                    variables['albedo'] = self.albedo_value
                else :
                    # EW_hemis = 1 if Subwindow_IGBP.comboBox.currentIndex() == 0 else -1
                    # NS_hemis = 1 if Subwindow_IGBP.comboBox_2.currentIndex() == 0 else -1
                    # 打开文件并读取反射率数据(根据所在波段选择反射率数据,1000nm以下用Band1数据，1000-1800nm用Band5数据，1800nm以上用Band7数据)
                    if wavelength_min_input <= 1000 :
                        filename_ref = 'output_data_1.txt'
                    elif wavelength_min_input > 1000 and wavelength_min_input < 1800  :
                        filename_ref = 'output_data_5.txt'
                    elif wavelength_min_input >= 1800 :
                        filename_ref = 'output_data_7.txt'
                    with open(filename_ref, 'r') as file:
                        lines = file.readlines()
                        # 创建空列表来存储第二列和第三列的数据
                        column1, column2, column3 = [], [], []
                        # 遍历每一行
                        for line in lines:
                            # 使用空格分割每一行的数据
                            parts = line.split()
                            # 将第一列、第二列和第三列的数据添加到对应的列表中
                            column1.append(float(parts[0])), column2.append(float(parts[1])), column3.append(float(parts[2]))

                    pattern_digit = r'^[+-]?\d+(\.\d+)?$' # 匹配纯数字的正则表达式（整数或小数）
                    pattern_range = r'^[+-]?\d+(\.\d+)?\s*,\s*[+-]?\d+(\.\d+)?$' # 匹配数字+','+数字的正则表达式
                    # 判断输入是纯数字还是范围
                    if re.match(pattern_digit,Subwindow_albedo.lineEdit.text()) and re.match(pattern_digit,Subwindow_albedo.lineEdit_2.text()):
                        print('输入是纯数字')
                        lon = float(Subwindow_albedo.lineEdit.text())
                        lat = float(Subwindow_albedo.lineEdit_2.text())
                        # 找到与用户输入的经度最接近的值
                        closest_lon = min(column1, key=lambda list_lon: abs(list_lon - lon))
                        # 找到与用户输入的纬度最接近的值
                        closest_lat = min(column2, key=lambda list_lat: abs(list_lat - lat))
                        # 新建索引
                        index = None
                        # 根据找到的经纬度值，确定对应索引
                        for i in range(len(column1)):
                            if column1[i] == closest_lon and column2[i] == closest_lat:
                                index = i
                                break
                        # 如果找到匹配的索引，获取对应的反射率数据
                        if index is not None:
                            if column3[index] == 0:
                                # 没有地表反射率数据就设置一个默认值
                                variables['albedo'] = 0.3
                                print('该位置尚无地表反射率数据')
                            else :
                                variables['albedo'] = column3[index]
                                print("成功获取对应反射率")
                        else:
                            print("未获取对应反射率")
                    elif re.match(pattern_range,Subwindow_albedo.lineEdit.text()) and re.match(pattern_range,Subwindow_albedo.lineEdit_2.text()):
                        print('输入是范围')
                        lon_parts = Subwindow_albedo.lineEdit.text().split(',')
                        lon_min = float(lon_parts[0])
                        lon_max = float(lon_parts[1])
                        lat_parts = Subwindow_albedo.lineEdit_2.text().split(',')
                        lat_min = float(lat_parts[0])
                        lat_max = float(lat_parts[1])
                        # # 分别找到与用户输入的最大经度和最小经度最接近的值
                        # closest_lon_min = min(column1, key=lambda list_lon: abs(list_lon - lon_min))
                        # closest_lon_max = min(column1, key=lambda list_lon: abs(list_lon - lon_max))
                        # # 分别找到与用户输入的最大纬度和最小纬度最接近的值
                        # closest_lat_min = min(column2, key=lambda list_lat: abs(list_lat - lat_min))
                        # closest_lat_max = min(column2, key=lambda list_lat: abs(list_lat - lat_max))
                        
                        # 得到用于仿真的经纬度范围(直接根据用户指定的经纬度范围，取出地表反射率文件的经纬度数据中对应范围内的元素，这里为了节省计算时间就不再找最接近的值)
                        # 使用布尔索引取出指定范围内的元素(将列表转换成numpy数组才能这么操作);并且要注意,反射率文件中的经纬度不是递增的,有很长的一段重复,所以要从lon_MCD12C1.txt和lat_MCD12C1.txt中读取
                        with open('lon_MCD12C1.txt', 'r') as file:
                            lon_MCD12C1 = np.array(file.readlines())
                            lon_MCD12C1 = lon_MCD12C1.astype(float)
                        with open('lat_MCD12C1.txt', 'r') as file:
                            lat_MCD12C1 = np.array(file.readlines())
                            lat_MCD12C1 = lat_MCD12C1.astype(float)
                        lon_range = lon_MCD12C1[(lon_MCD12C1 >= lon_min) & (lon_MCD12C1 <= lon_max)]
                        lat_range = lat_MCD12C1[(lat_MCD12C1 >= lat_min) & (lat_MCD12C1 <= lat_max)]
                    
                    else :
                        print('输入有误,请重新输入!')

            # 如果地表反射率没有指定经纬度范围
            if not (self.tab == 1 and self.albedo_type == 1 and re.match(pattern_range, Subwindow_albedo.lineEdit.text()) and re.match(pattern_range, Subwindow_albedo.lineEdit_2.text())):
                # 将读取的变量写入INP文件
                filename_inp = 'UVSPEC_Clear_' + self.gas + '.INP'
                filename_out = 'UVSPEC_Clear_' + self.gas + '.out'
                with open(filename_inp, 'w') as file:
                    for key, value in variables.items():
                        file.write(f"{key} {value}\n")

                start_time = time.time()
                # 控制命令行,TOA值用Libradtran的DISORT模型算，所有诊断消息将写入verbose.txt
                run_command(f"../../libRadtran2.0.5/libRadtran-2.0.5/bin/uvspec <{filename_inp}> {filename_out} 2> verbose.txt")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Execution time: {elapsed_time:.6f} seconds")

                # 打开文件并读取TOA数据
                with open(filename_out, 'r') as file:
                    lines = file.readlines()
                # 创建空列表来存储第二列和第三列的数据
                column1, column2, column3 = [], [], []
                # 遍历每一行
                for line in lines:
                    # 使用空格分割每一行的数据
                    parts = line.split()
                    # 检查是否有足够的数据列
                    if len(parts) >= 3:
                        # 将第一列、第二列和第三列的数据添加到对应的列表中
                        column1.append(float(parts[0]))
                        column2.append(float(parts[1]))
                        column3.append(float(parts[2]))

                # 计算绘图所需的数据
                chart_od_data = (todList.grid(), np.log10(todList.base))
                tranList = np.exp(-2 * todList)
                chart_tran_data = (todList.grid(), tranList.base)
                # chart_radiance_data = (radNadir.grid(), radNadir * (10 ** 7))
                chart_radiance_data = (column2, column3)

                # 更新进度条并检查终止线程的标志
                if self.check_stop_requested(progress=85): 
                    return

                # 发出信号，携带绘图数据，因为 QChart 是一个继承自 QGraphicsView 的 QWidget，因此它应该在 GUI 线程（主线程）中创建和操作。
                self.resultReady.emit((chart_od_data, chart_tran_data, chart_radiance_data))
                # 发出信号，携带表格2数据
                self.tableChanged_2.emit((column1,column3))
                # 计算表格所需数据(辐亮度最大值、最小值、中位数，光学厚度最大值、最小值、中位数)
                column3.sort()
                half_TOA = len(column3) // 2
                max_TOA = max(column3)
                min_TOA = min(column3)
                median_TOA = (column3[half_TOA] + column3[~half_TOA])/2
                todList.base.sort()
                half_TOD = len(todList.base) // 2
                max_TOD = max(todList.base)
                min_TOD = min(todList.base)
                median_TOD = (todList.base[half_TOD] + todList.base[~half_TOD])/2
                # 发出信号，携带表格数据
                self.tableChanged.emit((max_TOA,min_TOA,median_TOA,max_TOD,min_TOD,median_TOD))

                # 更新进度条并检查终止线程的标志
                if self.check_stop_requested(progress=100): 
                    return
            
            else :
                # 清空输出的图片和数据表格
                self.clear_signal.emit()
                # 定义INP和OUT文件的路径
                inp_dir = './BatchCompute/INP/'
                out_dir = './BatchCompute/OUT/'
                # 清空BatchCompute里INP和OUT文件夹中的文件
                clear_folder(inp_dir)
                clear_folder(out_dir)
                # 总的运行次数
                total_iterations = len(lon_range) * len(lat_range)
                # 计数器，跟踪当前运行次数
                current_iteration = 0

                start_time = time.time()
                
                # 将读取的变量写入INP文件
                for i in range(len(lon_range)):
                    for j in range(len(lat_range)):    
                        # 更新当前运行次数
                        current_iteration += 1
                        # 输出当前进度
                        print(f"正在运行第 {current_iteration} 个，共 {total_iterations} 个(lon_range: {i+1}/{len(lon_range)}, lat_range: {j+1}/{len(lat_range)})")
                        
                        filename_inp = './BatchCompute/INP/' + self.gas + '_' + str(lon_range[i]) + '_' + str(lat_range[j]) + '.INP'
                        filename_out = './BatchCompute/OUT/' + self.gas + '_' + str(lon_range[i]) + '_' + str(lat_range[j]) + '.OUT'
                        # 打开文件读取反射率数据
                        with open(filename_ref, 'r') as file:
                            lines = file.readlines()
                            # 创建空列表来存储第二列和第三列的数据
                            column1, column2, column3 = [], [], []
                            # 遍历每一行
                            for line in lines:
                                # 使用空格分割每一行的数据
                                parts = line.split()
                                # 将第一列、第二列和第三列的数据添加到对应的列表中
                                column1.append(float(parts[0])), column2.append(float(parts[1])), column3.append(float(parts[2]))
                        # 新建索引
                        index = None
                        # 根据找到的经纬度值，确定对应索引
                        for m in range(len(column1)):
                            if column1[m] == lon_range[i] and column2[m] == lat_range[j]:
                                index = m
                                break
                        # 如果找到匹配的索引，获取对应的反射率数据
                        if index is not None:
                            if column3[index] == 0:
                                # 没有地表反射率数据就设置一个默认值
                                variables['albedo'] = 0.3
                                print('该位置尚无地表反射率数据')
                            else :
                                variables['albedo'] = column3[index]
                                print("成功获取对应反射率")
                        else:
                            print("未获取对应反射率")

                        with open(filename_inp, 'w') as file:
                            for key, value in variables.items():
                                file.write(f"{key} {value}\n")
                        
                        # 控制命令行,TOA值用Libradtran的DISORT模型算，所有诊断消息将写入对应的verbose.txt
                        # verbose_file = './BatchCompute/verbose/' + 'verbose' + '_' + str(lon_range[i]) + '_' + str(lat_range[j]) + '.txt'
                        run_command(f"../../libRadtran2.0.5/libRadtran-2.0.5/bin/uvspec <{filename_inp}> {filename_out} ")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Execution time: {elapsed_time:.6f} seconds")
                # 更新进度条并检查终止线程的标志
                if self.check_stop_requested(progress=85): 
                    return
                
                # 获取OUT文件夹中的所有文件列表
                out_files = [f for f in os.listdir(out_dir) if f.endswith('.OUT')]
                # 初始化空的经纬度列表
                lon_list = []
                lat_list = []
                # 初始化四维数组数据
                toa_radiance_data = {}
                # 遍历所有的OUT文件并提取数据
                for file_name in out_files:
                    # 从文件名中提取经纬度信息
                    parts = file_name.split('_')
                    gas = parts[0]
                    lon = float(parts[1])
                    lat = float(parts[2].replace('.OUT', ''))
                    
                    # 将经纬度添加到列表
                    if lon not in lon_list:
                        lon_list.append(lon)
                    if lat not in lat_list:
                        lat_list.append(lat)                  
                    # 读取OUT文件内容
                    file_path = os.path.join(out_dir, file_name)
                    data = np.loadtxt(file_path)  # 假设文件内容为三列数据，波长、波数、TOA radiance
                    # 保存数据到字典，字典键为经度、纬度，值为读取的数据
                    toa_radiance_data[(lon, lat)] = data
                
                # 去重并排序经纬度
                lon_list = sorted(lon_list)
                lat_list = sorted(lat_list)
                # 获取波长和波数的维度大小（假设所有文件的数据行列数相同）
                sample_data = toa_radiance_data[(lon_list[0], lat_list[0])]
                wavelength_size = sample_data.shape[0]  # 行数
                # 创建四维数组，大小为 (经度，纬度，波长，列数)
                four_dim_data = np.zeros((len(lon_list), len(lat_list), wavelength_size, 3))
                # 将数据填充到四维数组
                for i, lon in enumerate(lon_list):
                    for j, lat in enumerate(lat_list):
                        four_dim_data[i, j, :, :] = toa_radiance_data[(lon, lat)]
                # 创建 NetCDF 文件
                nc_filename = 'toa_radiance_data.nc'
                with Dataset(nc_filename, 'w', format='NETCDF4') as ncfile:
                    # 创建维度
                    ncfile.createDimension('longitude', len(lon_list))
                    ncfile.createDimension('latitude', len(lat_list))
                    ncfile.createDimension('wavelength', wavelength_size)
                    ncfile.createDimension('variable_number', 3)

                    # 创建变量
                    longitudes = ncfile.createVariable('longitude', 'f4', ('longitude',))
                    latitudes = ncfile.createVariable('latitude', 'f4', ('latitude',))
                    wavelengths = ncfile.createVariable('wavelength', 'f4', ('wavelength',))
                    variable_number = ncfile.createVariable('variable_number', 'f4', ('variable_number',))
                    toa_radiances = ncfile.createVariable('toa_radiance', 'f4', ('variable_number', 'wavelength', 'latitude', 'longitude'))

                    # 填充变量数据
                    longitudes[:] = lon_list
                    latitudes[:] = lat_list
                    wavelengths[:] = sample_data[:, 0]  # 假设所有文件的第一列是波长
                    variable_number[:] = np.arange(3)  # 3列数据
                    # toa_radiances[:, :, :, :] = four_dim_data
                    # Python 和 MATLAB 对数组维度的存储顺序不同，所以要在这里对数组进行转置，确保在MATLAB中读取顺序正确
                    toa_radiances[:, :, :, :] = np.transpose(four_dim_data, (3, 2, 1, 0))

                    print(f"数据已成功存储到 {nc_filename} 文件中。")
                # 更新进度条并检查终止线程的标志
                if self.check_stop_requested(progress=100): 
                    return
                
    def stop(self):
        self.stop_requested = True
        
    def check_stop_requested(self, progress):
        # 更新进度条
        self.progressChanged.emit(progress)
        # 检查是否请求停止线程
        if self.stop_requested:
            # 请求停止时将进度条归零
            self.progressChanged.emit(0)
            return True
        return False

# 清除文件夹中所有文件的函数
def clear_folder(folder_path):
    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        # 遍历文件夹中的所有内容
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                # 如果是文件或者符号链接则删除
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                # 如果是文件夹则删除文件夹及其内容
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'Folder "{folder_path}" does not exist.')

# 手动创建一个新的xsArray实例，并将所需属性传递给构造函数进行拷贝，实现深拷贝目的
def manual_deepcopy(xs):
    new_xs = xsArray(xs.view(np.ndarray).copy(), xLimits=copy.deepcopy(xs.x), p=copy.deepcopy(xs.p), t=copy.deepcopy(xs.t), molec=copy.deepcopy(xs.molec), lineShape=copy.deepcopy(xs.lineShape))
    return new_xs

# 遍历 mls 中的每一组压强和温度组合，找到对应的 xsArray
def search_matched_xsArray(mls,xs_Array):
    # 创建一个存储匹配结果的列表
    matched_xsArray = []
    for i in range(len(mls['p'])):
        p_mls = mls['p'][i]  # 当前大气压强
        t_mls = mls['T'][i]  # 当前大气温度

        # 分别找到最接近的 p 和 t
        closest_p = min(xs_Array, key=lambda xs: abs(xs.p - p_mls))
        closest_t = min(xs_Array, key=lambda xs: abs(xs.t - t_mls))
        # 遍历 xs_Array，寻找同时满足最接近的 p 和 t 的元素
        for xs in xs_Array:
            if xs.p == closest_p.p and xs.t == closest_t.t:
                xs_temp = manual_deepcopy(xs)
                xs_temp.p = p_mls
                xs_temp.t = t_mls
                matched_xsArray.append(xs_temp)
                break
    return matched_xsArray
        
# chart绘图函数
def chart_draw(chart_titie,x_data,y_data,x_label,y_label):
    # 创建chart
    chart = QChart()
    chart.createDefaultAxes()
    chart.setTitle(chart_titie)
    # 设置标题字体大小
    font = QFont()
    font.setPointSize(12)
    chart.setTitleFont(font)
    # 设置外边距
    chart.setMargins(QMargins(0,0,0,0))
    # 设置背景为透明
    chart.setBackgroundBrush(QBrush(Qt.transparent))
    # 创建数据序列
    # series = QLineSeries()
    series = QSplineSeries()
    for i in range(len(x_data)):
        series.append(x_data[i],y_data[i])
    chart.addSeries(series)
    # 设置坐标轴的画笔
    axis_pen = QPen(Qt.black)
    axis_pen.setWidth(2)
    # 创建并设置 X 轴
    axisX = QValueAxis()
    axisX.setTitleText(x_label)  # 设置 X 轴标题
    axisX.setLinePen(axis_pen)
    # 创建并设置 Y 轴
    axisY = QValueAxis()
    axisY.setTitleText(y_label)  # 设置 Y 轴标题
    axisY.setLinePen(axis_pen)
    # 将 series 与坐标轴关联
    chart.setAxisX(axisX, series)  # 将 X 轴与 series 关联
    chart.setAxisY(axisY, series)  # 将 Y 轴与 series 关联s
    # 设置网格线的画笔
    grid_pen = QPen(Qt.black)  # 设置黑色的画笔
    grid_pen.setWidth(2)  # 设置画笔的宽度
    chart.axisX().setGridLinePen(grid_pen)  # 设置 X 轴网格线的画笔
    chart.axisY().setGridLinePen(grid_pen)  # 设置 Y 轴网格线的画笔
    # 设置线条的画笔
    series_pen = QPen(QColor(0, 0, 255))
    series_pen.setWidth(3)
    series.setPen(series_pen)
    # 隐藏默认的图例
    chart.legend().setVisible(False)
    # 将结果传递给主线程，因为需要确保所有与 GUI 相关的操作都在主线程中执行
    return chart

# 计算大气模式
def atmos_mode():
    global MainWindow  # 声明全局变量
    mls_data = './USS/USS_' + MainWindow.comboBox_3.currentText() + '.xy'
    mls = py4cats.vmrRead(mls_data)

    # 绘制大气模式-温度图
    chart_tem = chart_draw('温度',mls['T'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Temperature / K','Altitude / km')
    MainWindow.profile_Tem.setChart(chart_tem)
    # 绘制大气模式-湿度图,使用HTML标签来实现上标效果
    chart_hum = chart_draw('湿度',mls['H2O'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Humidity / cm<sup>-3</sup>','Altitude / km')
    MainWindow.profile_Hum.setChart(chart_hum)
    # 绘制大气模式-压强图
    chart_pre = chart_draw('压强',mls['p']/10,py4cats.unitConversion(mls['z'], 'length', new='km'),'Pressure / Pa','Altitude / km')
    MainWindow.profile_Pre.setChart(chart_pre)

# 执行命令行指令
def run_command(command):
    # 执行命令
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    # 检查命令是否成功执行
    if result.returncode == 0:
        print("Command executed successfully!")
        # print("Output:\n", result.stdout)
    else:
        print("Command failed with return code", result.returncode)
        print("Error:\n", result.stderr)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    QApplication.setOverrideCursor(Qt.CursorShape.SizeHorCursor)
    MainWindow = window()  # 创建窗体对象
    Subwindow_IGBP = window_IGBP()  # 创建子窗体-IGBP
    Subwindow_albedo = window_albedo() # 创建子窗体-albedo
    
    # 绘制大气模式
    atmos_mode()

    # 设置窗口图标、标题
    MainWindow.setWindowIcon(QIcon("logo.png"))
    MainWindow.setWindowTitle("Target gas radiation transfer simulation system")

    # 获取屏幕尺寸
    screen = QGuiApplication.primaryScreen().size()
    width = screen.width()
    height = screen.height()
    # 设置窗口位置、几何
    x = (screen.width() - screen.width()//2) // 2
    y = (screen.height() - screen.height()//2) // 2
    # 将主窗口设置在屏幕中间（但是效果未实现，每次出现的位置都不固定）
    MainWindow.setGeometry(x,y,width//2, height//2)

    MainWindow.show()
    sys.exit(app.exec())  # 程序关闭时退出进程