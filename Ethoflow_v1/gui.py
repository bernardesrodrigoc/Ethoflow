# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_new.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ethoflow(object):
    def setupUi(self, ethoflow):
        ethoflow.setObjectName("ethoflow")
        ethoflow.resize(1229, 781)
        font = QtGui.QFont()
        font.setPointSize(10)
        ethoflow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon/name.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ethoflow.setWindowIcon(icon)
        ethoflow.setStyleSheet("QMainWindow {\n"
"    background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-color: #ececec;    \n"
"    color:#ececec;\n"
"    padding: 2px;\n"
"    background-color: #ececec;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-color: #ececec;\n"
"    background-color:#ececec;\n"
"    color: #ececec;\n"
"}\n"
"QLabel {\n"
"    color: #000000;\n"
"}\n"
"QLabel:disabled {\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(220, 220, 220), stop:1 rgb(220, 220, 220));\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"    color: #000000;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #000000;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    color: #000000;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(223,223,223);\n"
"        background-color:rgb(226,226,226);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:1px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #000000;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #000000;\n"
"}\n"
"QRadioButton {\n"
"    color: 000000;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"    border-color: color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(220, 220, 220), stop:1 rgb(220, 220, 220));\n"
"    background-color:color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(220, 220, 220), stop:1 rgb(220, 220, 220));\n"
"    color: color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(220, 220, 220), stop:1 rgb(220, 220, 220));\n"
"    \n"
"}")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.output_median_area = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_median_area.setFont(font)
        self.output_median_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_median_area.setAlignment(QtCore.Qt.AlignCenter)
        self.output_median_area.setObjectName("output_median_area")
        self.verticalLayout.addWidget(self.output_median_area)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.output_sd_area = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_sd_area.setFont(font)
        self.output_sd_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_sd_area.setAlignment(QtCore.Qt.AlignCenter)
        self.output_sd_area.setObjectName("output_sd_area")
        self.verticalLayout.addWidget(self.output_sd_area)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.max_area = QtWidgets.QLineEdit(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_area.setFont(font)
        self.max_area.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.max_area.setAlignment(QtCore.Qt.AlignCenter)
        self.max_area.setObjectName("max_area")
        self.verticalLayout_4.addWidget(self.max_area)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.min_area = QtWidgets.QLineEdit(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_area.setFont(font)
        self.min_area.setAlignment(QtCore.Qt.AlignCenter)
        self.min_area.setObjectName("min_area")
        self.verticalLayout_4.addWidget(self.min_area)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.output_max_area = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_max_area.setFont(font)
        self.output_max_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_max_area.setAlignment(QtCore.Qt.AlignCenter)
        self.output_max_area.setObjectName("output_max_area")
        self.verticalLayout_2.addWidget(self.output_max_area)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.output_min_area = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_min_area.setFont(font)
        self.output_min_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_min_area.setAlignment(QtCore.Qt.AlignCenter)
        self.output_min_area.setObjectName("output_min_area")
        self.verticalLayout_2.addWidget(self.output_min_area)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.output_max_len = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_max_len.setFont(font)
        self.output_max_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);")
        self.output_max_len.setAlignment(QtCore.Qt.AlignCenter)
        self.output_max_len.setObjectName("output_max_len")
        self.verticalLayout_5.addWidget(self.output_max_len)
        self.label_12 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.output_min_len = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_min_len.setFont(font)
        self.output_min_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_min_len.setAlignment(QtCore.Qt.AlignCenter)
        self.output_min_len.setObjectName("output_min_len")
        self.verticalLayout_5.addWidget(self.output_min_len)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.max_len = QtWidgets.QLineEdit(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_len.setFont(font)
        self.max_len.setAlignment(QtCore.Qt.AlignCenter)
        self.max_len.setObjectName("max_len")
        self.verticalLayout_6.addWidget(self.max_len)
        self.label_5 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.min_len = QtWidgets.QLineEdit(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_len.setFont(font)
        self.min_len.setAlignment(QtCore.Qt.AlignCenter)
        self.min_len.setObjectName("min_len")
        self.verticalLayout_6.addWidget(self.min_len)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.output_median_len = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_median_len.setFont(font)
        self.output_median_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_median_len.setAlignment(QtCore.Qt.AlignCenter)
        self.output_median_len.setObjectName("output_median_len")
        self.verticalLayout_3.addWidget(self.output_median_len)
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.output_sd_len = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_sd_len.setFont(font)
        self.output_sd_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.output_sd_len.setAlignment(QtCore.Qt.AlignCenter)
        self.output_sd_len.setObjectName("output_sd_len")
        self.verticalLayout_3.addWidget(self.output_sd_len)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_9, 0, 1, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_30 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_7.addWidget(self.label_30)
        self.output_max_prop = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_max_prop.setFont(font)
        self.output_max_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);")
        self.output_max_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.output_max_prop.setObjectName("output_max_prop")
        self.verticalLayout_7.addWidget(self.output_max_prop)
        self.label_29 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_7.addWidget(self.label_29)
        self.output_min_prop = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_min_prop.setFont(font)
        self.output_min_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);")
        self.output_min_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.output_min_prop.setObjectName("output_min_prop")
        self.verticalLayout_7.addWidget(self.output_min_prop)
        self.gridLayout_5.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_28 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_9.addWidget(self.label_28)
        self.max_prop = QtWidgets.QLineEdit(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_prop.setFont(font)
        self.max_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.max_prop.setObjectName("max_prop")
        self.verticalLayout_9.addWidget(self.max_prop)
        self.label_27 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_9.addWidget(self.label_27)
        self.min_prop = QtWidgets.QLineEdit(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_prop.setFont(font)
        self.min_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.min_prop.setObjectName("min_prop")
        self.verticalLayout_9.addWidget(self.min_prop)
        self.gridLayout_5.addLayout(self.verticalLayout_9, 1, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_31 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_8.addWidget(self.label_31)
        self.output_median_prop = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_median_prop.setFont(font)
        self.output_median_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);")
        self.output_median_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.output_median_prop.setObjectName("output_median_prop")
        self.verticalLayout_8.addWidget(self.output_median_prop)
        self.label_32 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_8.addWidget(self.label_32)
        self.output_sd_prop = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.output_sd_prop.setFont(font)
        self.output_sd_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);")
        self.output_sd_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.output_sd_prop.setObjectName("output_sd_prop")
        self.verticalLayout_8.addWidget(self.output_sd_prop)
        self.gridLayout_5.addLayout(self.verticalLayout_8, 1, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_12, 1, 0, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_38 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_10.addWidget(self.label_38)
        self.set_frame_resolution = QtWidgets.QLineEdit(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_frame_resolution.setFont(font)
        self.set_frame_resolution.setInputMask("")
        self.set_frame_resolution.setFrame(True)
        self.set_frame_resolution.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.set_frame_resolution.setAlignment(QtCore.Qt.AlignCenter)
        self.set_frame_resolution.setReadOnly(False)
        self.set_frame_resolution.setObjectName("set_frame_resolution")
        self.verticalLayout_10.addWidget(self.set_frame_resolution)
        self.Framenumber = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber.setFont(font)
        self.Framenumber.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber.setObjectName("Framenumber")
        self.verticalLayout_10.addWidget(self.Framenumber)
        self.frame_number = QtWidgets.QLineEdit(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_number.setFont(font)
        self.frame_number.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_number.setObjectName("frame_number")
        self.verticalLayout_10.addWidget(self.frame_number)
        self.gridLayout_9.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Framenumber_4 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_4.setFont(font)
        self.Framenumber_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_4.setObjectName("Framenumber_4")
        self.gridLayout_7.addWidget(self.Framenumber_4, 0, 0, 1, 1)
        self.Framenumber_5 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_5.setFont(font)
        self.Framenumber_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_5.setObjectName("Framenumber_5")
        self.gridLayout_7.addWidget(self.Framenumber_5, 0, 1, 1, 1)
        self.shape_1 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.shape_1.setFont(font)
        self.shape_1.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"\n"
"")
        self.shape_1.setAlignment(QtCore.Qt.AlignCenter)
        self.shape_1.setObjectName("shape_1")
        self.gridLayout_7.addWidget(self.shape_1, 1, 0, 1, 1)
        self.shape_0 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.shape_0.setFont(font)
        self.shape_0.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.shape_0.setAlignment(QtCore.Qt.AlignCenter)
        self.shape_0.setObjectName("shape_0")
        self.gridLayout_7.addWidget(self.shape_0, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Framenumber_3 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_3.setFont(font)
        self.Framenumber_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_3.setObjectName("Framenumber_3")
        self.horizontalLayout.addWidget(self.Framenumber_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("color: rgb(0, 0, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.gridLayout_8.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_15, 1, 1, 1, 1)
        self.verticalLayout_14.addWidget(self.groupBox_5)
        self.groupBox_16 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_16)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label2_9 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_9.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_9.setFont(font)
        self.label2_9.setAcceptDrops(False)
        self.label2_9.setStyleSheet("color: rgb(239, 41, 41);")
        self.label2_9.setTextFormat(QtCore.Qt.AutoText)
        self.label2_9.setScaledContents(True)
        self.label2_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_9.setWordWrap(True)
        self.label2_9.setObjectName("label2_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2_9)
        self.label2_8 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_8.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_8.setFont(font)
        self.label2_8.setAcceptDrops(False)
        self.label2_8.setTextFormat(QtCore.Qt.AutoText)
        self.label2_8.setScaledContents(False)
        self.label2_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_8.setWordWrap(True)
        self.label2_8.setObjectName("label2_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label2_8)
        self.gridLayout_12.addLayout(self.formLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox_20)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.calc_dist_scale = QtWidgets.QPushButton(self.splitter)
        self.calc_dist_scale.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_dist_scale.setFont(font)
        self.calc_dist_scale.setMouseTracking(False)
        self.calc_dist_scale.setObjectName("calc_dist_scale")
        self.distance_scale = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_scale.setFont(font)
        self.distance_scale.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_scale.setObjectName("distance_scale")
        self.horizontalLayout_2.addWidget(self.splitter)
        spacerItem = QtWidgets.QSpacerItem(78, 35, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_12.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_20)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label2_3 = QtWidgets.QLabel(self.splitter_2)
        self.label2_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_3.setFont(font)
        self.label2_3.setTextFormat(QtCore.Qt.AutoText)
        self.label2_3.setScaledContents(False)
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setObjectName("label2_3")
        self.distance_scale_know = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_scale_know.setFont(font)
        self.distance_scale_know.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_scale_know.setObjectName("distance_scale_know")
        self.gridLayout_12.addWidget(self.splitter_2, 2, 0, 1, 1)
        self.label2_2 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_2.setFont(font)
        self.label2_2.setAcceptDrops(False)
        self.label2_2.setTextFormat(QtCore.Qt.AutoText)
        self.label2_2.setScaledContents(True)
        self.label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_2.setWordWrap(True)
        self.label2_2.setObjectName("label2_2")
        self.gridLayout_12.addWidget(self.label2_2, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_20, 0, 0, 1, 1)
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_16)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label2_10 = QtWidgets.QLabel(self.groupBox_21)
        self.label2_10.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_10.setFont(font)
        self.label2_10.setAcceptDrops(False)
        self.label2_10.setAutoFillBackground(False)
        self.label2_10.setTextFormat(QtCore.Qt.AutoText)
        self.label2_10.setScaledContents(True)
        self.label2_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_10.setWordWrap(True)
        self.label2_10.setObjectName("label2_10")
        self.horizontalLayout_3.addWidget(self.label2_10)
        self.interaction_threshold = QtWidgets.QLineEdit(self.groupBox_21)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.interaction_threshold.setFont(font)
        self.interaction_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.interaction_threshold.setObjectName("interaction_threshold")
        self.horizontalLayout_3.addWidget(self.interaction_threshold)
        self.gridLayout_13.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.label2_4 = QtWidgets.QLabel(self.groupBox_21)
        self.label2_4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_4.setFont(font)
        self.label2_4.setAcceptDrops(False)
        self.label2_4.setAutoFillBackground(False)
        self.label2_4.setTextFormat(QtCore.Qt.AutoText)
        self.label2_4.setScaledContents(True)
        self.label2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_4.setWordWrap(True)
        self.label2_4.setObjectName("label2_4")
        self.gridLayout_13.addWidget(self.label2_4, 2, 0, 1, 1)
        self.label2_12 = QtWidgets.QLabel(self.groupBox_21)
        self.label2_12.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_12.setFont(font)
        self.label2_12.setAcceptDrops(False)
        self.label2_12.setStyleSheet("color: rgb(239, 41, 41);")
        self.label2_12.setTextFormat(QtCore.Qt.AutoText)
        self.label2_12.setScaledContents(True)
        self.label2_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_12.setWordWrap(True)
        self.label2_12.setObjectName("label2_12")
        self.gridLayout_13.addWidget(self.label2_12, 1, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_21, 0, 1, 1, 1)
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox_16)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_22.setFont(font)
        self.groupBox_22.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label2_11 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_11.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_11.setFont(font)
        self.label2_11.setAcceptDrops(False)
        self.label2_11.setAutoFillBackground(False)
        self.label2_11.setTextFormat(QtCore.Qt.AutoText)
        self.label2_11.setScaledContents(True)
        self.label2_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_11.setWordWrap(True)
        self.label2_11.setObjectName("label2_11")
        self.gridLayout_14.addWidget(self.label2_11, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label2_6 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_6.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label2_6.setFont(font)
        self.label2_6.setAcceptDrops(False)
        self.label2_6.setAutoFillBackground(False)
        self.label2_6.setTextFormat(QtCore.Qt.AutoText)
        self.label2_6.setScaledContents(True)
        self.label2_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_6.setWordWrap(True)
        self.label2_6.setObjectName("label2_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2_6)
        self.thersh_min_mov = QtWidgets.QLineEdit(self.groupBox_22)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thersh_min_mov.setFont(font)
        self.thersh_min_mov.setAlignment(QtCore.Qt.AlignCenter)
        self.thersh_min_mov.setObjectName("thersh_min_mov")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thersh_min_mov)
        self.gridLayout_14.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label2_7 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_7.setFont(font)
        self.label2_7.setAcceptDrops(False)
        self.label2_7.setAutoFillBackground(False)
        self.label2_7.setTextFormat(QtCore.Qt.AutoText)
        self.label2_7.setScaledContents(True)
        self.label2_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_7.setWordWrap(True)
        self.label2_7.setObjectName("label2_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2_7)
        self.thersh_max_mov = QtWidgets.QLineEdit(self.groupBox_22)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thersh_max_mov.setFont(font)
        self.thersh_max_mov.setAlignment(QtCore.Qt.AlignCenter)
        self.thersh_max_mov.setObjectName("thersh_max_mov")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thersh_max_mov)
        self.gridLayout_14.addLayout(self.formLayout_3, 2, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label2_13 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_13.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_13.setFont(font)
        self.label2_13.setAcceptDrops(False)
        self.label2_13.setStyleSheet("color: rgb(239, 41, 41);")
        self.label2_13.setTextFormat(QtCore.Qt.AutoText)
        self.label2_13.setScaledContents(True)
        self.label2_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_13.setWordWrap(True)
        self.label2_13.setObjectName("label2_13")
        self.verticalLayout_12.addWidget(self.label2_13)
        self.label2_14 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_14.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_14.setFont(font)
        self.label2_14.setAcceptDrops(False)
        self.label2_14.setAutoFillBackground(False)
        self.label2_14.setTextFormat(QtCore.Qt.AutoText)
        self.label2_14.setScaledContents(True)
        self.label2_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_14.setWordWrap(True)
        self.label2_14.setObjectName("label2_14")
        self.verticalLayout_12.addWidget(self.label2_14)
        self.gridLayout_14.addLayout(self.verticalLayout_12, 3, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_22, 0, 2, 1, 1)
        self.verticalLayout_14.addWidget(self.groupBox_16)
        self.gridLayout_19.addLayout(self.verticalLayout_14, 0, 0, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.upload_video = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(True)
        self.upload_video.setFont(font)
        self.upload_video.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.upload_video.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.upload_video.setAcceptDrops(False)
        self.upload_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.upload_video.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/uplaod_video1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_video.setIcon(icon1)
        self.upload_video.setIconSize(QtCore.QSize(40, 40))
        self.upload_video.setShortcut("")
        self.upload_video.setObjectName("upload_video")
        self.gridLayout_18.addWidget(self.upload_video, 0, 0, 1, 1)
        self.run_video = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.run_video.setFont(font)
        self.run_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_video.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon/run_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_video.setIcon(icon2)
        self.run_video.setIconSize(QtCore.QSize(40, 40))
        self.run_video.setObjectName("run_video")
        self.gridLayout_18.addWidget(self.run_video, 0, 1, 1, 1)
        self.read_parameters = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.read_parameters.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icon/read_parameters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.read_parameters.setIcon(icon3)
        self.read_parameters.setIconSize(QtCore.QSize(40, 40))
        self.read_parameters.setObjectName("read_parameters")
        self.gridLayout_18.addWidget(self.read_parameters, 1, 0, 1, 1)
        self.stop_view_video = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stop_view_video.setFont(font)
        self.stop_view_video.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icon/stop_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_view_video.setIcon(icon4)
        self.stop_view_video.setIconSize(QtCore.QSize(40, 40))
        self.stop_view_video.setObjectName("stop_view_video")
        self.gridLayout_18.addWidget(self.stop_view_video, 1, 1, 1, 1)
        self.save_parameters = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_parameters.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icon/save_parameters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_parameters.setIcon(icon5)
        self.save_parameters.setIconSize(QtCore.QSize(40, 40))
        self.save_parameters.setObjectName("save_parameters")
        self.gridLayout_18.addWidget(self.save_parameters, 2, 0, 1, 1)
        self.close = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close.setFont(font)
        self.close.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icon/close_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon6)
        self.close.setIconSize(QtCore.QSize(40, 40))
        self.close.setObjectName("close")
        self.gridLayout_18.addWidget(self.close, 2, 1, 1, 1)
        self.verticalLayout_15.addLayout(self.gridLayout_18)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_29 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_29.setFont(font)
        self.groupBox_29.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_29.setObjectName("groupBox_29")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_29)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.thresh_option = QtWidgets.QComboBox(self.groupBox_29)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thresh_option.setFont(font)
        self.thresh_option.setObjectName("thresh_option")
        self.thresh_option.addItem("")
        self.thresh_option.addItem("")
        self.horizontalLayout_4.addWidget(self.thresh_option)
        self.label = QtWidgets.QLabel(self.groupBox_29)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.tresh_value = QtWidgets.QLineEdit(self.groupBox_29)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tresh_value.setFont(font)
        self.tresh_value.setAlignment(QtCore.Qt.AlignCenter)
        self.tresh_value.setObjectName("tresh_value")
        self.horizontalLayout_4.addWidget(self.tresh_value)
        self.gridLayout_16.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_29)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.n_ind = QtWidgets.QLineEdit(self.groupBox_29)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_ind.setFont(font)
        self.n_ind.setAlignment(QtCore.Qt.AlignCenter)
        self.n_ind.setObjectName("n_ind")
        self.horizontalLayout_5.addWidget(self.n_ind)
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout_16.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_13.addWidget(self.groupBox_29)
        self.groupBox_17 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_17.setObjectName("groupBox_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_17)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Framenumber_6 = QtWidgets.QLabel(self.groupBox_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_6.setFont(font)
        self.Framenumber_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_6.setObjectName("Framenumber_6")
        self.horizontalLayout_6.addWidget(self.Framenumber_6)
        self.combo_roi = QtWidgets.QComboBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.combo_roi.setFont(font)
        self.combo_roi.setObjectName("combo_roi")
        self.combo_roi.addItem("")
        self.combo_roi.addItem("")
        self.horizontalLayout_6.addWidget(self.combo_roi)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Framenumber_7 = QtWidgets.QLabel(self.groupBox_17)
        self.Framenumber_7.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_7.setFont(font)
        self.Framenumber_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_7.setObjectName("Framenumber_7")
        self.horizontalLayout_7.addWidget(self.Framenumber_7)
        self.roi_shape_crop = QtWidgets.QComboBox(self.groupBox_17)
        self.roi_shape_crop.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roi_shape_crop.setFont(font)
        self.roi_shape_crop.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.roi_shape_crop.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.roi_shape_crop.setCurrentText("")
        self.roi_shape_crop.setObjectName("roi_shape_crop")
        self.roi_shape_crop.addItem("")
        self.roi_shape_crop.addItem("")
        self.horizontalLayout_7.addWidget(self.roi_shape_crop)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.calc_dist = QtWidgets.QPushButton(self.groupBox_17)
        self.calc_dist.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_dist.setFont(font)
        self.calc_dist.setObjectName("calc_dist")
        self.horizontalLayout_8.addWidget(self.calc_dist)
        self.distance_crop = QtWidgets.QLineEdit(self.groupBox_17)
        self.distance_crop.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_crop.setFont(font)
        self.distance_crop.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_crop.setObjectName("distance_crop")
        self.horizontalLayout_8.addWidget(self.distance_crop)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.label2 = QtWidgets.QLabel(self.groupBox_17)
        self.label2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2.setFont(font)
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setScaledContents(True)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.verticalLayout_11.addWidget(self.label2)
        self.verticalLayout_13.addWidget(self.groupBox_17)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.groupBox_18 = QtWidgets.QGroupBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Framenumber_10 = QtWidgets.QLabel(self.groupBox_18)
        self.Framenumber_10.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_10.setFont(font)
        self.Framenumber_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_10.setText("")
        self.Framenumber_10.setPixmap(QtGui.QPixmap("images/icon/select_blue.png"))
        self.Framenumber_10.setScaledContents(True)
        self.Framenumber_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_10.setObjectName("Framenumber_10")
        self.horizontalLayout_9.addWidget(self.Framenumber_10)
        self.deter_center = QtWidgets.QPushButton(self.groupBox_18)
        self.deter_center.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.deter_center.setFont(font)
        self.deter_center.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(255, 100, 100), stop:0.395 rgb(255, 80, 80), stop:0.605 rgb(255, 50,50), stop:1 rgb(255, 0, 0));\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.deter_center.setObjectName("deter_center")
        self.horizontalLayout_9.addWidget(self.deter_center)
        self.gridLayout_17.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(self.groupBox_18)
        self.label1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setScaledContents(True)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.gridLayout_17.addWidget(self.label1, 1, 0, 1, 1)
        self.label3 = QtWidgets.QLabel(self.groupBox_18)
        self.label3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label3.setFont(font)
        self.label3.setTextFormat(QtCore.Qt.AutoText)
        self.label3.setScaledContents(True)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.gridLayout_17.addWidget(self.label3, 2, 0, 1, 1)
        self.verticalLayout_15.addWidget(self.groupBox_18)
        self.gridLayout_19.addLayout(self.verticalLayout_15, 0, 1, 1, 1)
        ethoflow.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.check_save_data = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_save_data.setFont(font)
        self.check_save_data.setChecked(False)
        self.check_save_data.setObjectName("check_save_data")
        self.gridLayout_20.addWidget(self.check_save_data, 0, 0, 1, 1)
        self.check_save_video = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_save_video.setFont(font)
        self.check_save_video.setChecked(False)
        self.check_save_video.setObjectName("check_save_video")
        self.gridLayout_20.addWidget(self.check_save_video, 1, 0, 1, 1)
        self.show_video_processing = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.show_video_processing.setFont(font)
        self.show_video_processing.setChecked(False)
        self.show_video_processing.setObjectName("show_video_processing")
        self.gridLayout_20.addWidget(self.show_video_processing, 2, 0, 1, 1)
        self.check_end_video = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_end_video.setFont(font)
        self.check_end_video.setChecked(False)
        self.check_end_video.setObjectName("check_end_video")
        self.gridLayout_20.addWidget(self.check_end_video, 3, 0, 1, 1)
        self.check_regions = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_regions.setFont(font)
        self.check_regions.setChecked(False)
        self.check_regions.setObjectName("check_regions")
        self.gridLayout_20.addWidget(self.check_regions, 4, 0, 1, 1)
        self.check_regions_ind = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_regions_ind.setFont(font)
        self.check_regions_ind.setChecked(False)
        self.check_regions_ind.setObjectName("check_regions_ind")
        self.gridLayout_20.addWidget(self.check_regions_ind, 5, 0, 1, 1)
        self.Framenumber_8 = QtWidgets.QLabel(self.groupBox_2)
        self.Framenumber_8.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_8.setFont(font)
        self.Framenumber_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_8.setText("")
        self.Framenumber_8.setPixmap(QtGui.QPixmap("images/icon/id.png"))
        self.Framenumber_8.setScaledContents(True)
        self.Framenumber_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_8.setObjectName("Framenumber_8")
        self.gridLayout_20.addWidget(self.Framenumber_8, 6, 0, 1, 1)
        self.combo_id = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_id.setFont(font)
        self.combo_id.setObjectName("combo_id")
        self.combo_id.addItem("")
        self.combo_id.addItem("")
        self.gridLayout_20.addWidget(self.combo_id, 7, 0, 1, 1)
        self.Framenumber_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_9.setFont(font)
        self.Framenumber_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_9.setObjectName("Framenumber_9")
        self.gridLayout_20.addWidget(self.Framenumber_9, 8, 0, 1, 1)
        self.video_time_in_frame = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.video_time_in_frame.setFont(font)
        self.video_time_in_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.video_time_in_frame.setObjectName("video_time_in_frame")
        self.gridLayout_20.addWidget(self.video_time_in_frame, 9, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.groupBox_2)
        self.groupBox_23 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_23.setFont(font)
        self.groupBox_23.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_23)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Framenumber_21 = QtWidgets.QLabel(self.groupBox_23)
        self.Framenumber_21.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_21.setFont(font)
        self.Framenumber_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_21.setText("")
        self.Framenumber_21.setPixmap(QtGui.QPixmap("images/icon/select_blue.png"))
        self.Framenumber_21.setScaledContents(True)
        self.Framenumber_21.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_21.setObjectName("Framenumber_21")
        self.horizontalLayout_10.addWidget(self.Framenumber_21)
        self.select_regions = QtWidgets.QPushButton(self.groupBox_23)
        self.select_regions.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_regions.setFont(font)
        self.select_regions.setObjectName("select_regions")
        self.horizontalLayout_10.addWidget(self.select_regions)
        self.gridLayout_21.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.Framenumber_17 = QtWidgets.QLabel(self.groupBox_23)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_17.setFont(font)
        self.Framenumber_17.setAcceptDrops(False)
        self.Framenumber_17.setScaledContents(True)
        self.Framenumber_17.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_17.setWordWrap(True)
        self.Framenumber_17.setObjectName("Framenumber_17")
        self.gridLayout_21.addWidget(self.Framenumber_17, 1, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.groupBox_23)
        self.gridLayout_22.addLayout(self.verticalLayout_16, 0, 0, 1, 1)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.groupBox_28 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_28.setFont(font)
        self.groupBox_28.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_28.setObjectName("groupBox_28")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.groupBox_28)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Framenumber_22 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_22.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_22.setFont(font)
        self.Framenumber_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_22.setText("")
        self.Framenumber_22.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_22.setScaledContents(True)
        self.Framenumber_22.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_22.setObjectName("Framenumber_22")
        self.horizontalLayout_11.addWidget(self.Framenumber_22)
        self.Framenumber_25 = QtWidgets.QLabel(self.groupBox_28)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_25.setFont(font)
        self.Framenumber_25.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_25.setWordWrap(True)
        self.Framenumber_25.setObjectName("Framenumber_25")
        self.horizontalLayout_11.addWidget(self.Framenumber_25)
        self.verticalLayout_18.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Framenumber_29 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_29.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_29.setFont(font)
        self.Framenumber_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_29.setText("")
        self.Framenumber_29.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_29.setScaledContents(True)
        self.Framenumber_29.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_29.setObjectName("Framenumber_29")
        self.horizontalLayout_12.addWidget(self.Framenumber_29)
        self.Framenumber_26 = QtWidgets.QLabel(self.groupBox_28)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_26.setFont(font)
        self.Framenumber_26.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_26.setWordWrap(True)
        self.Framenumber_26.setObjectName("Framenumber_26")
        self.horizontalLayout_12.addWidget(self.Framenumber_26)
        self.verticalLayout_18.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Framenumber_30 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_30.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_30.setFont(font)
        self.Framenumber_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_30.setText("")
        self.Framenumber_30.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_30.setScaledContents(True)
        self.Framenumber_30.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_30.setObjectName("Framenumber_30")
        self.horizontalLayout_13.addWidget(self.Framenumber_30)
        self.Framenumber_27 = QtWidgets.QLabel(self.groupBox_28)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_27.setFont(font)
        self.Framenumber_27.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_27.setWordWrap(True)
        self.Framenumber_27.setObjectName("Framenumber_27")
        self.horizontalLayout_13.addWidget(self.Framenumber_27)
        self.verticalLayout_18.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Framenumber_31 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_31.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_31.setFont(font)
        self.Framenumber_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_31.setText("")
        self.Framenumber_31.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_31.setScaledContents(True)
        self.Framenumber_31.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_31.setObjectName("Framenumber_31")
        self.horizontalLayout_14.addWidget(self.Framenumber_31)
        self.Framenumber_28 = QtWidgets.QLabel(self.groupBox_28)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_28.setFont(font)
        self.Framenumber_28.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_28.setWordWrap(True)
        self.Framenumber_28.setObjectName("Framenumber_28")
        self.horizontalLayout_14.addWidget(self.Framenumber_28)
        self.verticalLayout_18.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem2 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.start_img = QtWidgets.QLineEdit(self.groupBox_28)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_img.setFont(font)
        self.start_img.setAlignment(QtCore.Qt.AlignCenter)
        self.start_img.setObjectName("start_img")
        self.horizontalLayout_15.addWidget(self.start_img)
        self.make_imgs_mask = QtWidgets.QPushButton(self.groupBox_28)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.make_imgs_mask.setFont(font)
        self.make_imgs_mask.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../../home/rodrigo/.designer/backup/images/icon/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.make_imgs_mask.setIcon(icon7)
        self.make_imgs_mask.setIconSize(QtCore.QSize(50, 50))
        self.make_imgs_mask.setObjectName("make_imgs_mask")
        self.horizontalLayout_15.addWidget(self.make_imgs_mask)
        self.Framenumber_32 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_32.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_32.setFont(font)
        self.Framenumber_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_32.setText("")
        self.Framenumber_32.setPixmap(QtGui.QPixmap("images/icon/make_data.png"))
        self.Framenumber_32.setScaledContents(True)
        self.Framenumber_32.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_32.setObjectName("Framenumber_32")
        self.horizontalLayout_15.addWidget(self.Framenumber_32)
        spacerItem3 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_18.addLayout(self.horizontalLayout_15)
        self.verticalLayout_26.addWidget(self.groupBox_28)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem4)
        self.run_video_simple_ground = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_video_simple_ground.sizePolicy().hasHeightForWidth())
        self.run_video_simple_ground.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.run_video_simple_ground.setFont(font)
        self.run_video_simple_ground.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_video_simple_ground.setIcon(icon2)
        self.run_video_simple_ground.setIconSize(QtCore.QSize(50, 45))
        self.run_video_simple_ground.setObjectName("run_video_simple_ground")
        self.verticalLayout_17.addWidget(self.run_video_simple_ground)
        self.run_video_complex_ground = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_video_complex_ground.sizePolicy().hasHeightForWidth())
        self.run_video_complex_ground.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.run_video_complex_ground.setFont(font)
        self.run_video_complex_ground.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(52, 101, 164);")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/icon/run_complexv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_video_complex_ground.setIcon(icon8)
        self.run_video_complex_ground.setIconSize(QtCore.QSize(50, 45))
        self.run_video_complex_ground.setObjectName("run_video_complex_ground")
        self.verticalLayout_17.addWidget(self.run_video_complex_ground)
        self.stop_view_video_2 = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_view_video_2.sizePolicy().hasHeightForWidth())
        self.stop_view_video_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stop_view_video_2.setFont(font)
        self.stop_view_video_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stop_view_video_2.setIcon(icon4)
        self.stop_view_video_2.setIconSize(QtCore.QSize(40, 40))
        self.stop_view_video_2.setObjectName("stop_view_video_2")
        self.verticalLayout_17.addWidget(self.stop_view_video_2)
        self.close_2 = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_2.sizePolicy().hasHeightForWidth())
        self.close_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close_2.setFont(font)
        self.close_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.close_2.setIcon(icon6)
        self.close_2.setIconSize(QtCore.QSize(40, 40))
        self.close_2.setObjectName("close_2")
        self.verticalLayout_17.addWidget(self.close_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem5)
        self.horizontalLayout_19.addLayout(self.verticalLayout_17)
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_19.setObjectName("groupBox_19")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.groupBox_19)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.processing = QtWidgets.QLabel(self.groupBox_19)
        self.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.processing.setAlignment(QtCore.Qt.AlignCenter)
        self.processing.setObjectName("processing")
        self.verticalLayout_19.addWidget(self.processing)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem6 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem6)
        self.Framenumber_38 = QtWidgets.QLabel(self.groupBox_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_38.setFont(font)
        self.Framenumber_38.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_38.setObjectName("Framenumber_38")
        self.horizontalLayout_16.addWidget(self.Framenumber_38)
        self.processed_frame_number = QtWidgets.QLCDNumber(self.groupBox_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processed_frame_number.sizePolicy().hasHeightForWidth())
        self.processed_frame_number.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.processed_frame_number.setFont(font)
        self.processed_frame_number.setStyleSheet("color: rgb(0, 0, 255);")
        self.processed_frame_number.setObjectName("processed_frame_number")
        self.horizontalLayout_16.addWidget(self.processed_frame_number)
        spacerItem7 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem7)
        self.verticalLayout_19.addLayout(self.horizontalLayout_16)
        self.video_progressBar = QtWidgets.QProgressBar(self.groupBox_19)
        self.video_progressBar.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"")
        self.video_progressBar.setProperty("value", 0)
        self.video_progressBar.setObjectName("video_progressBar")
        self.verticalLayout_19.addWidget(self.video_progressBar)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem8 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)
        self.Framenumber_13 = QtWidgets.QLabel(self.groupBox_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_13.setFont(font)
        self.Framenumber_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_13.setObjectName("Framenumber_13")
        self.horizontalLayout_17.addWidget(self.Framenumber_13)
        self.display_spent_time = QtWidgets.QLabel(self.groupBox_19)
        self.display_spent_time.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.display_spent_time.setAlignment(QtCore.Qt.AlignCenter)
        self.display_spent_time.setObjectName("display_spent_time")
        self.horizontalLayout_17.addWidget(self.display_spent_time)
        spacerItem9 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem9)
        self.verticalLayout_19.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem10 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem10)
        self.Framenumber_18 = QtWidgets.QLabel(self.groupBox_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_18.setFont(font)
        self.Framenumber_18.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_18.setObjectName("Framenumber_18")
        self.horizontalLayout_18.addWidget(self.Framenumber_18)
        self.prop_detection = QtWidgets.QLabel(self.groupBox_19)
        self.prop_detection.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.prop_detection.setAlignment(QtCore.Qt.AlignCenter)
        self.prop_detection.setObjectName("prop_detection")
        self.horizontalLayout_18.addWidget(self.prop_detection)
        spacerItem11 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem11)
        self.verticalLayout_19.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19.addWidget(self.groupBox_19)
        self.verticalLayout_26.addLayout(self.horizontalLayout_19)
        self.gridLayout_22.addLayout(self.verticalLayout_26, 0, 1, 1, 1)
        ethoflow.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.groupBox_25 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_25.setFont(font)
        self.groupBox_25.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_25.setObjectName("groupBox_25")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.groupBox_25)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.groupBox_26 = QtWidgets.QGroupBox(self.groupBox_25)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_26.setFont(font)
        self.groupBox_26.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_26.setObjectName("groupBox_26")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.groupBox_26)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_16 = QtWidgets.QLabel(self.groupBox_26)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_29.addWidget(self.label_16)
        self.label_20 = QtWidgets.QLabel(self.groupBox_26)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_29.addWidget(self.label_20)
        self.verticalLayout_21.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.stimated_area = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_area.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_area.setObjectName("stimated_area")
        self.horizontalLayout_21.addWidget(self.stimated_area)
        self.stimated_sd_area = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_sd_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_sd_area.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_sd_area.setObjectName("stimated_sd_area")
        self.horizontalLayout_21.addWidget(self.stimated_sd_area)
        self.verticalLayout_21.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_15 = QtWidgets.QLabel(self.groupBox_26)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_30.addWidget(self.label_15)
        self.label_19 = QtWidgets.QLabel(self.groupBox_26)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_30.addWidget(self.label_19)
        self.verticalLayout_21.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.stimated_len = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_len.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_len.setObjectName("stimated_len")
        self.horizontalLayout_20.addWidget(self.stimated_len)
        self.stimated_sd_len = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_sd_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_sd_len.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_sd_len.setObjectName("stimated_sd_len")
        self.horizontalLayout_20.addWidget(self.stimated_sd_len)
        self.verticalLayout_21.addLayout(self.horizontalLayout_20)
        self.Framenumber_11 = QtWidgets.QLabel(self.groupBox_26)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_11.setFont(font)
        self.Framenumber_11.setAcceptDrops(False)
        self.Framenumber_11.setMidLineWidth(0)
        self.Framenumber_11.setScaledContents(False)
        self.Framenumber_11.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_11.setWordWrap(True)
        self.Framenumber_11.setObjectName("Framenumber_11")
        self.verticalLayout_21.addWidget(self.Framenumber_11)
        self.verticalLayout_22.addWidget(self.groupBox_26)
        self.groupBox_27 = QtWidgets.QGroupBox(self.groupBox_25)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_27.setFont(font)
        self.groupBox_27.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_27.setObjectName("groupBox_27")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_27)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_17 = QtWidgets.QLabel(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_26.addWidget(self.label_17)
        self.label_21 = QtWidgets.QLabel(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_26.addWidget(self.label_21)
        self.verticalLayout_20.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.body_prop = QtWidgets.QLabel(self.groupBox_27)
        self.body_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.body_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.body_prop.setObjectName("body_prop")
        self.horizontalLayout_25.addWidget(self.body_prop)
        self.sd_body_prop = QtWidgets.QLabel(self.groupBox_27)
        self.sd_body_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.sd_body_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.sd_body_prop.setObjectName("sd_body_prop")
        self.horizontalLayout_25.addWidget(self.sd_body_prop)
        self.verticalLayout_20.addLayout(self.horizontalLayout_25)
        self.Framenumber_20 = QtWidgets.QLabel(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_20.setFont(font)
        self.Framenumber_20.setAcceptDrops(False)
        self.Framenumber_20.setMidLineWidth(0)
        self.Framenumber_20.setScaledContents(False)
        self.Framenumber_20.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_20.setWordWrap(True)
        self.Framenumber_20.setObjectName("Framenumber_20")
        self.verticalLayout_20.addWidget(self.Framenumber_20)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem12 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem12)
        self.run_estimates = QtWidgets.QPushButton(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.run_estimates.setFont(font)
        self.run_estimates.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_estimates.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_estimates.setIcon(icon2)
        self.run_estimates.setIconSize(QtCore.QSize(40, 40))
        self.run_estimates.setObjectName("run_estimates")
        self.horizontalLayout_27.addWidget(self.run_estimates)
        spacerItem13 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem13)
        self.verticalLayout_20.addLayout(self.horizontalLayout_27)
        self.Framenumber_14 = QtWidgets.QLabel(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_14.setFont(font)
        self.Framenumber_14.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_14.setObjectName("Framenumber_14")
        self.verticalLayout_20.addWidget(self.Framenumber_14)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem14 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem14)
        self.n_amostrad_frame = QtWidgets.QLineEdit(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_amostrad_frame.setFont(font)
        self.n_amostrad_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.n_amostrad_frame.setObjectName("n_amostrad_frame")
        self.horizontalLayout_28.addWidget(self.n_amostrad_frame)
        spacerItem15 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem15)
        self.verticalLayout_20.addLayout(self.horizontalLayout_28)
        self.Framenumber_19 = QtWidgets.QLabel(self.groupBox_27)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_19.setFont(font)
        self.Framenumber_19.setAcceptDrops(False)
        self.Framenumber_19.setStyleSheet("color: rgb(239, 41, 41);")
        self.Framenumber_19.setMidLineWidth(0)
        self.Framenumber_19.setScaledContents(False)
        self.Framenumber_19.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_19.setWordWrap(True)
        self.Framenumber_19.setObjectName("Framenumber_19")
        self.verticalLayout_20.addWidget(self.Framenumber_19)
        self.verticalLayout_22.addWidget(self.groupBox_27)
        self.gridLayout_25.addWidget(self.groupBox_25, 0, 0, 1, 1)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.Framenumber_15 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_15.setFont(font)
        self.Framenumber_15.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_15.setObjectName("Framenumber_15")
        self.horizontalLayout_22.addWidget(self.Framenumber_15)
        self.n_behaviour_1 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_behaviour_1.setFont(font)
        self.n_behaviour_1.setAlignment(QtCore.Qt.AlignCenter)
        self.n_behaviour_1.setObjectName("n_behaviour_1")
        self.horizontalLayout_22.addWidget(self.n_behaviour_1)
        self.gridLayout_24.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.Framenumber_23 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_23.setFont(font)
        self.Framenumber_23.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_23.setObjectName("Framenumber_23")
        self.horizontalLayout_23.addWidget(self.Framenumber_23)
        self.n_behaviour_2 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_behaviour_2.setFont(font)
        self.n_behaviour_2.setAlignment(QtCore.Qt.AlignCenter)
        self.n_behaviour_2.setObjectName("n_behaviour_2")
        self.horizontalLayout_23.addWidget(self.n_behaviour_2)
        self.gridLayout_24.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem16 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem16)
        self.make_imgs_behavior = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.make_imgs_behavior.setFont(font)
        self.make_imgs_behavior.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.make_imgs_behavior.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.make_imgs_behavior.setIcon(icon2)
        self.make_imgs_behavior.setIconSize(QtCore.QSize(40, 40))
        self.make_imgs_behavior.setObjectName("make_imgs_behavior")
        self.horizontalLayout_24.addWidget(self.make_imgs_behavior)
        spacerItem17 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem17)
        self.gridLayout_24.addLayout(self.horizontalLayout_24, 2, 0, 1, 1)
        self.verticalLayout_25.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        spacerItem18 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem18)
        self.run_behaviour = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.run_behaviour.setFont(font)
        self.run_behaviour.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_behaviour.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_behaviour.setIcon(icon2)
        self.run_behaviour.setIconSize(QtCore.QSize(40, 40))
        self.run_behaviour.setObjectName("run_behaviour")
        self.horizontalLayout_32.addWidget(self.run_behaviour)
        spacerItem19 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem19)
        self.verticalLayout_23.addLayout(self.horizontalLayout_32)
        self.Framenumber_24 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_24.setFont(font)
        self.Framenumber_24.setAcceptDrops(False)
        self.Framenumber_24.setAutoFillBackground(False)
        self.Framenumber_24.setMidLineWidth(0)
        self.Framenumber_24.setScaledContents(False)
        self.Framenumber_24.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_24.setWordWrap(True)
        self.Framenumber_24.setObjectName("Framenumber_24")
        self.verticalLayout_23.addWidget(self.Framenumber_24)
        self.percent_behviour_ocorred = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.percent_behviour_ocorred.setFont(font)
        self.percent_behviour_ocorred.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.percent_behviour_ocorred.setAlignment(QtCore.Qt.AlignCenter)
        self.percent_behviour_ocorred.setObjectName("percent_behviour_ocorred")
        self.verticalLayout_23.addWidget(self.percent_behviour_ocorred)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        spacerItem20 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem20)
        self.upload_model = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upload_model.setFont(font)
        self.upload_model.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/icon/upload_model.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_model.setIcon(icon9)
        self.upload_model.setIconSize(QtCore.QSize(50, 50))
        self.upload_model.setObjectName("upload_model")
        self.horizontalLayout_31.addWidget(self.upload_model)
        spacerItem21 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem21)
        self.verticalLayout_23.addLayout(self.horizontalLayout_31)
        self.verticalLayout_25.addWidget(self.groupBox_4)
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_24.setFont(font)
        self.groupBox_24.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_24.setObjectName("groupBox_24")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.groupBox_24)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.stimate_progressBar = QtWidgets.QProgressBar(self.groupBox_24)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stimate_progressBar.setFont(font)
        self.stimate_progressBar.setProperty("value", 0)
        self.stimate_progressBar.setObjectName("stimate_progressBar")
        self.verticalLayout_24.addWidget(self.stimate_progressBar)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.Framenumber_33 = QtWidgets.QLabel(self.groupBox_24)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_33.setFont(font)
        self.Framenumber_33.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_33.setObjectName("Framenumber_33")
        self.horizontalLayout_33.addWidget(self.Framenumber_33)
        self.display_spent_time_meansure = QtWidgets.QLabel(self.groupBox_24)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.display_spent_time_meansure.setFont(font)
        self.display_spent_time_meansure.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.display_spent_time_meansure.setAlignment(QtCore.Qt.AlignCenter)
        self.display_spent_time_meansure.setObjectName("display_spent_time_meansure")
        self.horizontalLayout_33.addWidget(self.display_spent_time_meansure)
        self.verticalLayout_24.addLayout(self.horizontalLayout_33)
        self.verticalLayout_25.addWidget(self.groupBox_24)
        self.gridLayout_25.addLayout(self.verticalLayout_25, 0, 1, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)
        ethoflow.addTab(self.tab, "")

        self.retranslateUi(ethoflow)
        ethoflow.setCurrentIndex(0)
        self.thresh_option.setCurrentIndex(0)
        self.combo_roi.setCurrentIndex(-1)
        self.roi_shape_crop.setCurrentIndex(-1)
        self.combo_id.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ethoflow)

    def retranslateUi(self, ethoflow):
        _translate = QtCore.QCoreApplication.translate
        ethoflow.setWindowTitle(_translate("ethoflow", "ETHOFLOW"))
        self.groupBox_5.setTitle(_translate("ethoflow", "Detection parameters"))
        self.groupBox_6.setTitle(_translate("ethoflow", "Area"))
        self.label_10.setText(_translate("ethoflow", "Median"))
        self.output_median_area.setText(_translate("ethoflow", "------------"))
        self.label_9.setText(_translate("ethoflow", "SD"))
        self.output_sd_area.setText(_translate("ethoflow", "------------"))
        self.label_7.setText(_translate("ethoflow", "Max"))
        self.max_area.setText(_translate("ethoflow", "100000"))
        self.label_3.setText(_translate("ethoflow", "Min"))
        self.min_area.setText(_translate("ethoflow", "0"))
        self.label_2.setText(_translate("ethoflow", "Max"))
        self.output_max_area.setText(_translate("ethoflow", "------------"))
        self.label_8.setText(_translate("ethoflow", "Min"))
        self.output_min_area.setText(_translate("ethoflow", "------------"))
        self.label_25.setText(_translate("ethoflow", "Input"))
        self.label_26.setText(_translate("ethoflow", "Output"))
        self.groupBox_9.setTitle(_translate("ethoflow", "Length"))
        self.label_11.setText(_translate("ethoflow", "Max"))
        self.output_max_len.setText(_translate("ethoflow", "------------"))
        self.label_12.setText(_translate("ethoflow", "Min"))
        self.output_min_len.setText(_translate("ethoflow", "------------"))
        self.label_4.setText(_translate("ethoflow", "Max"))
        self.max_len.setText(_translate("ethoflow", "100000"))
        self.label_5.setText(_translate("ethoflow", "Min"))
        self.min_len.setText(_translate("ethoflow", "0"))
        self.label_14.setText(_translate("ethoflow", "Median"))
        self.output_median_len.setText(_translate("ethoflow", "------------"))
        self.label_13.setText(_translate("ethoflow", "SD"))
        self.output_sd_len.setText(_translate("ethoflow", "------------"))
        self.label_34.setText(_translate("ethoflow", "Output"))
        self.label_33.setText(_translate("ethoflow", "Input"))
        self.groupBox_12.setTitle(_translate("ethoflow", "Proportion"))
        self.label_30.setText(_translate("ethoflow", "Max"))
        self.output_max_prop.setText(_translate("ethoflow", "------------"))
        self.label_29.setText(_translate("ethoflow", "Min"))
        self.output_min_prop.setText(_translate("ethoflow", "------------"))
        self.label_28.setText(_translate("ethoflow", "Max"))
        self.max_prop.setText(_translate("ethoflow", "100000"))
        self.label_27.setText(_translate("ethoflow", "Min"))
        self.min_prop.setText(_translate("ethoflow", "0"))
        self.label_31.setText(_translate("ethoflow", "Median"))
        self.output_median_prop.setText(_translate("ethoflow", "------------"))
        self.label_32.setText(_translate("ethoflow", "SD"))
        self.output_sd_prop.setText(_translate("ethoflow", "------------"))
        self.label_36.setText(_translate("ethoflow", "Input"))
        self.label_35.setText(_translate("ethoflow", "Output"))
        self.groupBox_15.setTitle(_translate("ethoflow", "Video"))
        self.label_38.setText(_translate("ethoflow", "Resolution (%)"))
        self.set_frame_resolution.setText(_translate("ethoflow", "100"))
        self.Framenumber.setText(_translate("ethoflow", "Frame"))
        self.frame_number.setText(_translate("ethoflow", "0"))
        self.Framenumber_4.setText(_translate("ethoflow", "Y"))
        self.Framenumber_5.setText(_translate("ethoflow", "X"))
        self.shape_1.setText(_translate("ethoflow", "------------"))
        self.shape_0.setText(_translate("ethoflow", "------------"))
        self.Framenumber_3.setText(_translate("ethoflow", "of"))
        self.groupBox_16.setTitle(_translate("ethoflow", "Analysis parameters"))
        self.groupBox_20.setTitle(_translate("ethoflow", "Scale"))
        self.label2_9.setText(_translate("ethoflow", "Attention:"))
        self.label2_8.setText(_translate("ethoflow", "after adjusting the resolution"))
        self.calc_dist_scale.setText(_translate("ethoflow", "calculate "))
        self.distance_scale.setText(_translate("ethoflow", "1"))
        self.label2_3.setText(_translate("ethoflow", "Put real scale distance (e.g. cm)"))
        self.distance_scale_know.setText(_translate("ethoflow", "1"))
        self.label2_2.setText(_translate("ethoflow", "Select 2 points for know distance"))
        self.groupBox_21.setTitle(_translate("ethoflow", "Interaction"))
        self.label2_10.setText(_translate("ethoflow", "Put the interaction threshold"))
        self.interaction_threshold.setText(_translate("ethoflow", "0.8"))
        self.label2_4.setText(_translate("ethoflow", "Interaction will be considered when individuals approach a shorter distance. Put real distance (e.g. cm)"))
        self.label2_12.setText(_translate("ethoflow", "Observation:"))
        self.groupBox_22.setTitle(_translate("ethoflow", "Movement"))
        self.label2_11.setText(_translate("ethoflow", "Put the movement threshold"))
        self.label2_6.setText(_translate("ethoflow", "Low"))
        self.thersh_min_mov.setText(_translate("ethoflow", "0.02"))
        self.label2_7.setText(_translate("ethoflow", "High"))
        self.thersh_max_mov.setText(_translate("ethoflow", "0.3"))
        self.label2_13.setText(_translate("ethoflow", "Observation:"))
        self.label2_14.setText(_translate("ethoflow", "Put real distance (e.g. cm)"))
        self.upload_video.setText(_translate("ethoflow", "Upload video"))
        self.run_video.setText(_translate("ethoflow", "Run "))
        self.read_parameters.setText(_translate("ethoflow", "Read parameters"))
        self.stop_view_video.setText(_translate("ethoflow", "Stop"))
        self.save_parameters.setText(_translate("ethoflow", "Save parameters"))
        self.close.setText(_translate("ethoflow", "Close"))
        self.groupBox_29.setTitle(_translate("ethoflow", "Threshold"))
        self.thresh_option.setItemText(0, _translate("ethoflow", "Manual"))
        self.thresh_option.setItemText(1, _translate("ethoflow", "Automatic"))
        self.label.setText(_translate("ethoflow", "Value"))
        self.tresh_value.setText(_translate("ethoflow", "95"))
        self.label_6.setText(_translate("ethoflow", "<html><head/><body><p>N individuos</p></body></html>"))
        self.n_ind.setText(_translate("ethoflow", "1"))
        self.groupBox_17.setTitle(_translate("ethoflow", "ROI "))
        self.Framenumber_6.setText(_translate("ethoflow", "Select"))
        self.combo_roi.setItemText(0, _translate("ethoflow", "No"))
        self.combo_roi.setItemText(1, _translate("ethoflow", "Yes"))
        self.Framenumber_7.setText(_translate("ethoflow", "Shape"))
        self.roi_shape_crop.setItemText(0, _translate("ethoflow", "Circle"))
        self.roi_shape_crop.setItemText(1, _translate("ethoflow", "Rectangle"))
        self.calc_dist.setText(_translate("ethoflow", "Calculate distance"))
        self.distance_crop.setText(_translate("ethoflow", "0"))
        self.label2.setText(_translate("ethoflow", "-> select center and edge (2 points)"))
        self.groupBox_18.setTitle(_translate("ethoflow", "Choose arena"))
        self.deter_center.setText(_translate("ethoflow", "Select"))
        self.label1.setText(_translate("ethoflow", "Select the center of the arena (1 point)"))
        self.label3.setText(_translate("ethoflow", "-> select upper left and lower right (2 points)"))
        ethoflow.setTabText(ethoflow.indexOf(self.widget), _translate("ethoflow", "SETTING"))
        self.groupBox_2.setTitle(_translate("ethoflow", "Outputs"))
        self.check_save_data.setText(_translate("ethoflow", "Save data"))
        self.check_save_video.setText(_translate("ethoflow", "Save video"))
        self.show_video_processing.setText(_translate("ethoflow", "Show video in processing"))
        self.check_end_video.setText(_translate("ethoflow", "Notify when finished"))
        self.check_regions.setText(_translate("ethoflow", "Regions"))
        self.check_regions_ind.setText(_translate("ethoflow", "Regions by individuals"))
        self.combo_id.setItemText(0, _translate("ethoflow", "No"))
        self.combo_id.setItemText(1, _translate("ethoflow", "Yes"))
        self.Framenumber_9.setText(_translate("ethoflow", "Video time in frame"))
        self.video_time_in_frame.setText(_translate("ethoflow", "100"))
        self.groupBox_23.setTitle(_translate("ethoflow", "Regions"))
        self.select_regions.setText(_translate("ethoflow", "Select regions"))
        self.Framenumber_17.setText(_translate("ethoflow", "Presse Enter, then: - Press \"q\" to quit selecting boxes  - Press any other key to select next region"))
        self.groupBox_28.setTitle(_translate("ethoflow", "Make data for mask R-CNN"))
        self.Framenumber_25.setText(_translate("ethoflow", "The images will be save in path: \"\'make_mask_rcnn_data/mask_imgs\""))
        self.Framenumber_26.setText(_translate("ethoflow", "In the \"video time in frame\" place the amount of images that will be generated. This should be <= the number of backgrounds"))
        self.Framenumber_27.setText(_translate("ethoflow", "Make images separate for training and validation"))
        self.Framenumber_28.setText(_translate("ethoflow", "Entry start image value. It is to when save different .json file"))
        self.start_img.setText(_translate("ethoflow", "1"))
        self.make_imgs_mask.setText(_translate("ethoflow", "Make data"))
        self.run_video_simple_ground.setText(_translate("ethoflow", "Run simple background"))
        self.run_video_complex_ground.setText(_translate("ethoflow", "Run complex background"))
        self.stop_view_video_2.setText(_translate("ethoflow", "Stop"))
        self.close_2.setText(_translate("ethoflow", "Close"))
        self.groupBox_19.setTitle(_translate("ethoflow", "Processing summary"))
        self.processing.setText(_translate("ethoflow", "------------"))
        self.Framenumber_38.setText(_translate("ethoflow", "Frame number ="))
        self.Framenumber_13.setText(_translate("ethoflow", "Time spent ="))
        self.display_spent_time.setText(_translate("ethoflow", "------------"))
        self.Framenumber_18.setText(_translate("ethoflow", "True detection rate ="))
        self.prop_detection.setText(_translate("ethoflow", "------------"))
        ethoflow.setTabText(ethoflow.indexOf(self.tab_2), _translate("ethoflow", "ANALYSES"))
        self.groupBox_25.setTitle(_translate("ethoflow", "Measurements"))
        self.groupBox_26.setTitle(_translate("ethoflow", "Area and length"))
        self.label_16.setText(_translate("ethoflow", "Median area"))
        self.label_20.setText(_translate("ethoflow", "SD  area"))
        self.stimated_area.setText(_translate("ethoflow", "------------"))
        self.stimated_sd_area.setText(_translate("ethoflow", "------------"))
        self.label_15.setText(_translate("ethoflow", "Median length"))
        self.label_19.setText(_translate("ethoflow", "SD length"))
        self.stimated_len.setText(_translate("ethoflow", "------------"))
        self.stimated_sd_len.setText(_translate("ethoflow", "------------"))
        self.Framenumber_11.setText(_translate("ethoflow", "Area and length estimates based on random frames where there is no cross."))
        self.groupBox_27.setTitle(_translate("ethoflow", "Proportion"))
        self.label_17.setText(_translate("ethoflow", "Median"))
        self.label_21.setText(_translate("ethoflow", "SD"))
        self.body_prop.setText(_translate("ethoflow", "------------"))
        self.sd_body_prop.setText(_translate("ethoflow", "------------"))
        self.Framenumber_20.setText(_translate("ethoflow", "Area / length ratio in any frame (with cross or not)"))
        self.run_estimates.setText(_translate("ethoflow", "Run "))
        self.Framenumber_14.setText(_translate("ethoflow", "Video time in frame"))
        self.n_amostrad_frame.setText(_translate("ethoflow", "100"))
        self.Framenumber_19.setText(_translate("ethoflow", "Unit = pixels"))
        self.groupBox_3.setTitle(_translate("ethoflow", "Make data for train"))
        self.Framenumber_15.setText(_translate("ethoflow", "N images for complex behavior"))
        self.n_behaviour_1.setText(_translate("ethoflow", "10"))
        self.Framenumber_23.setText(_translate("ethoflow", "N images for non behavior"))
        self.n_behaviour_2.setText(_translate("ethoflow", "10"))
        self.make_imgs_behavior.setText(_translate("ethoflow", "Run "))
        self.groupBox_4.setTitle(_translate("ethoflow", "AI behaviour analyses"))
        self.run_behaviour.setText(_translate("ethoflow", "Run "))
        self.Framenumber_24.setText(_translate("ethoflow", "Behavior occurrence (%)"))
        self.percent_behviour_ocorred.setText(_translate("ethoflow", "------------"))
        self.upload_model.setText(_translate("ethoflow", "Upload CNN"))
        self.groupBox_24.setTitle(_translate("ethoflow", "Processing summary"))
        self.Framenumber_33.setText(_translate("ethoflow", "Time spent ="))
        self.display_spent_time_meansure.setText(_translate("ethoflow", "------------"))
        ethoflow.setTabText(ethoflow.indexOf(self.tab), _translate("ethoflow", "DEEP ANALYSES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ethoflow = QtWidgets.QTabWidget()
    ui = Ui_ethoflow()
    ui.setupUi(ethoflow)
    ethoflow.show()
    sys.exit(app.exec_())
