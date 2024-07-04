from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QToolButton, QAbstractButton, QWidgetAction, QMenu, QComboBox, QGraphicsDropShadowEffect
from PySide6.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView
from PySide6.QtGui import QGuiApplication, QColor, QPalette, QAction, QIcon, QDesktopServices,QFont,QBrush,QPen,QCursor
from mainwindow import Ui_MainWindow
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
# import debugpy
import time
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

    def startLBLRTM(self):
        # 更新进度条
        self.progressBar.setValue(0)
        # MainWindow 的这些组件是在主线程中创建的，所以需要确保所有与 GUI 相关的操作都在主线程中执行
        # 读取界面参数
        gas = MainWindow.comboBox.currentText() #气体
        wav_min = float(MainWindow.lineEdit_33.text()) #波数最小值
        wav_max = float(MainWindow.lineEdit_34.text()) #波数最大值
        spec_Res = float(MainWindow.lineEdit_35.text()) #光谱分辨率
        line_data = './HITRAN_data/HITRAN_' + gas + '_all.par' #HITRAN线数据
        profile_num = MainWindow.comboBox_3.currentText()
        mls_data = './USS/USS_' + profile_num + '.xy' #廓线数据
        # 读取参数传给libradtran计算辐射强度
        day_of_year = int(MainWindow.lineEdit_43.text())
        albedo = float(MainWindow.lineEdit_50.text())
        sza = float(MainWindow.lineEdit_45.text())
        phi0 = float(MainWindow.lineEdit_42.text())
        umu = float(MainWindow.lineEdit_44.text())
        phi = float(MainWindow.lineEdit_41.text())
        vis = float(MainWindow.lineEdit_55.text())
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
        atm_mode = mode_dict.get(MainWindow.comboBox_2.currentIndex())
        # 读取参数生成狭缝函数
        slit_type = 1 if MainWindow.comboBox_4.currentText == '高斯' else 2 if MainWindow.comboBox_4.currentText == '三角' else 3
        FWHM = float(MainWindow.lineEdit_54.text())

        # 创建线程实例时传递参数
        # profile_num代表UI界面选择的默认廓线文件
        self.lblrtm_thread = LBLRTMThread(gas, wav_min, wav_max, spec_Res, line_data, mls_data, profile_num, day_of_year, albedo, sza, phi0, umu, phi, slit_type, FWHM, vis, atm_mode)
        # 连接信号与槽
        self.lblrtm_thread.resultReady.connect(self.simu_output)
        self.lblrtm_thread.progressChanged.connect(self.update_progressbar)
        self.lblrtm_thread.tableChanged.connect(self.update_table)
        self.lblrtm_thread.tableChanged_2.connect(self.update_table_2)
        
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
        chart_radiance = chart_draw('辐亮度', *chart_radiance_data, r'Wavenumber / cm<sup>-1</sup>', 'Radiance')
        self.profile_radiance.setChart(chart_radiance)
        # 更新进度条
        self.progressBar.setValue(100)
    
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
  
class LBLRTMThread(QtCore.QThread):
    # 定义一个带有结果的信号
    resultReady = QtCore.Signal(tuple)
    # 定义更新进度条的信号
    progressChanged = QtCore.Signal(int)
    # 定义更新表格1的信号
    tableChanged = QtCore.Signal(tuple)
    # 定义更新表格2的信号
    tableChanged_2 = QtCore.Signal(tuple)

    def __init__(self, gas, wav_min, wav_max, spec_Res, line_data, mls_data, profile_num, day_of_year, albedo, sza, phi0, umu, phi, slit_type, FWHM, vis, atm_mode):
        super().__init__()  # 调用父类的初始化方法
        self.gas = gas
        self.wav_min = wav_min
        self.wav_max = wav_max
        self.spec_Res = spec_Res
        self.line_data = line_data
        self.mls_data = mls_data
        self.profile_num = profile_num
        self.day_of_year = day_of_year
        self.albedo = albedo
        self.sza = sza
        self.phi0 = phi0
        self.umu = umu
        self.phi = phi
        self.slit_type = slit_type
        self.FWHM = FWHM
        self.vis = vis
        self.atm_mode = atm_mode
        # 设置一个终止线程的标志
        self.stop_requested = False

    def run(self):
        # 首先检查终止线程的标志
        if not self.stop_requested:   
            # 解决调试过程中无法停在QThread里的断点的问题，当不调试时记得注释掉这一行
            # debugpy.debug_this_thread()

            # 读取线数据和环境参数
            dictLineLists = py4cats.higstract(self.line_data,(self.wav_min,self.wav_max))
            mls = py4cats.atmRead(self.mls_data,extract=self.gas)

            # 计算光学厚度、透过率
            dodList = py4cats.lbl2od(mls,dictLineLists)
            todList = py4cats.dod2tod(dodList)
            # radNadir_0 = py4cats.dod2ri(dodList, obsAngle=180, tSurface='BoA',space=-6000) # 因为太阳被形容为温度为6000K的黑体，所以space=-6000代表太阳光谱，这个space变量也可以是文件名，即可从文件中读取辐射光谱
            # radNadir = radNadir_0.convolve(self.spec_Res, 'G') # 卷积操作

            # 更新进度条
            self.progressChanged.emit(10)
            # 定期检查终止线程的标志
            if self.stop_requested:
                self.progressChanged.emit(0)
                return

            # 计算辐射强度
            # 读取内容至字典中
            variables = {}
            filename = './typical_INP/' + self.atm_mode + '.INP'
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.split(' ')
                    if parts[0] == 'aerosol_modify':
                        parts[0] = parts[0] + ' ' + parts[1] + ' ' + parts[2]
                        variables[parts[0]] = parts[3]
                    else :
                        variables[parts[0]] = ' '.join(parts[1:])
            file.close()
            # 为防止出现波数起始值不统一的情况，直接使用todList的波数值，即原始线数据的实际波数值，不使用UI界面上读取的波数值
            # 同时需要注意，这里的波长值必须与太阳光谱kurudz_full.txt里的波长值完全一致，不然Libradtran无法运行
            column_kurudz_wav = []
            # 读取太阳光谱kurudz_full.txt里的波长值
            with open('kurudz_full.txt','r') as f:
                lines = f.readlines()
            f.close()
            for line in lines :
                parts = line.split()
                if not parts[0].startswith('#'):
                    column_kurudz_wav.append(float(parts[0]))
            # 找到第一个大于wavelength_min的波长值(这一行很耗时间，所以设置一个检查点)
            wavelength_min_input = min([wav for wav in column_kurudz_wav if wav > 1/(todList.grid()[-1]*10**(-7))])
            # 定期检查终止线程的标志
            if self.stop_requested:
                self.progressChanged.emit(0)
                return
            # 找到第一个小于wavelength_max的波长值(这一行很耗时间，所以设置一个检查点)
            wavelength_max_input = max([wav for wav in column_kurudz_wav if wav < 1/(todList.grid()[0]*10**(-7))])
            # 定期检查终止线程的标志
            if self.stop_requested:
                self.progressChanged.emit(0)
                return
            # 更新进度条
            self.progressChanged.emit(25)
            time.sleep(2)

            # 根据UI界面的参数修改INP文件
            variables['wavelength'] = str(wavelength_min_input) + ' ' + str(wavelength_max_input)
            variables['day_of_year'] = self.day_of_year
            variables['albedo'] = self.albedo
            variables['sza'] = int(self.sza)
            variables['phi0'] = self.phi0
            variables['umu'] = self.umu
            variables['phi'] = self.phi
            variables['mol_tau_file'] = 'abs ' + 'mol_tau_file_' + self.gas +'.txt'
            variables['atmosphere_file'] = './dat/USS_' + self.profile_num + '.dat'
            # variables['aerosol_visibility'] = self.vis
            # 将读取的变量写入INP文件
            filename_inp = 'UVSPEC_Clear_' + self.gas + '.INP'
            filename_out = 'UVSPEC_Clear_' + self.gas + '.out'
            with open(filename_inp, 'w') as file:
                for key, value in variables.items():
                    file.write(f"{key} {value}\n")
            file.close()
            # 计算分子光学厚度
            mol_tau_file.mol_tau(self,self.gas,self.wav_min,self.wav_max,self.line_data,self.mls_data,self.profile_num,self.stop_requested)

            # 更新进度条
            self.progressChanged.emit(60)
            # 定期检查终止线程的标志
            if self.stop_requested:
                self.progressChanged.emit(0)
                return
            # time.sleep(2)

            # 生成狭缝函数(光谱响应函数)
            run_command(f"../../libRadtran2.0.5/libRadtran-2.0.5/bin/make_slitfunction -f {self.FWHM} -r 0.01 -t {self.slit_type} > slit.dat")

            # 更新进度条
            self.progressChanged.emit(70)
            # 定期检查终止线程的标志
            if self.stop_requested:
                self.progressChanged.emit(0)
                return
            # time.sleep(2)

            # 控制命令行,TOA值用Libradtran的DISORT模型算，所有诊断消息将写入verbose.txt
            run_command(f"../../libRadtran2.0.5/libRadtran-2.0.5/bin/uvspec <{filename_inp}> {filename_out} 2> verbose.txt")

            # 打开文件并读取TOA数据
            with open(filename_out, 'r') as file:
                lines = file.readlines()
            file.close()
            # 创建空列表来存储第二列和第三列的数据
            column1 = []
            column2 = []
            column3 = []
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

            # 更新进度条
            self.progressChanged.emit(80)
            # 定期检查终止线程的标志
            if self.stop_requested:
                self.progressChanged.emit(0)
                return
            # time.sleep(2)

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
        
    def stop(self):
        self.stop_requested = True

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
    
    # 绘制大气模式
    atmos_mode()

    # 设置窗口图标、标题
    MainWindow.setWindowIcon(QIcon("logo.png"))
    MainWindow.setWindowTitle("Target gas radiation transfer simulation system")

    # screen = QGuiApplication.primaryScreen().size()
    # width = screen.width()
    # height = screen.height()
    MainWindow.resize(1280, 1100)

    MainWindow.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程