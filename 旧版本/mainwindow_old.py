# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_old.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import pic_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1077, 761)
        self.frame_res_2 = QFrame(Form)
        self.frame_res_2.setObjectName(u"frame_res_2")
        self.frame_res_2.setGeometry(QRect(-10, 0, 1081, 771))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.frame_res_2.setFont(font)
        self.frame_res_2.setStyleSheet(u"")
        self.frame_res_2.setFrameShape(QFrame.StyledPanel)
        self.frame_res_2.setFrameShadow(QFrame.Raised)
        self.label_73 = QLabel(self.frame_res_2)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(10, 0, 1081, 757))
        self.label_73.setStyleSheet(u"border-image: url(:/pic/background_1220.png);")
        self.widget_11 = QWidget(self.frame_res_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(32, 110, 221, 291))
        self.gridLayout_6 = QGridLayout(self.widget_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_78 = QLabel(self.widget_11)
        self.label_78.setObjectName(u"label_78")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_78.setFont(font1)
        self.label_78.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_78.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_78, 3, 0, 1, 1)

        self.label_77 = QLabel(self.widget_11)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font1)
        self.label_77.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_77.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_77, 2, 0, 1, 1)

        self.lineEdit_33 = QLineEdit(self.widget_11)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_33.sizePolicy().hasHeightForWidth())
        self.lineEdit_33.setSizePolicy(sizePolicy)
        self.lineEdit_33.setMinimumSize(QSize(81, 31))
        self.lineEdit_33.setMaximumSize(QSize(81, 31))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.lineEdit_33.setFont(font2)
        self.lineEdit_33.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_6.addWidget(self.lineEdit_33, 1, 1, 1, 1)

        self.label_79 = QLabel(self.widget_11)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font1)
        self.label_79.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_79.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_79, 4, 0, 1, 1)

        self.pushButton_start = QPushButton(self.widget_11)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(81, 0))
        self.pushButton_start.setMaximumSize(QSize(81, 16777215))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(12)
        self.pushButton_start.setFont(font3)
        self.pushButton_start.setStyleSheet(u"border: 2px solid white;")

        self.gridLayout_6.addWidget(self.pushButton_start, 6, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.widget_11)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 31))
        self.comboBox_3.setMaximumSize(QSize(16777215, 31))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(12)
        self.comboBox_3.setFont(font4)
        self.comboBox_3.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_6.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.lineEdit_34 = QLineEdit(self.widget_11)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_34.sizePolicy().hasHeightForWidth())
        self.lineEdit_34.setSizePolicy(sizePolicy)
        self.lineEdit_34.setMinimumSize(QSize(81, 31))
        self.lineEdit_34.setMaximumSize(QSize(81, 31))
        self.lineEdit_34.setFont(font2)
        self.lineEdit_34.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_6.addWidget(self.lineEdit_34, 2, 1, 1, 1)

        self.lineEdit_35 = QLineEdit(self.widget_11)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_35.sizePolicy().hasHeightForWidth())
        self.lineEdit_35.setSizePolicy(sizePolicy)
        self.lineEdit_35.setMinimumSize(QSize(81, 31))
        self.lineEdit_35.setMaximumSize(QSize(81, 31))
        self.lineEdit_35.setFont(font2)
        self.lineEdit_35.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_6.addWidget(self.lineEdit_35, 3, 1, 1, 1)

        self.label_80 = QLabel(self.widget_11)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font1)
        self.label_80.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_80.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_80, 5, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.widget_11)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(81, 0))
        self.pushButton_stop.setMaximumSize(QSize(81, 16777215))
        self.pushButton_stop.setFont(font3)
        self.pushButton_stop.setStyleSheet(u"border: 2px solid white;")

        self.gridLayout_6.addWidget(self.pushButton_stop, 6, 1, 1, 1)

        self.label_75 = QLabel(self.widget_11)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font1)
        self.label_75.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_75.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_75, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(0, 31))
        self.comboBox.setMaximumSize(QSize(16777215, 31))
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_6.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_76 = QLabel(self.widget_11)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font1)
        self.label_76.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_76.setTextFormat(Qt.AutoText)

        self.gridLayout_6.addWidget(self.label_76, 1, 0, 1, 1)

        self.lineEdit_40 = QLineEdit(self.widget_11)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy)
        self.lineEdit_40.setMinimumSize(QSize(81, 31))
        self.lineEdit_40.setMaximumSize(QSize(81, 31))
        self.lineEdit_40.setFont(font2)
        self.lineEdit_40.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_6.addWidget(self.lineEdit_40, 5, 1, 1, 1)

        self.widget_13 = QWidget(self.frame_res_2)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(29, 450, 231, 291))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.gridLayout_7 = QGridLayout(self.widget_13)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_44 = QLineEdit(self.widget_13)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_44.sizePolicy().hasHeightForWidth())
        self.lineEdit_44.setSizePolicy(sizePolicy)
        self.lineEdit_44.setMinimumSize(QSize(81, 31))
        self.lineEdit_44.setMaximumSize(QSize(81, 31))
        self.lineEdit_44.setFont(font2)
        self.lineEdit_44.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_7.addWidget(self.lineEdit_44, 2, 1, 1, 1)

        self.label_88 = QLabel(self.widget_13)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font1)
        self.label_88.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_88.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_88, 4, 0, 1, 1)

        self.lineEdit_53 = QLineEdit(self.widget_13)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_53.sizePolicy().hasHeightForWidth())
        self.lineEdit_53.setSizePolicy(sizePolicy)
        self.lineEdit_53.setMinimumSize(QSize(81, 31))
        self.lineEdit_53.setMaximumSize(QSize(81, 31))
        self.lineEdit_53.setFont(font2)
        self.lineEdit_53.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_7.addWidget(self.lineEdit_53, 5, 1, 1, 1)

        self.label_89 = QLabel(self.widget_13)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font1)
        self.label_89.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_89.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_89, 1, 0, 1, 1)

        self.label_90 = QLabel(self.widget_13)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font1)
        self.label_90.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_90.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_90, 2, 0, 1, 1)

        self.label_85 = QLabel(self.widget_13)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font1)
        self.label_85.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_85.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_85, 0, 0, 1, 1)

        self.lineEdit_41 = QLineEdit(self.widget_13)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy)
        self.lineEdit_41.setMinimumSize(QSize(81, 31))
        self.lineEdit_41.setMaximumSize(QSize(81, 31))
        self.lineEdit_41.setFont(font2)
        self.lineEdit_41.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_7.addWidget(self.lineEdit_41, 3, 1, 1, 1)

        self.lineEdit_43 = QLineEdit(self.widget_13)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_43.sizePolicy().hasHeightForWidth())
        self.lineEdit_43.setSizePolicy(sizePolicy)
        self.lineEdit_43.setMinimumSize(QSize(81, 31))
        self.lineEdit_43.setMaximumSize(QSize(81, 31))
        self.lineEdit_43.setFont(font2)
        self.lineEdit_43.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_7.addWidget(self.lineEdit_43, 4, 1, 1, 1)

        self.label_102 = QLabel(self.widget_13)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font1)
        self.label_102.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_102.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_102, 5, 0, 1, 1)

        self.lineEdit_45 = QLineEdit(self.widget_13)
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

        self.gridLayout_7.addWidget(self.lineEdit_45, 0, 1, 1, 1)

        self.lineEdit_42 = QLineEdit(self.widget_13)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_42.sizePolicy().hasHeightForWidth())
        self.lineEdit_42.setSizePolicy(sizePolicy)
        self.lineEdit_42.setMinimumSize(QSize(81, 31))
        self.lineEdit_42.setMaximumSize(QSize(81, 31))
        self.lineEdit_42.setFont(font2)
        self.lineEdit_42.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_7.addWidget(self.lineEdit_42, 1, 1, 1, 1)

        self.label_87 = QLabel(self.widget_13)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font1)
        self.label_87.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_87.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_87, 3, 0, 1, 1)

        self.label_103 = QLabel(self.widget_13)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font1)
        self.label_103.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_103.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.label_103, 6, 0, 1, 1)

        self.lineEdit_54 = QLineEdit(self.widget_13)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_54.sizePolicy().hasHeightForWidth())
        self.lineEdit_54.setSizePolicy(sizePolicy)
        self.lineEdit_54.setMinimumSize(QSize(81, 31))
        self.lineEdit_54.setMaximumSize(QSize(81, 31))
        self.lineEdit_54.setFont(font2)
        self.lineEdit_54.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_7.addWidget(self.lineEdit_54, 6, 1, 1, 1)

        self.widget_14 = QWidget(self.frame_res_2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setGeometry(QRect(848, 110, 221, 281))
        self.gridLayout_8 = QGridLayout(self.widget_14)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_47 = QLineEdit(self.widget_14)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        sizePolicy.setHeightForWidth(self.lineEdit_47.sizePolicy().hasHeightForWidth())
        self.lineEdit_47.setSizePolicy(sizePolicy)
        self.lineEdit_47.setMinimumSize(QSize(81, 31))
        self.lineEdit_47.setMaximumSize(QSize(81, 31))
        self.lineEdit_47.setFont(font2)
        self.lineEdit_47.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_47, 1, 1, 1, 1)

        self.lineEdit_49 = QLineEdit(self.widget_14)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        sizePolicy.setHeightForWidth(self.lineEdit_49.sizePolicy().hasHeightForWidth())
        self.lineEdit_49.setSizePolicy(sizePolicy)
        self.lineEdit_49.setMinimumSize(QSize(81, 31))
        self.lineEdit_49.setMaximumSize(QSize(81, 31))
        self.lineEdit_49.setFont(font2)
        self.lineEdit_49.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_49, 2, 1, 1, 1)

        self.label_98 = QLabel(self.widget_14)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font1)
        self.label_98.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_98.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_98, 6, 0, 1, 1)

        self.lineEdit_50 = QLineEdit(self.widget_14)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        sizePolicy.setHeightForWidth(self.lineEdit_50.sizePolicy().hasHeightForWidth())
        self.lineEdit_50.setSizePolicy(sizePolicy)
        self.lineEdit_50.setMinimumSize(QSize(81, 31))
        self.lineEdit_50.setMaximumSize(QSize(81, 31))
        self.lineEdit_50.setFont(font2)
        self.lineEdit_50.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_50, 0, 1, 1, 1)

        self.label_93 = QLabel(self.widget_14)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font1)
        self.label_93.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_93.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_93, 3, 0, 1, 1)

        self.lineEdit_46 = QLineEdit(self.widget_14)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        sizePolicy.setHeightForWidth(self.lineEdit_46.sizePolicy().hasHeightForWidth())
        self.lineEdit_46.setSizePolicy(sizePolicy)
        self.lineEdit_46.setMinimumSize(QSize(81, 31))
        self.lineEdit_46.setMaximumSize(QSize(81, 31))
        self.lineEdit_46.setFont(font2)
        self.lineEdit_46.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_46, 3, 1, 1, 1)

        self.lineEdit_52 = QLineEdit(self.widget_14)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        sizePolicy.setHeightForWidth(self.lineEdit_52.sizePolicy().hasHeightForWidth())
        self.lineEdit_52.setSizePolicy(sizePolicy)
        self.lineEdit_52.setMinimumSize(QSize(81, 31))
        self.lineEdit_52.setMaximumSize(QSize(81, 31))
        self.lineEdit_52.setFont(font2)
        self.lineEdit_52.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_52, 4, 1, 1, 1)

        self.lineEdit_55 = QLineEdit(self.widget_14)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        sizePolicy.setHeightForWidth(self.lineEdit_55.sizePolicy().hasHeightForWidth())
        self.lineEdit_55.setSizePolicy(sizePolicy)
        self.lineEdit_55.setMinimumSize(QSize(81, 31))
        self.lineEdit_55.setMaximumSize(QSize(81, 31))
        self.lineEdit_55.setFont(font2)
        self.lineEdit_55.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_55, 5, 1, 1, 1)

        self.label_92 = QLabel(self.widget_14)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font1)
        self.label_92.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_92.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_92, 1, 0, 1, 1)

        self.label_94 = QLabel(self.widget_14)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font1)
        self.label_94.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_94.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_94, 2, 0, 1, 1)

        self.label_97 = QLabel(self.widget_14)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font1)
        self.label_97.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_97.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_97, 5, 0, 1, 1)

        self.lineEdit_51 = QLineEdit(self.widget_14)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        sizePolicy.setHeightForWidth(self.lineEdit_51.sizePolicy().hasHeightForWidth())
        self.lineEdit_51.setSizePolicy(sizePolicy)
        self.lineEdit_51.setMinimumSize(QSize(81, 31))
        self.lineEdit_51.setMaximumSize(QSize(81, 31))
        self.lineEdit_51.setFont(font2)
        self.lineEdit_51.setStyleSheet(u"border-style: outset; \n"
"border-width: 1px; \n"
"border-style:solid;\n"
"border-color: rgb(81,97,230);")

        self.gridLayout_8.addWidget(self.lineEdit_51, 6, 1, 1, 1)

        self.label_95 = QLabel(self.widget_14)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font1)
        self.label_95.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_95.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_95, 0, 0, 1, 1)

        self.label_96 = QLabel(self.widget_14)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font1)
        self.label_96.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_96.setTextFormat(Qt.AutoText)

        self.gridLayout_8.addWidget(self.label_96, 4, 0, 1, 1)

        self.label_tem = QLabel(self.frame_res_2)
        self.label_tem.setObjectName(u"label_tem")
        self.label_tem.setGeometry(QRect(280, 113, 200, 200))
        self.label_tem.setStyleSheet(u"")
        self.label_H2O = QLabel(self.frame_res_2)
        self.label_H2O.setObjectName(u"label_H2O")
        self.label_H2O.setGeometry(QRect(460, 113, 200, 200))
        font5 = QFont()
        font5.setFamilies([u"\u9ed1\u4f53"])
        font5.setPointSize(13)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_H2O.setFont(font5)
        self.label_H2O.setStyleSheet(u"")
        self.label_TOD = QLabel(self.frame_res_2)
        self.label_TOD.setObjectName(u"label_TOD")
        self.label_TOD.setGeometry(QRect(270, 355, 620, 120))
        self.label_TOD.setStyleSheet(u"")
        self.label_output = QLabel(self.frame_res_2)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setGeometry(QRect(850, 501, 211, 241))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_output.setFont(font6)
        self.label_output.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_output.setTextFormat(Qt.PlainText)
        self.label_output.setScaledContents(True)
        self.label_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.comboBox_2 = QComboBox(self.frame_res_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(480, 80, 131, 24))
        self.comboBox_2.setFont(font1)
        self.label_81 = QLabel(self.frame_res_2)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(290, 110, 61, 31))
        self.label_81.setFont(font1)
        self.label_81.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_81.setTextFormat(Qt.AutoText)
        self.label_82 = QLabel(self.frame_res_2)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(470, 110, 51, 31))
        self.label_82.setFont(font1)
        self.label_82.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_82.setTextFormat(Qt.AutoText)
        self.label_83 = QLabel(self.frame_res_2)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(650, 110, 71, 31))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_83.setTextFormat(Qt.AutoText)
        self.label_pre = QLabel(self.frame_res_2)
        self.label_pre.setObjectName(u"label_pre")
        self.label_pre.setGeometry(QRect(640, 113, 200, 200))
        self.label_pre.setFont(font5)
        self.label_pre.setStyleSheet(u"")
        self.label_tran = QLabel(self.frame_res_2)
        self.label_tran.setObjectName(u"label_tran")
        self.label_tran.setGeometry(QRect(270, 480, 620, 120))
        self.label_tran.setStyleSheet(u"")
        self.label_radiance = QLabel(self.frame_res_2)
        self.label_radiance.setObjectName(u"label_radiance")
        self.label_radiance.setGeometry(QRect(270, 620, 605, 120))
        self.label_radiance.setStyleSheet(u"")
        self.label_91 = QLabel(self.frame_res_2)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(280, 340, 111, 31))
        self.label_91.setFont(font1)
        self.label_91.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_91.setTextFormat(Qt.AutoText)
        self.label_99 = QLabel(self.frame_res_2)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(280, 460, 91, 31))
        self.label_99.setFont(font1)
        self.label_99.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_99.setTextFormat(Qt.AutoText)
        self.label_100 = QLabel(self.frame_res_2)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(280, 600, 101, 31))
        self.label_100.setFont(font1)
        self.label_100.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.label_100.setTextFormat(Qt.AutoText)
        self.pushButton_visual = QPushButton(self.frame_res_2)
        self.pushButton_visual.setObjectName(u"pushButton_visual")
        self.pushButton_visual.setGeometry(QRect(840, 460, 131, 36))
        self.pushButton_visual.setMinimumSize(QSize(81, 0))
        self.pushButton_visual.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_visual.setFont(font3)
        self.pushButton_visual.setStyleSheet(u"border: 2px solid white;")
        self.pushButton_hdf = QPushButton(self.frame_res_2)
        self.pushButton_hdf.setObjectName(u"pushButton_hdf")
        self.pushButton_hdf.setGeometry(QRect(975, 460, 101, 36))
        self.pushButton_hdf.setMinimumSize(QSize(81, 0))
        self.pushButton_hdf.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_hdf.setFont(font3)
        self.pushButton_hdf.setStyleSheet(u"border: 2px solid white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_73.setText("")
        self.label_78.setText(QCoreApplication.translate("Form", u"\u5149\u8c31\u5206\u8fa8\u7387", None))
        self.label_77.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u6ce2\u6570max/cm<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.lineEdit_33.setText(QCoreApplication.translate("Form", u"6355", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"\u5ed3\u7ebf\u9009\u62e9", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"15", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"20", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"25", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"32", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Form", u"50", None))

        self.lineEdit_34.setText(QCoreApplication.translate("Form", u"6365", None))
        self.lineEdit_35.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.label_80.setText(QCoreApplication.translate("Form", u"\u65b9\u4f4d\u89d2", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"\u5178\u578b\u6d89\u78b3\u6c14\u4f53", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"CO2", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"CH4", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"NO2", None))

        self.label_76.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u6ce2\u6570min/cm<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.lineEdit_40.setText(QCoreApplication.translate("Form", u"29", None))
        self.lineEdit_44.setText(QCoreApplication.translate("Form", u"5", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u6548\u7387", None))
        self.lineEdit_53.setText(QCoreApplication.translate("Form", u"20", None))
        self.label_89.setText(QCoreApplication.translate("Form", u"\u89c6\u573a\u89d2 (deg)", None))
        self.label_90.setText(QCoreApplication.translate("Form", u"\u91c7\u6837\u7387 (GHz)", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"\u671b\u8fdc\u955c\u53e3\u5f84 (m)", None))
        self.lineEdit_41.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.lineEdit_43.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_102.setText(QCoreApplication.translate("Form", u"\u4fe1\u566a\u6bd4", None))
        self.lineEdit_45.setText(QCoreApplication.translate("Form", u"0.638", None))
        self.lineEdit_42.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_87.setText(QCoreApplication.translate("Form", u"\u900f\u8fc7\u7387", None))
        self.label_103.setText(QCoreApplication.translate("Form", u"\u80cc\u666f\u566a\u58f0\u56e0\u5b50", None))
        self.lineEdit_54.setText(QCoreApplication.translate("Form", u"5", None))
        self.lineEdit_47.setText(QCoreApplication.translate("Form", u"50", None))
        self.lineEdit_49.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_98.setText(QCoreApplication.translate("Form", u"\u53cd\u5c04\u7387", None))
        self.lineEdit_50.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_93.setText(QCoreApplication.translate("Form", u"\u5730\u8868\u7c7b\u578b", None))
        self.lineEdit_46.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.lineEdit_52.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_55.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_92.setText(QCoreApplication.translate("Form", u"\u6c14\u6eb6\u80f6", None))
        self.label_94.setText(QCoreApplication.translate("Form", u"\u4e91", None))
        self.label_97.setText(QCoreApplication.translate("Form", u"DEM", None))
        self.lineEdit_51.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.label_95.setText(QCoreApplication.translate("Form", u"\u5927\u6c14\u5ed3\u7ebf", None))
        self.label_96.setText(QCoreApplication.translate("Form", u"\u7c97\u7cd9\u5ea6", None))
        self.label_tem.setText("")
        self.label_H2O.setText("")
        self.label_TOD.setText("")
        self.label_output.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u6674\u6717\u5929\u7a7a", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"\u591a\u4e91", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"\u6c99\u5c18", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form", u"\u8f7b\u5ea6\u96fe\u973e", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Form", u"\u4e2d\u5ea6\u96fe\u973e", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Form", u"\u91cd\u5ea6\u96fe\u973e", None))

        self.label_81.setText(QCoreApplication.translate("Form", u"\u6e29\u5ea6", None))
        self.label_82.setText(QCoreApplication.translate("Form", u"\u6e7f\u5ea6", None))
        self.label_83.setText(QCoreApplication.translate("Form", u"\u538b\u5f3a", None))
        self.label_pre.setText("")
        self.label_tran.setText("")
        self.label_radiance.setText("")
        self.label_91.setText(QCoreApplication.translate("Form", u"\u5149\u5b66\u539a\u5ea6", None))
        self.label_99.setText(QCoreApplication.translate("Form", u"\u900f\u8fc7\u7387", None))
        self.label_100.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>TOA\u8f90\u5c04</p></body></html>", None))
        self.pushButton_visual.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u8f93\u51fa", None))
        self.pushButton_hdf.setText(QCoreApplication.translate("Form", u"hdf\u8f93\u51fa", None))
    # retranslateUi

