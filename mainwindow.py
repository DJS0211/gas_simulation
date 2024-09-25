# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from PySide6.QtCharts import QChartView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 1082)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.profile_TOD = QChartView(self.frame_5)
        self.profile_TOD.setObjectName(u"profile_TOD")
        sizePolicy.setHeightForWidth(self.profile_TOD.sizePolicy().hasHeightForWidth())
        self.profile_TOD.setSizePolicy(sizePolicy)
        self.profile_TOD.setFrameShape(QFrame.NoFrame)
        self.profile_TOD.setFrameShadow(QFrame.Plain)
        self.profile_TOD.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_5.addWidget(self.profile_TOD)

        self.profile_tran = QChartView(self.frame_5)
        self.profile_tran.setObjectName(u"profile_tran")
        sizePolicy.setHeightForWidth(self.profile_tran.sizePolicy().hasHeightForWidth())
        self.profile_tran.setSizePolicy(sizePolicy)
        self.profile_tran.setFrameShape(QFrame.NoFrame)
        self.profile_tran.setFrameShadow(QFrame.Plain)

        self.verticalLayout_5.addWidget(self.profile_tran)

        self.profile_radiance = QChartView(self.frame_5)
        self.profile_radiance.setObjectName(u"profile_radiance")
        sizePolicy.setHeightForWidth(self.profile_radiance.sizePolicy().hasHeightForWidth())
        self.profile_radiance.setSizePolicy(sizePolicy)
        self.profile_radiance.setFrameShape(QFrame.NoFrame)
        self.profile_radiance.setFrameShadow(QFrame.Plain)

        self.verticalLayout_5.addWidget(self.profile_radiance)

        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)
        self.verticalLayout_5.setStretch(2, 10)
        self.verticalLayout_5.setStretch(3, 10)
        self.verticalLayout_5.setStretch(4, 1)

        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.pushButton_hdf = QPushButton(self.frame_4)
        self.pushButton_hdf.setObjectName(u"pushButton_hdf")
        sizePolicy1.setHeightForWidth(self.pushButton_hdf.sizePolicy().hasHeightForWidth())
        self.pushButton_hdf.setSizePolicy(sizePolicy1)
        self.pushButton_hdf.setMinimumSize(QSize(0, 0))
        self.pushButton_hdf.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_hdf.setFont(font1)
        self.pushButton_hdf.setStyleSheet(u"border: 2px solid white;")

        self.verticalLayout_4.addWidget(self.pushButton_hdf)

        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem12)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font2);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem13)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font3);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font2);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font3);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font2);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font3);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font2);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font3);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font2);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font3);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font2);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font3);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.DashDotLine)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(152)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.tableWidget_2 = QTableWidget(self.frame_4)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        if (self.tableWidget_2.rowCount() < 6):
            self.tableWidget_2.setRowCount(6)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem32)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(76)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tableWidget_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 10)
        self.verticalLayout_4.setStretch(3, 10)

        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(10)
        self.tabWidget.setFont(font4)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_12 = QHBoxLayout(self.tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.comboBox_5 = QComboBox(self.tab)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_12.addWidget(self.comboBox_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBox_7 = QComboBox(self.tab_2)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_15.addWidget(self.comboBox_7)

        self.lineEdit_50 = QLineEdit(self.tab_2)
        self.lineEdit_50.setObjectName(u"lineEdit_50")

        self.horizontalLayout_15.addWidget(self.lineEdit_50)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.widget_17 = QWidget(self.frame_3)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_92 = QLabel(self.widget_17)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font1)
        self.label_92.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_92.setTextFormat(Qt.AutoText)

        self.horizontalLayout_16.addWidget(self.label_92)

        self.pushButton = QPushButton(self.widget_17)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(0, 31))
        self.pushButton.setMaximumSize(QSize(16777215, 31))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.pushButton)

        self.horizontalLayout_16.setStretch(0, 3)
        self.horizontalLayout_16.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.frame_3)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_94 = QLabel(self.widget_18)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font1)
        self.label_94.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_94.setTextFormat(Qt.AutoText)

        self.horizontalLayout_17.addWidget(self.label_94)

        self.pushButton_2 = QPushButton(self.widget_18)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(0, 31))
        self.pushButton_2.setMaximumSize(QSize(16777215, 31))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.pushButton_2)

        self.horizontalLayout_17.setStretch(0, 3)
        self.horizontalLayout_17.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_18)

        self.widget_20 = QWidget(self.frame_3)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy)
        self.horizontalLayout_19 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_96 = QLabel(self.widget_20)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font1)
        self.label_96.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_96.setTextFormat(Qt.AutoText)

        self.horizontalLayout_19.addWidget(self.label_96)

        self.lineEdit_59 = QLineEdit(self.widget_20)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        sizePolicy2.setHeightForWidth(self.lineEdit_59.sizePolicy().hasHeightForWidth())
        self.lineEdit_59.setSizePolicy(sizePolicy2)
        self.lineEdit_59.setMinimumSize(QSize(0, 31))
        self.lineEdit_59.setMaximumSize(QSize(16777215, 31))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.lineEdit_59.setFont(font5)
        self.lineEdit_59.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_19.addWidget(self.lineEdit_59)

        self.horizontalLayout_19.setStretch(0, 3)
        self.horizontalLayout_19.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_20)

        self.widget_22 = QWidget(self.frame_3)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.horizontalLayout_21 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_98 = QLabel(self.widget_22)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font1)
        self.label_98.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_98.setTextFormat(Qt.AutoText)

        self.horizontalLayout_21.addWidget(self.label_98)

        self.lineEdit_51 = QLineEdit(self.widget_22)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        sizePolicy2.setHeightForWidth(self.lineEdit_51.sizePolicy().hasHeightForWidth())
        self.lineEdit_51.setSizePolicy(sizePolicy2)
        self.lineEdit_51.setMinimumSize(QSize(0, 31))
        self.lineEdit_51.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_51.setFont(font5)
        self.lineEdit_51.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_21.addWidget(self.lineEdit_51)

        self.horizontalLayout_21.setStretch(0, 3)
        self.horizontalLayout_21.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_22)

        self.widget_21 = QWidget(self.frame_3)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_97 = QLabel(self.widget_21)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font1)
        self.label_97.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_97.setTextFormat(Qt.AutoText)

        self.horizontalLayout_20.addWidget(self.label_97)

        self.lineEdit_55 = QLineEdit(self.widget_21)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        sizePolicy2.setHeightForWidth(self.lineEdit_55.sizePolicy().hasHeightForWidth())
        self.lineEdit_55.setSizePolicy(sizePolicy2)
        self.lineEdit_55.setMinimumSize(QSize(0, 31))
        self.lineEdit_55.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_55.setFont(font5)
        self.lineEdit_55.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_20.addWidget(self.lineEdit_55)

        self.horizontalLayout_20.setStretch(0, 3)
        self.horizontalLayout_20.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_21)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(5, 1)
        self.verticalLayout_3.setStretch(6, 1)

        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.widget_25 = QWidget(self.frame_2)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy)
        self.widget_25.setStyleSheet(u"border-color: rgb(170, 0, 0);")
        self.verticalLayout_7 = QVBoxLayout(self.widget_25)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_105 = QLabel(self.widget_26)
        self.label_105.setObjectName(u"label_105")
        sizePolicy.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy)
        self.label_105.setFont(font1)
        self.label_105.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_105.setTextFormat(Qt.AutoText)

        self.horizontalLayout_22.addWidget(self.label_105)

        self.comboBox_6 = QComboBox(self.widget_26)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setFont(font2)

        self.horizontalLayout_22.addWidget(self.comboBox_6)


        self.verticalLayout_7.addWidget(self.widget_26)

        self.widget_14 = QWidget(self.widget_25)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.widget_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 2)

        self.label_9 = QLabel(self.widget_14)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 2, 2)

        self.lineEdit_5 = QLineEdit(self.widget_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font5)
        self.lineEdit_5.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget_14)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font5)
        self.lineEdit_6.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_2.addWidget(self.lineEdit_6, 6, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_14)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font5)
        self.lineEdit_4.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_2.addWidget(self.lineEdit_4, 4, 2, 1, 1)

        self.label_8 = QLabel(self.widget_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)

        self.lineEdit = QLineEdit(self.widget_14)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font5)
        self.lineEdit.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_12 = QLabel(self.widget_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 2)

        self.label_13 = QLabel(self.widget_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_2.addWidget(self.label_13, 6, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.widget_14)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 2, 1, 1)

        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_14)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font5)
        self.lineEdit_3.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_14)


        self.verticalLayout_2.addWidget(self.widget_25)

        self.widget_8 = QWidget(self.frame_2)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_85 = QLabel(self.widget_8)
        self.label_85.setObjectName(u"label_85")
        sizePolicy.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy)
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_85.setTextFormat(Qt.AutoText)

        self.horizontalLayout_8.addWidget(self.label_85)

        self.lineEdit_45 = QLineEdit(self.widget_8)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_45.sizePolicy().hasHeightForWidth())
        self.lineEdit_45.setSizePolicy(sizePolicy)
        self.lineEdit_45.setMinimumSize(QSize(0, 0))
        self.lineEdit_45.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_45.setFont(font5)
        self.lineEdit_45.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_8.addWidget(self.lineEdit_45)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.frame_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_89 = QLabel(self.widget_9)
        self.label_89.setObjectName(u"label_89")
        sizePolicy.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy)
        self.label_89.setFont(font1)
        self.label_89.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_89.setTextFormat(Qt.AutoText)

        self.horizontalLayout_9.addWidget(self.label_89)

        self.lineEdit_42 = QLineEdit(self.widget_9)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_42.sizePolicy().hasHeightForWidth())
        self.lineEdit_42.setSizePolicy(sizePolicy)
        self.lineEdit_42.setMinimumSize(QSize(0, 0))
        self.lineEdit_42.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_42.setFont(font3)
        self.lineEdit_42.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_9.addWidget(self.lineEdit_42)

        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.frame_2)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_90 = QLabel(self.widget_10)
        self.label_90.setObjectName(u"label_90")
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        self.label_90.setFont(font1)
        self.label_90.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_90.setTextFormat(Qt.AutoText)

        self.horizontalLayout_10.addWidget(self.label_90)

        self.lineEdit_44 = QLineEdit(self.widget_10)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_44.sizePolicy().hasHeightForWidth())
        self.lineEdit_44.setSizePolicy(sizePolicy)
        self.lineEdit_44.setMinimumSize(QSize(0, 0))
        self.lineEdit_44.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_44.setFont(font5)
        self.lineEdit_44.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_10.addWidget(self.lineEdit_44)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.frame_2)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_87 = QLabel(self.widget_11)
        self.label_87.setObjectName(u"label_87")
        sizePolicy.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy)
        self.label_87.setFont(font1)
        self.label_87.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_87.setTextFormat(Qt.AutoText)

        self.horizontalLayout_11.addWidget(self.label_87)

        self.lineEdit_41 = QLineEdit(self.widget_11)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy)
        self.lineEdit_41.setMinimumSize(QSize(0, 0))
        self.lineEdit_41.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_41.setFont(font5)
        self.lineEdit_41.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_11.addWidget(self.lineEdit_41)

        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_11)

        self.widget_13 = QWidget(self.frame_2)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_102 = QLabel(self.widget_13)
        self.label_102.setObjectName(u"label_102")
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        self.label_102.setFont(font1)
        self.label_102.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_102.setTextFormat(Qt.AutoText)

        self.horizontalLayout_13.addWidget(self.label_102)

        self.comboBox_4 = QComboBox(self.widget_13)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QSize(0, 0))
        self.comboBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_4.setFont(font2)
        self.comboBox_4.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_13.addWidget(self.comboBox_4)

        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.frame_2)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_103 = QLabel(self.widget_15)
        self.label_103.setObjectName(u"label_103")
        sizePolicy.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy)
        self.label_103.setFont(font1)
        self.label_103.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_103.setTextFormat(Qt.AutoText)

        self.horizontalLayout_14.addWidget(self.label_103)

        self.lineEdit_54 = QLineEdit(self.widget_15)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_54.sizePolicy().hasHeightForWidth())
        self.lineEdit_54.setSizePolicy(sizePolicy)
        self.lineEdit_54.setMinimumSize(QSize(0, 0))
        self.lineEdit_54.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_54.setFont(font5)
        self.lineEdit_54.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_14.addWidget(self.lineEdit_54)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_15)

        self.widget_24 = QWidget(self.frame_2)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy)
        self.horizontalLayout_25 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_104 = QLabel(self.widget_24)
        self.label_104.setObjectName(u"label_104")
        sizePolicy.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy)
        self.label_104.setFont(font1)
        self.label_104.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_104.setTextFormat(Qt.AutoText)

        self.horizontalLayout_25.addWidget(self.label_104)

        self.lineEdit_56 = QLineEdit(self.widget_24)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_56.sizePolicy().hasHeightForWidth())
        self.lineEdit_56.setSizePolicy(sizePolicy)
        self.lineEdit_56.setMinimumSize(QSize(0, 0))
        self.lineEdit_56.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_56.setFont(font5)
        self.lineEdit_56.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_25.addWidget(self.lineEdit_56)

        self.horizontalLayout_25.setStretch(0, 3)
        self.horizontalLayout_25.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_24)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"border: 1px solid gray;\n"
"border-radius: 8px;\n"
"#margin:0 0 0 0 px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QFrame\n"
"{\n"
"#border: 2px solid gray;\n"
"margin:0 0 0 0 px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_75 = QLabel(self.widget)
        self.label_75.setObjectName(u"label_75")
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setFont(font1)
        self.label_75.setStyleSheet(u"QLabel\n"
"{\n"
"border: 0px solid gray;\n"
"}")
        self.label_75.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label_75)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setFont(font5)
        self.comboBox.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox.setStyleSheet(u"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_76 = QLabel(self.widget_2)
        self.label_76.setObjectName(u"label_76")
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setFont(font1)
        self.label_76.setStyleSheet(u"QLabel\n"
"{\n"
"border: 0px solid gray;\n"
"}")
        self.label_76.setTextFormat(Qt.AutoText)

        self.horizontalLayout_2.addWidget(self.label_76)

        self.lineEdit_33 = QLineEdit(self.widget_2)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_33.sizePolicy().hasHeightForWidth())
        self.lineEdit_33.setSizePolicy(sizePolicy)
        self.lineEdit_33.setMinimumSize(QSize(0, 0))
        self.lineEdit_33.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_33.setFont(font5)
        self.lineEdit_33.setStyleSheet(u"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_2.addWidget(self.lineEdit_33)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_77 = QLabel(self.widget_3)
        self.label_77.setObjectName(u"label_77")
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setFont(font1)
        self.label_77.setStyleSheet(u"QLabel\n"
"{\n"
"border: 0px solid gray;\n"
"}")
        self.label_77.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.label_77)

        self.lineEdit_34 = QLineEdit(self.widget_3)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_34.sizePolicy().hasHeightForWidth())
        self.lineEdit_34.setSizePolicy(sizePolicy)
        self.lineEdit_34.setMinimumSize(QSize(0, 0))
        self.lineEdit_34.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_34.setFont(font5)
        self.lineEdit_34.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_3.addWidget(self.lineEdit_34)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_78 = QLabel(self.widget_4)
        self.label_78.setObjectName(u"label_78")
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setFont(font1)
        self.label_78.setStyleSheet(u"QLabel\n"
"{\n"
"border: 0px solid gray;\n"
"}")
        self.label_78.setTextFormat(Qt.AutoText)

        self.horizontalLayout_4.addWidget(self.label_78)

        self.lineEdit_35 = QLineEdit(self.widget_4)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_35.sizePolicy().hasHeightForWidth())
        self.lineEdit_35.setSizePolicy(sizePolicy)
        self.lineEdit_35.setMinimumSize(QSize(0, 0))
        self.lineEdit_35.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_35.setFont(font5)
        self.lineEdit_35.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_4.addWidget(self.lineEdit_35)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_79 = QLabel(self.widget_5)
        self.label_79.setObjectName(u"label_79")
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setFont(font1)
        self.label_79.setStyleSheet(u"QLabel\n"
"{\n"
"border: 0px solid gray;\n"
"}")
        self.label_79.setTextFormat(Qt.AutoText)

        self.horizontalLayout_5.addWidget(self.label_79)

        self.comboBox_3 = QComboBox(self.widget_5)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QSize(0, 0))
        self.comboBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_3.setFont(font5)
        self.comboBox_3.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_5.addWidget(self.comboBox_3)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_80 = QLabel(self.widget_6)
        self.label_80.setObjectName(u"label_80")
        sizePolicy.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy)
        self.label_80.setFont(font1)
        self.label_80.setStyleSheet(u"QLabel\n"
"{\n"
"border: 0px solid gray;\n"
"}")
        self.label_80.setTextFormat(Qt.AutoText)

        self.horizontalLayout_6.addWidget(self.label_80)

        self.lineEdit_40 = QLineEdit(self.widget_6)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy)
        self.lineEdit_40.setMinimumSize(QSize(0, 0))
        self.lineEdit_40.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_40.setFont(font5)
        self.lineEdit_40.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_6.addWidget(self.lineEdit_40)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.pushButton_start = QPushButton(self.widget_7)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QSize(0, 0))
        self.pushButton_start.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_start.setFont(font1)
        self.pushButton_start.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.widget_7)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setMinimumSize(QSize(0, 0))
        self.pushButton_stop.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_stop.setFont(font1)
        self.pushButton_stop.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pushButton_stop)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_7)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"\u6977\u4f53"])
        font6.setPointSize(26)
        self.label_3.setFont(font6)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.widget_23 = QWidget(self.frame_7)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.widget_23)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.widget_23)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setItalic(False)
        self.comboBox_2.setFont(font7)

        self.horizontalLayout_23.addWidget(self.comboBox_2)


        self.verticalLayout_6.addWidget(self.widget_23)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.profile_Tem = QChartView(self.frame_6)
        self.profile_Tem.setObjectName(u"profile_Tem")
        sizePolicy.setHeightForWidth(self.profile_Tem.sizePolicy().hasHeightForWidth())
        self.profile_Tem.setSizePolicy(sizePolicy)
        self.profile_Tem.setFrameShape(QFrame.NoFrame)
        self.profile_Tem.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_24.addWidget(self.profile_Tem)

        self.profile_Hum = QChartView(self.frame_6)
        self.profile_Hum.setObjectName(u"profile_Hum")
        sizePolicy.setHeightForWidth(self.profile_Hum.sizePolicy().hasHeightForWidth())
        self.profile_Hum.setSizePolicy(sizePolicy)
        self.profile_Hum.setFrameShape(QFrame.NoFrame)
        self.profile_Hum.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_24.addWidget(self.profile_Hum)

        self.profile_Pre = QChartView(self.frame_6)
        self.profile_Pre.setObjectName(u"profile_Pre")
        sizePolicy.setHeightForWidth(self.profile_Pre.sizePolicy().hasHeightForWidth())
        self.profile_Pre.setSizePolicy(sizePolicy)
        self.profile_Pre.setFrameShape(QFrame.NoFrame)
        self.profile_Pre.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_24.addWidget(self.profile_Pre)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 8)

        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_7.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u78b3\u536b\u661f\u6a21\u62df\u8f93\u51fa", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.pushButton_hdf.setText(QCoreApplication.translate("MainWindow", u"hdf\u8f93\u51fa", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1\u503c", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2\u503c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3\u503c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"4\u503c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"5\u503c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"6\u503c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u8f90\u4eae\u5ea6\u6700\u5927\u503c", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u8f90\u4eae\u5ea6\u6700\u5c0f\u503c", None));
        ___qtablewidgetitem15 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u8f90\u4eae\u5ea6\u4e2d\u4f4d\u6570", None));
        ___qtablewidgetitem16 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u5149\u5b66\u539a\u5ea6\u6700\u5927\u503c", None));
        ___qtablewidgetitem17 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u5149\u5b66\u539a\u5ea6\u6700\u5c0f\u503c", None));
        ___qtablewidgetitem18 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u5149\u5b66\u539a\u5ea6\u4e2d\u4f4d\u6570", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u957f", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u8f90\u4eae\u5ea6", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u53c2\u6570", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e38\u7eff\u9488\u53f6\u6797", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5e38\u7eff\u9614\u53f6\u6797", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"\u843d\u53f6\u9488\u53f6\u6797", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"\u843d\u53f6\u9614\u53f6\u6797", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6df7\u4ea4\u6797", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5c01\u95ed\u704c\u6728\u4e1b", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5f00\u9614\u704c\u6728\u4e1b", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"\u68ee\u6797\u8349\u539f", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"\u7a00\u6811\u8349\u539f", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"\u8349\u539f", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"\u6c38\u4e45\u6e7f\u5730", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("MainWindow", u"\u8015\u5730", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("MainWindow", u"\u57ce\u5e02\u548c\u5efa\u7b51", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("MainWindow", u"\u8015\u5730/\u81ea\u7136\u690d\u88ab\u6df7\u5408", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("MainWindow", u"\u6c38\u4e45\u51b0\u96ea", None))
        self.comboBox_5.setItemText(15, QCoreApplication.translate("MainWindow", u"\u6c99\u6f20/\u4f4e\u690d\u88ab\u8986\u76d6", None))
        self.comboBox_5.setItemText(16, QCoreApplication.translate("MainWindow", u"\u6c34\u4f53", None))
        self.comboBox_5.setItemText(17, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u7ecf\u7eac\u5ea6", None))

        self.comboBox_5.setCurrentText(QCoreApplication.translate("MainWindow", u"\u5e38\u7eff\u9488\u53f6\u6797", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5730\u8868\u7c7b\u578b", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u503c", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u7ecf\u7eac\u5ea6", None))

        self.lineEdit_50.setText(QCoreApplication.translate("MainWindow", u"0.3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5730\u8868\u53cd\u5c04\u7387", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"DEM", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8...", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u7c97\u7cd9\u5ea6", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8...", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u6eb6\u80f6ssa", None))
        self.lineEdit_59.setText(QCoreApplication.translate("MainWindow", u"0.85", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u6eb6\u80f6gg", None))
        self.lineEdit_51.setText(QCoreApplication.translate("MainWindow", u"0.7", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"\u80fd\u89c1\u5ea6/km", None))
        self.lineEdit_55.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u53c2\u6570", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"\u5149\u6e90", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"\u592a\u9633", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e3b\u52a8\u5149\u6e90", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u6d4b\u5668\u9ad8\u5ea6/km", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u5149\u8109\u51b2\u80fd\u91cf/J", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u63a2\u6d4b\u5668\u9762\u79ef/m<span style=\" vertical-align:super;\">2</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u5206\u8fa8\u7387/km", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u6d4b\u5c42\u6570", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u6d4b\u5668\u6548\u7387", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u592a\u9633\u5929\u9876\u89d2/\u00b0", None))
        self.lineEdit_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u592a\u9633\u65b9\u4f4d\u89d2/\u00b0", None))
        self.lineEdit_42.setText(QCoreApplication.translate("MainWindow", u"40.0", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b\u5929\u9876\u89d2", None))
        self.lineEdit_44.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b\u65b9\u4f4d\u89d2/\u00b0", None))
        self.lineEdit_41.setText(QCoreApplication.translate("MainWindow", u"90.0", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"\u54cd\u5e94\u51fd\u6570\u7c7b\u578b", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ad8\u65af", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e09\u89d2", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"\u77e9\u5f62", None))

        self.label_103.setText(QCoreApplication.translate("MainWindow", u"\u534a\u9ad8\u5168\u5bbd/nm", None))
        self.lineEdit_54.setText(QCoreApplication.translate("MainWindow", u"0.75", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"\u536b\u661f\u59ff\u6001\u89d2", None))
        self.lineEdit_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u53c2\u6570", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u5178\u578b\u6d89\u78b3\u6c14\u4f53", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CO2", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CH4", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"NO2", None))

        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u957fmin/nm</p></body></html>", None))
        self.lineEdit_33.setText(QCoreApplication.translate("MainWindow", u"1571", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u957fmax/nm</p></body></html>", None))
        self.lineEdit_34.setText(QCoreApplication.translate("MainWindow", u"1574", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u5149\u8c31\u5206\u8fa8\u7387", None))
        self.lineEdit_35.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u5ed3\u7ebf\u9009\u62e9", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"36", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"100m", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"200m", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"500m", None))

        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6c14\u4f53\u6a21\u578b", None))
        self.lineEdit_40.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6c14\u4f53\u8f90\u5c04\u4f20\u8f93\u4eff\u771f\u7cfb\u7edf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5927\u6c14\u6a21\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6674\u6717\u5929\u7a7a", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u591a\u4e91", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6c99\u5c18", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u8f7b\u5ea6\u96fe\u973e", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u4e2d\u5ea6\u96fe\u973e", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u91cd\u5ea6\u96fe\u973e", None))

    # retranslateUi

