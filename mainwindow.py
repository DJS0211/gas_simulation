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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
from PySide6.QtCharts import QChartView
# from chartview import ChartView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(969, 999)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(18)
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
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_75 = QLabel(self.widget)
        self.label_75.setObjectName(u"label_75")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
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
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(0, 31))
        self.comboBox.setMaximumSize(QSize(16777215, 31))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_76 = QLabel(self.widget_2)
        self.label_76.setObjectName(u"label_76")
        sizePolicy1.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.lineEdit_33.sizePolicy().hasHeightForWidth())
        self.lineEdit_33.setSizePolicy(sizePolicy1)
        self.lineEdit_33.setMinimumSize(QSize(0, 31))
        self.lineEdit_33.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_33.setFont(font2)
        self.lineEdit_33.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_2.addWidget(self.lineEdit_33)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_77 = QLabel(self.widget_3)
        self.label_77.setObjectName(u"label_77")
        sizePolicy1.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.lineEdit_34.sizePolicy().hasHeightForWidth())
        self.lineEdit_34.setSizePolicy(sizePolicy1)
        self.lineEdit_34.setMinimumSize(QSize(0, 31))
        self.lineEdit_34.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_34.setFont(font2)
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
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_78 = QLabel(self.widget_4)
        self.label_78.setObjectName(u"label_78")
        sizePolicy1.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.lineEdit_35.sizePolicy().hasHeightForWidth())
        self.lineEdit_35.setSizePolicy(sizePolicy1)
        self.lineEdit_35.setMinimumSize(QSize(0, 31))
        self.lineEdit_35.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_35.setFont(font2)
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
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_79 = QLabel(self.widget_5)
        self.label_79.setObjectName(u"label_79")
        sizePolicy1.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy1)
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
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(0, 31))
        self.comboBox_3.setMaximumSize(QSize(16777215, 31))
        self.comboBox_3.setFont(font2)
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
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_80 = QLabel(self.widget_6)
        self.label_80.setObjectName(u"label_80")
        sizePolicy1.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy1)
        self.lineEdit_40.setMinimumSize(QSize(0, 31))
        self.lineEdit_40.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_40.setFont(font2)
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
        self.widget_7.setStyleSheet(u"QWidget\n"
"{\n"
"border: 1px solid gray;\n"
"border-radius: 8px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_start = QPushButton(self.widget_7)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(81, 0))
        self.pushButton_start.setMaximumSize(QSize(81, 16777215))
        self.pushButton_start.setFont(font1)
        self.pushButton_start.setStyleSheet(u"border: 2px solid white;")

        self.horizontalLayout_7.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.widget_7)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(81, 0))
        self.pushButton_stop.setMaximumSize(QSize(81, 16777215))
        self.pushButton_stop.setFont(font1)
        self.pushButton_stop.setStyleSheet(u"border: 2px solid white;")

        self.horizontalLayout_7.addWidget(self.pushButton_stop)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_7)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"\u6977\u4f53"])
        font3.setPointSize(26)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.widget_23 = QWidget(self.frame_7)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_7 = QLabel(self.widget_23)
        self.label_7.setObjectName(u"label_7")
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
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(16)
        font4.setBold(False)
        font4.setItalic(False)
        self.comboBox_2.setFont(font4)

        self.horizontalLayout_23.addWidget(self.comboBox_2)


        self.verticalLayout_6.addWidget(self.widget_23)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.profile_Tem = QChartView(self.frame_6)
        self.profile_Tem.setObjectName(u"profile_Tem")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profile_Tem.sizePolicy().hasHeightForWidth())
        self.profile_Tem.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.profile_Tem)

        self.profile_Hum = QChartView(self.frame_6)
        self.profile_Hum.setObjectName(u"profile_Hum")
        sizePolicy2.setHeightForWidth(self.profile_Hum.sizePolicy().hasHeightForWidth())
        self.profile_Hum.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.profile_Hum)

        self.profile_Pre = QChartView(self.frame_6)
        self.profile_Pre.setObjectName(u"profile_Pre")
        sizePolicy2.setHeightForWidth(self.profile_Pre.sizePolicy().hasHeightForWidth())
        self.profile_Pre.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.profile_Pre)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)

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

        self.widget_16 = QWidget(self.frame_3)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_95 = QLabel(self.widget_16)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font1)
        self.label_95.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_95.setTextFormat(Qt.AutoText)

        self.horizontalLayout_15.addWidget(self.label_95)

        self.lineEdit_50 = QLineEdit(self.widget_16)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        sizePolicy1.setHeightForWidth(self.lineEdit_50.sizePolicy().hasHeightForWidth())
        self.lineEdit_50.setSizePolicy(sizePolicy1)
        self.lineEdit_50.setMinimumSize(QSize(0, 31))
        self.lineEdit_50.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_50.setFont(font2)
        self.lineEdit_50.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_15.addWidget(self.lineEdit_50)

        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.frame_3)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_92 = QLabel(self.widget_17)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font1)
        self.label_92.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_92.setTextFormat(Qt.AutoText)

        self.horizontalLayout_16.addWidget(self.label_92)

        self.lineEdit_47 = QLineEdit(self.widget_17)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        sizePolicy1.setHeightForWidth(self.lineEdit_47.sizePolicy().hasHeightForWidth())
        self.lineEdit_47.setSizePolicy(sizePolicy1)
        self.lineEdit_47.setMinimumSize(QSize(0, 31))
        self.lineEdit_47.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_47.setFont(font2)
        self.lineEdit_47.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_16.addWidget(self.lineEdit_47)

        self.horizontalLayout_16.setStretch(0, 3)
        self.horizontalLayout_16.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.frame_3)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_94 = QLabel(self.widget_18)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font1)
        self.label_94.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_94.setTextFormat(Qt.AutoText)

        self.horizontalLayout_17.addWidget(self.label_94)

        self.lineEdit_49 = QLineEdit(self.widget_18)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        sizePolicy1.setHeightForWidth(self.lineEdit_49.sizePolicy().hasHeightForWidth())
        self.lineEdit_49.setSizePolicy(sizePolicy1)
        self.lineEdit_49.setMinimumSize(QSize(0, 31))
        self.lineEdit_49.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_49.setFont(font2)
        self.lineEdit_49.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_17.addWidget(self.lineEdit_49)

        self.horizontalLayout_17.setStretch(0, 3)
        self.horizontalLayout_17.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.frame_3)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_93 = QLabel(self.widget_19)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font1)
        self.label_93.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_93.setTextFormat(Qt.AutoText)

        self.horizontalLayout_18.addWidget(self.label_93)

        self.lineEdit_46 = QLineEdit(self.widget_19)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        sizePolicy1.setHeightForWidth(self.lineEdit_46.sizePolicy().hasHeightForWidth())
        self.lineEdit_46.setSizePolicy(sizePolicy1)
        self.lineEdit_46.setMinimumSize(QSize(0, 31))
        self.lineEdit_46.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_46.setFont(font2)
        self.lineEdit_46.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_18.addWidget(self.lineEdit_46)

        self.horizontalLayout_18.setStretch(0, 3)
        self.horizontalLayout_18.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.frame_3)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_96 = QLabel(self.widget_20)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font1)
        self.label_96.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_96.setTextFormat(Qt.AutoText)

        self.horizontalLayout_19.addWidget(self.label_96)

        self.lineEdit_52 = QLineEdit(self.widget_20)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        sizePolicy1.setHeightForWidth(self.lineEdit_52.sizePolicy().hasHeightForWidth())
        self.lineEdit_52.setSizePolicy(sizePolicy1)
        self.lineEdit_52.setMinimumSize(QSize(0, 31))
        self.lineEdit_52.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_52.setFont(font2)
        self.lineEdit_52.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_19.addWidget(self.lineEdit_52)

        self.horizontalLayout_19.setStretch(0, 3)
        self.horizontalLayout_19.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.frame_3)
        self.widget_21.setObjectName(u"widget_21")
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
        sizePolicy1.setHeightForWidth(self.lineEdit_55.sizePolicy().hasHeightForWidth())
        self.lineEdit_55.setSizePolicy(sizePolicy1)
        self.lineEdit_55.setMinimumSize(QSize(0, 31))
        self.lineEdit_55.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_55.setFont(font2)
        self.lineEdit_55.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_20.addWidget(self.lineEdit_55)

        self.horizontalLayout_20.setStretch(0, 3)
        self.horizontalLayout_20.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.frame_3)
        self.widget_22.setObjectName(u"widget_22")
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
        sizePolicy1.setHeightForWidth(self.lineEdit_51.sizePolicy().hasHeightForWidth())
        self.lineEdit_51.setSizePolicy(sizePolicy1)
        self.lineEdit_51.setMinimumSize(QSize(0, 31))
        self.lineEdit_51.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_51.setFont(font2)
        self.lineEdit_51.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_21.addWidget(self.lineEdit_51)

        self.horizontalLayout_21.setStretch(0, 3)
        self.horizontalLayout_21.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.widget_22)


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
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

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
        self.lineEdit_45.setMinimumSize(QSize(81, 31))
        self.lineEdit_45.setMaximumSize(QSize(81, 31))
        self.lineEdit_45.setFont(font2)
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
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_89 = QLabel(self.widget_9)
        self.label_89.setObjectName(u"label_89")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy3)
        self.label_89.setFont(font1)
        self.label_89.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_89.setTextFormat(Qt.AutoText)

        self.horizontalLayout_9.addWidget(self.label_89)

        self.lineEdit_42 = QLineEdit(self.widget_9)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_42.sizePolicy().hasHeightForWidth())
        self.lineEdit_42.setSizePolicy(sizePolicy3)
        self.lineEdit_42.setMinimumSize(QSize(81, 31))
        self.lineEdit_42.setMaximumSize(QSize(81, 31))
        self.lineEdit_42.setFont(font2)
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
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_90 = QLabel(self.widget_10)
        self.label_90.setObjectName(u"label_90")
        sizePolicy3.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy3)
        self.label_90.setFont(font1)
        self.label_90.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_90.setTextFormat(Qt.AutoText)

        self.horizontalLayout_10.addWidget(self.label_90)

        self.lineEdit_44 = QLineEdit(self.widget_10)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_44.sizePolicy().hasHeightForWidth())
        self.lineEdit_44.setSizePolicy(sizePolicy3)
        self.lineEdit_44.setMinimumSize(QSize(81, 31))
        self.lineEdit_44.setMaximumSize(QSize(81, 31))
        self.lineEdit_44.setFont(font2)
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
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_87 = QLabel(self.widget_11)
        self.label_87.setObjectName(u"label_87")
        sizePolicy3.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy3)
        self.label_87.setFont(font1)
        self.label_87.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_87.setTextFormat(Qt.AutoText)

        self.horizontalLayout_11.addWidget(self.label_87)

        self.lineEdit_41 = QLineEdit(self.widget_11)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy3)
        self.lineEdit_41.setMinimumSize(QSize(81, 31))
        self.lineEdit_41.setMaximumSize(QSize(81, 31))
        self.lineEdit_41.setFont(font2)
        self.lineEdit_41.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_11.addWidget(self.lineEdit_41)

        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.frame_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_88 = QLabel(self.widget_12)
        self.label_88.setObjectName(u"label_88")
        sizePolicy3.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy3)
        self.label_88.setFont(font1)
        self.label_88.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_88.setTextFormat(Qt.AutoText)

        self.horizontalLayout_12.addWidget(self.label_88)

        self.lineEdit_43 = QLineEdit(self.widget_12)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_43.sizePolicy().hasHeightForWidth())
        self.lineEdit_43.setSizePolicy(sizePolicy3)
        self.lineEdit_43.setMinimumSize(QSize(81, 31))
        self.lineEdit_43.setMaximumSize(QSize(81, 31))
        self.lineEdit_43.setFont(font2)
        self.lineEdit_43.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_12.addWidget(self.lineEdit_43)

        self.horizontalLayout_12.setStretch(0, 3)
        self.horizontalLayout_12.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.frame_2)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_102 = QLabel(self.widget_13)
        self.label_102.setObjectName(u"label_102")
        sizePolicy3.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy3)
        self.label_102.setFont(font1)
        self.label_102.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_102.setTextFormat(Qt.AutoText)

        self.horizontalLayout_13.addWidget(self.label_102)

        self.lineEdit_53 = QLineEdit(self.widget_13)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_53.sizePolicy().hasHeightForWidth())
        self.lineEdit_53.setSizePolicy(sizePolicy3)
        self.lineEdit_53.setMinimumSize(QSize(81, 31))
        self.lineEdit_53.setMaximumSize(QSize(81, 31))
        self.lineEdit_53.setFont(font2)
        self.lineEdit_53.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_13.addWidget(self.lineEdit_53)

        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.frame_2)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_103 = QLabel(self.widget_15)
        self.label_103.setObjectName(u"label_103")
        sizePolicy3.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy3)
        self.label_103.setFont(font1)
        self.label_103.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"")
        self.label_103.setTextFormat(Qt.AutoText)

        self.horizontalLayout_14.addWidget(self.label_103)

        self.lineEdit_54 = QLineEdit(self.widget_15)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_54.sizePolicy().hasHeightForWidth())
        self.lineEdit_54.setSizePolicy(sizePolicy3)
        self.lineEdit_54.setMinimumSize(QSize(81, 31))
        self.lineEdit_54.setMaximumSize(QSize(81, 31))
        self.lineEdit_54.setFont(font2)
        self.lineEdit_54.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.horizontalLayout_14.addWidget(self.lineEdit_54)


        self.verticalLayout_2.addWidget(self.widget_15)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.profile_TOD = QChartView(self.frame_5)
        self.profile_TOD.setObjectName(u"profile_TOD")
        sizePolicy2.setHeightForWidth(self.profile_TOD.sizePolicy().hasHeightForWidth())
        self.profile_TOD.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.profile_TOD)

        self.profile_tran = QChartView(self.frame_5)
        self.profile_tran.setObjectName(u"profile_tran")
        sizePolicy2.setHeightForWidth(self.profile_tran.sizePolicy().hasHeightForWidth())
        self.profile_tran.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.profile_tran)

        self.profile_radiance = QChartView(self.frame_5)
        self.profile_radiance.setObjectName(u"profile_radiance")
        sizePolicy2.setHeightForWidth(self.profile_radiance.sizePolicy().hasHeightForWidth())
        self.profile_radiance.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.profile_radiance)


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
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.widget_14 = QWidget(self.frame_4)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_visual = QPushButton(self.widget_14)
        self.pushButton_visual.setObjectName(u"pushButton_visual")
        sizePolicy.setHeightForWidth(self.pushButton_visual.sizePolicy().hasHeightForWidth())
        self.pushButton_visual.setSizePolicy(sizePolicy)
        self.pushButton_visual.setMinimumSize(QSize(0, 0))
        self.pushButton_visual.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_visual.setFont(font1)
        self.pushButton_visual.setStyleSheet(u"border: 2px solid white;")

        self.horizontalLayout_22.addWidget(self.pushButton_visual)

        self.pushButton_hdf = QPushButton(self.widget_14)
        self.pushButton_hdf.setObjectName(u"pushButton_hdf")
        sizePolicy.setHeightForWidth(self.pushButton_hdf.sizePolicy().hasHeightForWidth())
        self.pushButton_hdf.setSizePolicy(sizePolicy)
        self.pushButton_hdf.setMinimumSize(QSize(0, 0))
        self.pushButton_hdf.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_hdf.setFont(font1)
        self.pushButton_hdf.setStyleSheet(u"border: 2px solid white;")

        self.horizontalLayout_22.addWidget(self.pushButton_hdf)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.widget_14)

        self.graphicsView = QChartView(self.frame_4)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_4.addWidget(self.graphicsView)


        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u53c2\u6570", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u5178\u578b\u6d89\u78b3\u6c14\u4f53", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CO2", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CH4", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"NO2", None))

        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u6570min/cm<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.lineEdit_33.setText(QCoreApplication.translate("MainWindow", u"6355", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6ce2\u6570max/cm<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.lineEdit_34.setText(QCoreApplication.translate("MainWindow", u"6365", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u5149\u8c31\u5206\u8fa8\u7387", None))
        self.lineEdit_35.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u5ed3\u7ebf\u9009\u62e9", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"32", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"50", None))

        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u4f4d\u89d2", None))
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

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u53c2\u6570", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"\u5927\u6c14\u5ed3\u7ebf", None))
        self.lineEdit_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u6eb6\u80f6", None))
        self.lineEdit_47.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u4e91", None))
        self.lineEdit_49.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8868\u7c7b\u578b", None))
        self.lineEdit_46.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u7c97\u7cd9\u5ea6", None))
        self.lineEdit_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"DEM", None))
        self.lineEdit_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5c04\u7387", None))
        self.lineEdit_51.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u53c2\u6570", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u671b\u8fdc\u955c\u53e3\u5f84(m)", None))
        self.lineEdit_45.setText(QCoreApplication.translate("MainWindow", u"0.638", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u573a\u89d2(deg)", None))
        self.lineEdit_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u7387(GHz)", None))
        self.lineEdit_44.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u900f\u8fc7\u7387", None))
        self.lineEdit_41.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u6548\u7387", None))
        self.lineEdit_43.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u566a\u6bd4", None))
        self.lineEdit_53.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f\u566a\u58f0\u56e0\u5b50", None))
        self.lineEdit_54.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u78b3\u536b\u661f\u6a21\u62df\u8f93\u51fa", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u53c2\u6570", None))
        self.pushButton_visual.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316\u8f93\u51fa", None))
        self.pushButton_hdf.setText(QCoreApplication.translate("MainWindow", u"hdf\u8f93\u51fa", None))
    # retranslateUi

