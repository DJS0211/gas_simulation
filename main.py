from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QToolButton, QAbstractButton, QWidgetAction, QMenu, QComboBox
from PySide6.QtGui import QGuiApplication, QColor, QPalette, QAction, QIcon, QDesktopServices,QFont
from mainwindow import Ui_MainWindow
import sys
import py4cats
import matplotlib.pyplot as plt
import numpy as np	
import math
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
from PySide6.QtCharts import QChart,QChartView,QAbstractAxis,QAbstractSeries,QValueAxis,QLineSeries
from PySide6.QtCore import QMargins,Qt,QRectF
# import time
# # 指定字体名称
# rcParams['font.family'] = 'Arial'


class window(QtWidgets.QMainWindow, Ui_MainWindow):
    # 定义自定义信号
    landSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 设置ComboBox的样式表
        self.comboBox.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }")
        self.comboBox_2.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }") 
        self.comboBox_3.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }")

        # 连接start按钮，触发LBLRTM模型
        self.pushButton_start.clicked.connect(self.startLBLRTM)
        # 连接stop按钮
        self.pushButton_stop.clicked.connect(self.stopLBLRTM)

    def startLBLRTM(self):
        # MainWindow 的这些组件是在主线程中创建的，所以需要确保所有与 GUI 相关的操作都在主线程中执行
        # 读取界面参数
        gas = MainWindow.comboBox.currentText()
        wav_min = int(MainWindow.lineEdit_33.text())
        wav_max = int(MainWindow.lineEdit_34.text())
        spec_Res = float(MainWindow.lineEdit_35.text())
        line_data = './data/HITRAN/HITRAN_' + gas + '.par'
        mls_data = './data/atmos/' + MainWindow.comboBox_3.currentText() + '/mls.xy'

        # 创建线程实例时传递参数
        self.lblrtm_thread = LBLRTMThread(gas, wav_min, wav_max, spec_Res, line_data, mls_data)
        # 连接信号与槽
        self.lblrtm_thread.resultReady.connect(self.handle_result)
        
        # 启动线程来运行LBLRTM函数
        self.lblrtm_thread.start()

    def stopLBLRTM(self):
        # 终止线程的运行
        if self.lblrtm_thread.isRunning():
            self.lblrtm_thread.terminate()
    
    # 处理计算结果的槽函数，用于更新UI界面
    @QtCore.Slot(tuple) # @QtCore.Slot() 是一个装饰器，用于将一个普通的 Python 方法标记为一个槽函数（slot）;这种装饰器语法是可选的，但它有助于提高代码的可读性和表现性。
    def handle_result(self, chart_data):
        chart_od_data, chart_tran_data, chart_radiance_data = chart_data
        # 使用接收到的数据创建和更新 QChart 对象
        chart_od = LBLRTM_plot('光学厚度', *chart_od_data, 'Wavenumber', 'TOD')
        self.profile_TOD.setChart(chart_od)
        chart_tran = LBLRTM_plot('透过率', *chart_tran_data, 'Wavenumber', 'Transmittance')
        self.profile_tran.setChart(chart_tran)
        chart_radiance = LBLRTM_plot('辐射强度', *chart_radiance_data, 'Wavenumber', 'Radiance')
        self.profile_radiance.setChart(chart_radiance)

class LBLRTMThread(QtCore.QThread):
    # 定义一个带有结果的信号
    resultReady = QtCore.Signal(tuple)

    def __init__(self, gas, wav_min, wav_max, spec_Res, line_data, mls_data):
        super().__init__()  # 调用父类的初始化方法
        self.gas = gas
        self.wav_min = wav_min
        self.wav_max = wav_max
        self.spec_Res = spec_Res
        self.line_data = line_data
        self.mls_data = mls_data

    def run(self):
        # 读取线数据和环境参数
        dictLineLists = py4cats.higstract(self.line_data,(self.wav_min,self.wav_max))
        mls = py4cats.atmRead(self.mls_data,extract=self.gas)

        # 计算光学厚度、辐射强度
        dodList = py4cats.lbl2od(mls,dictLineLists)
        todList = py4cats.dod2tod(dodList)
        radNadir_0 = py4cats.dod2ri(dodList, obsAngle=180, tSurface='BoA',space=-6000) #因为太阳被形容为温度为6000K的黑体，所以space=-6000代表太阳光谱，这个space变量也可以是文件名，即可从文件中读取辐射光谱
        radNadir = radNadir_0.convolve(self.spec_Res, 'G') # 卷积操作

        # 计算绘图所需的数据
        chart_od_data = (todList.grid(), np.log10(todList.base))
        tranList = np.exp(-2 * todList)
        chart_tran_data = (todList.grid(), tranList.base)
        chart_radiance_data = (radNadir.grid(), radNadir * (10 ** 7))

        # 发出信号，携带绘图数据，因为 QChart 是一个继承自 QGraphicsView 的 QWidget，因此它应该在 GUI 线程（主线程）中创建和操作。
        self.resultReady.emit((chart_od_data, chart_tran_data, chart_radiance_data))

def LBLRTM_plot(chart_titie,x_data,y_data,x_label,y_label):
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
    # 创建数据序列
    series = QLineSeries()
    for i in range(len(x_data)):
        series.append(x_data[i],y_data[i])
    chart.addSeries(series)
    # 创建并设置 X 轴
    axisX = QValueAxis()
    axisX.setTitleText(x_label)  # 设置 X 轴标题
    # 创建并设置 Y 轴
    axisY = QValueAxis()
    axisY.setTitleText(y_label)  # 设置 Y 轴标题
    # 将 series 与坐标轴关联
    chart.setAxisX(axisX, series)  # 将 X 轴与 series 关联
    chart.setAxisY(axisY, series)  # 将 Y 轴与 series 关联
    # 隐藏默认的图例
    chart.legend().setVisible(False)
    # 将结果传递给主线程，因为需要确保所有与 GUI 相关的操作都在主线程中执行
    return chart

def atmos_mode():
    global MainWindow  # 声明全局变量
    mls = py4cats.vmrRead('./data/atmos/USS/USS_16.xy')

    # 绘制大气模式-温度图
    mode_plot('温度',mls['T'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Temperature','Altitude',MainWindow.profile_Tem)
    # 绘制大气模式-湿度图
    mode_plot('湿度',mls['H2O'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Humidity','Altitude',MainWindow.profile_Hum)
    # 绘制大气模式-压强图
    mode_plot('压强',mls['p'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Pressure','Altitude',MainWindow.profile_Pre)

def mode_plot(chart_titie,x_data,y_data,x_label,y_label,chart_window):
    # 绘制大气模式图
    chart = QChart()
    chart.createDefaultAxes()
    chart.setTitle(chart_titie)
    # 设置标题字体大小
    font = QFont()
    font.setPointSize(12)
    chart.setTitleFont(font)
    # 设置外边距
    chart.setMargins(QMargins(0,0,0,0))
    # 创建数据序列
    series = QLineSeries()
    for i in range(len(x_data)):
        series.append(x_data[i],y_data[i])
    chart.addSeries(series)
    # 创建并设置 X 轴
    axisX = QValueAxis()
    axisX.setTitleText(x_label)  # 设置 X 轴标题
    # chart.addAxis(axisX, Qt.AlignBottom)  # 将 X 轴添加到 chart 中，并设置对齐方式
    # 创建并设置 Y 轴
    axisY = QValueAxis()
    axisY.setTitleText(y_label)  # 设置 Y 轴标题
    # chart.addAxis(axisY, Qt.AlignLeft)  # 将 Y 轴添加到 chart 中，并设置对齐方式
    # 将 series 与坐标轴关联
    chart.setAxisX(axisX, series)  # 将 X 轴与 series 关联
    chart.setAxisY(axisY, series)  # 将 Y 轴与 series 关联
    # 隐藏默认的图例
    chart.legend().setVisible(False)
    chart_window.setChart(chart)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = window()  # 创建窗体对象

    # 绘制大气模式
    atmos_mode()

    # 设置窗口图标、标题
    MainWindow.setWindowIcon(QIcon("logo.png"))
    MainWindow.setWindowTitle("Target gas radiation transfer simulation system")

    # screen = QGuiApplication.primaryScreen().size()
    # width = screen.width()
    # height = screen.height()
    # MainWindow.resize(1081, 757)

    MainWindow.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程