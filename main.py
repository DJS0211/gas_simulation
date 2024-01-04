from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QToolButton, QAbstractButton, QWidgetAction, QMenu, QComboBox
from PySide6.QtGui import QGuiApplication, QColor, QPalette, QAction, QIcon, QDesktopServices
from mainwindow import Ui_Form
import sys
import py4cats
import matplotlib.pyplot as plt
import numpy as np	
import math
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams
# import time
# # 指定字体名称
# rcParams['font.family'] = 'Arial'


class window(QtWidgets.QMainWindow, Ui_Form):
    # 定义自定义信号
    landSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 设置ComboBox的样式表
        self.comboBox.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }")
        self.comboBox_2.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }") 
        self.comboBox_3.setStyleSheet("QComboBox::drop-down { border: 1px solid #ffffff; }")

        # 创建线程实例
        self.lblrtm_thread = LBLRTMThread()

        # 连接start按钮，触发LBLRTM模型
        self.pushButton_start.clicked.connect(self.startLBLRTM)
        # 连接stop按钮
        self.pushButton_stop.clicked.connect(self.stopLBLRTM)

    def startLBLRTM(self):
        # 启动线程来运行LBLRTM函数
        self.lblrtm_thread.start()

    def stopLBLRTM(self):
        # 终止线程的运行
        if self.lblrtm_thread.isRunning():
            self.lblrtm_thread.terminate()

    # # 将主窗口对象传递到其他文件中
    # def get_main_window(self):
    #     return self

class LBLRTMThread(QtCore.QThread):
    def run(self):
        # 在这里运行LBLRTM函数
        LBLRTM()

def LBLRTM():
    global MainWindow  # 声明全局变量
    # 读取界面参数
    gas = MainWindow.comboBox.currentText()
    wav_min = int(MainWindow.lineEdit_33.text())
    wav_max = int(MainWindow.lineEdit_34.text())
    spec_Res = float(MainWindow.lineEdit_35.text())
    line_data = './data/HITRAN/HITRAN_' + gas + '.par'
    mls_data = './data/atmos/' + MainWindow.comboBox_3.currentText() + '/mls.xy'
    
    # 读取线数据和环境参数
    dictLineLists = py4cats.higstract(line_data,(wav_min,wav_max))
    mls = py4cats.atmRead(mls_data,extract=gas)

    # 计算光学厚度、辐射强度
    dodList = py4cats.lbl2od(mls,dictLineLists)
    todList = py4cats.dod2tod(dodList)
    radNadir_0 = py4cats.dod2ri(dodList, obsAngle=180, tSurface='BoA',space=-6000) #因为太阳被形容为温度为6000K的黑体，所以space=-6000代表太阳光谱，这个space变量也可以是文件名，即可从文件中读取辐射光谱
    radNadir = radNadir_0.convolve(spec_Res, 'G') # 卷积操作

    # 绘制光学厚度图
    fig=plt.figure(figsize=(620/100, 200/100),dpi=100,facecolor='none')
    ax = fig.add_subplot(111)  # 添加子图
    ax.plot(todList.grid(),np.log10(todList.base),linewidth=2, color = 'yellow', alpha=1.0)
    # 添加横纵坐标标注
    # font = FontProperties(family='Arial', style='normal', size=12) # 创建一个字体属性对象，指定字体名称和大小
    # ax.set_xlabel('Wavenumber/$cm^{-1}$')
    # ax.set_ylabel('光学厚度', fontproperties=font)
    ax.set_ylabel('TOD',labelpad=1)
    # 设置横坐标只出现三个刻度
    xticks = [wav_min,(wav_min+wav_max)/2,wav_max]
    ax.set_xticks(xticks)
    # 设置坐标轴的颜色为白色
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    # 设置坐标轴标签的颜色为白色
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    # 设置坐标轴刻度的颜色为白色
    ax.tick_params(axis='both', colors='white')
    # 启用网格线
    ax.grid(True)
    # 保存图片
    plt.savefig('plot_tod.png', transparent=True)
    MainWindow.label_TOD.setStyleSheet("border-image: url(./plot_tod.png);")

    # 绘制透过率图
    tranList = np.exp(-2*todList)
    fig=plt.figure(figsize=(620/100, 200/100),dpi=100,facecolor='none')
    ax = fig.add_subplot(111)  # 添加子图
    # 以防透过率对应的横坐标出错，这里使用todList的横坐标数据
    ax.plot(todList.grid(),tranList.base,linewidth=2, color = 'yellow', alpha=1.0)
    # 添加横纵坐标标注
    # ax.set_xlabel('Wavenumber/$cm^{-1}$',fontsize = 25)
    ax.set_ylabel('transmittance',labelpad=1)
    # 设置横坐标只出现三个刻度
    xticks = [wav_min,(wav_min+wav_max)/2,wav_max]
    ax.set_xticks(xticks)
    # 设置坐标轴的颜色为白色
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    # 设置坐标轴标签的颜色为白色
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    # 设置坐标轴刻度的颜色为白色
    ax.tick_params(axis='both', colors='white')
    # 启用网格线
    ax.grid(True)
    # 保存图片
    plt.savefig('plot_tran.png', transparent=True)
    MainWindow.label_tran.setStyleSheet("border-image: url(./plot_tran.png);")

    # 绘制辐射强度图
    fig=plt.figure(figsize=(620/100, 200/100),dpi=100,facecolor='none')
    ax = fig.add_subplot(111)  # 添加子图
    ax.plot(radNadir.grid(),radNadir*(10**7),linewidth=2, color = 'yellow', alpha=1.0)
    # 添加横纵坐标标注
    # ax.set_xlabel('Wavenumber/$cm^{-1}$',fontsize = 25)
    ax.set_ylabel(r'radiance/(w/$cm^2$/sr/nm))',labelpad=1)
    # 设置横坐标只出现三个刻度
    xticks = [wav_min,(wav_min+wav_max)/2,wav_max]
    ax.set_xticks(xticks)
    # 设置坐标轴的颜色为白色
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    # 设置坐标轴标签的颜色为白色
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    # 设置坐标轴刻度的颜色为白色
    ax.tick_params(axis='both', colors='white')
    # 启用网格线
    ax.grid(True)
    # 保存图片
    plt.savefig('plot_ri.png', transparent=True)
    MainWindow.label_radiance.setStyleSheet("border-image: url(./plot_ri.png);")

def atmos_mode():
    global MainWindow  # 声明全局变量
    mls = py4cats.atmRead('./data/atmos/USS/USS_16.xy')

    # 绘制大气模式-温度图
    mode_plot(mls['T'],py4cats.unitConversion(mls['z'], 'length', new='km'),'Temperature / K','Altitude / km',MainWindow.label_tem,'./mode_picture/T.png')
    # 绘制大气模式-湿度图(不知为何，H2O的值无法从xy文件中获取，后面记得解决问题)
    H2O = [7.74e+03,6.07e+03,4.63e+03,3.18e+03,2.16e+03,925,367,70,5,3.9,4.43,4.72,5.03,5.22,4.75,3.5]
    mode_plot(H2O,py4cats.unitConversion(mls['z'], 'length', new='km'),'ppm','Altitude / km',MainWindow.label_H2O,'./mode_picture/H2O.png')
    # 绘制大气模式-压强图
    mode_plot(mls['p'],py4cats.unitConversion(mls['z'], 'length', new='km'),r'Pressure $p \rm\,[g/cm/s^2]$','Altitude / km',MainWindow.label_pre,'./mode_picture/p.png')

def mode_plot(x_data,y_data,x_label,y_label,label_window,save_filename):
    # 绘制大气模式-压强图
    fig=plt.figure(figsize=(700/100, 600/100),dpi=100,facecolor='none')
    ax = fig.add_subplot(111)  # 添加子图
    ax.plot(x_data,y_data,linewidth=3, color = 'yellow', alpha=1.0)
    # 添加横纵坐标标注
    ax.set_xlabel(x_label,labelpad=1 , fontsize = 20)
    ax.set_ylabel(y_label, labelpad=1 , fontsize = 20)
    # 设置坐标轴的颜色为白色
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    # 设置坐标轴标签的颜色为白色
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    # 设置坐标轴刻度的颜色为白色
    ax.tick_params(axis='both', colors='white',labelsize = 20)
    # 启用网格线
    ax.grid(True)
    # 保存图片
    plt.savefig(save_filename, transparent=True)
    label_window.setStyleSheet(f"border-image: url({save_filename});")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = window()  # 创建窗体对象

    # 绘制大气模式
    atmos_mode()
    
    # 设置主题颜色
    file = open("psblack.css", 'r')
    qss = file.read()
    paletteColor = qss[20:27]
    MainWindow.setPalette(QPalette(QColor(paletteColor)))
    MainWindow.setStyleSheet(qss)
    file.close()

    # 设置窗口图标、标题
    MainWindow.setWindowIcon(QIcon("logo.png"))
    MainWindow.setWindowTitle("Target gas radiation transfer simulation system")

    # screen = QGuiApplication.primaryScreen().size()
    # width = screen.width()
    # height = screen.height()
    # MainWindow.resize(1081, 757)

    MainWindow.show()  # 显示窗体
    sys.exit(app.exec())  # 程序关闭时退出进程