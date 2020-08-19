# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ethoflow(object):
    def setupUi(self, ethoflow):
        ethoflow.setObjectName("ethoflow")
        ethoflow.setEnabled(True)
        ethoflow.resize(1493, 941)
        font = QtGui.QFont()
        font.setPointSize(14)
        ethoflow.setFont(font)
        ethoflow.setMouseTracking(False)
        ethoflow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
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
        ethoflow.setIconSize(QtCore.QSize(100, 100))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.close = QtWidgets.QPushButton(self.tab)
        self.close.setGeometry(QtCore.QRect(1380, 0, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close.setFont(font)
        self.close.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon/close_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon1)
        self.close.setIconSize(QtCore.QSize(40, 40))
        self.close.setObjectName("close")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 120, 861, 471))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_9.setGeometry(QtCore.QRect(420, 30, 421, 211))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_10.setGeometry(QtCore.QRect(30, 40, 121, 166))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.max_len = QtWidgets.QLineEdit(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_len.setFont(font)
        self.max_len.setAlignment(QtCore.Qt.AlignCenter)
        self.max_len.setObjectName("max_len")
        self.verticalLayout_2.addWidget(self.max_len)
        self.label_5 = QtWidgets.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.min_len = QtWidgets.QLineEdit(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_len.setFont(font)
        self.min_len.setAlignment(QtCore.Qt.AlignCenter)
        self.min_len.setObjectName("min_len")
        self.verticalLayout_2.addWidget(self.min_len)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_11.setGeometry(QtCore.QRect(170, 40, 221, 151))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_11)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 201, 103))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 1, 1, 1)
        self.output_max_len = QtWidgets.QLabel(self.layoutWidget)
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
        self.gridLayout_4.addWidget(self.output_max_len, 1, 0, 1, 1)
        self.output_median_len = QtWidgets.QLabel(self.layoutWidget)
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
        self.gridLayout_4.addWidget(self.output_median_len, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 2, 1, 1, 1)
        self.output_min_len = QtWidgets.QLabel(self.layoutWidget)
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
        self.gridLayout_4.addWidget(self.output_min_len, 3, 0, 1, 1)
        self.output_sd_len = QtWidgets.QLabel(self.layoutWidget)
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
        self.gridLayout_4.addWidget(self.output_sd_len, 3, 1, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 30, 401, 211))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 40, 111, 175))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.min_area = QtWidgets.QLineEdit(self.groupBox_7)
        self.min_area.setGeometry(QtCore.QRect(11, 116, 89, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_area.setFont(font)
        self.min_area.setAlignment(QtCore.Qt.AlignCenter)
        self.min_area.setObjectName("min_area")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 28, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.max_area = QtWidgets.QLineEdit(self.groupBox_7)
        self.max_area.setGeometry(QtCore.QRect(11, 56, 89, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_area.setFont(font)
        self.max_area.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.max_area.setAlignment(QtCore.Qt.AlignCenter)
        self.max_area.setObjectName("max_area")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 22, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(170, 40, 201, 151))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_8.setObjectName("groupBox_8")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 40, 201, 103))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)
        self.output_max_area = QtWidgets.QLabel(self.layoutWidget1)
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
        self.gridLayout_2.addWidget(self.output_max_area, 1, 0, 1, 1)
        self.output_median_area = QtWidgets.QLabel(self.layoutWidget1)
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
        self.gridLayout_2.addWidget(self.output_median_area, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.output_min_area = QtWidgets.QLabel(self.layoutWidget1)
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
        self.gridLayout_2.addWidget(self.output_min_area, 3, 0, 1, 1)
        self.output_sd_area = QtWidgets.QLabel(self.layoutWidget1)
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
        self.gridLayout_2.addWidget(self.output_sd_area, 3, 1, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_15.setGeometry(QtCore.QRect(420, 240, 421, 211))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_15.setObjectName("groupBox_15")
        self.Resolution = QtWidgets.QGroupBox(self.groupBox_15)
        self.Resolution.setGeometry(QtCore.QRect(10, 40, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Resolution.setFont(font)
        self.Resolution.setAlignment(QtCore.Qt.AlignCenter)
        self.Resolution.setObjectName("Resolution")
        self.layoutWidget2 = QtWidgets.QWidget(self.Resolution)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 29, 91, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.set_frame_resolution = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_frame_resolution.setFont(font)
        self.set_frame_resolution.setInputMask("")
        self.set_frame_resolution.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.set_frame_resolution.setAlignment(QtCore.Qt.AlignCenter)
        self.set_frame_resolution.setReadOnly(False)
        self.set_frame_resolution.setObjectName("set_frame_resolution")
        self.horizontalLayout_2.addWidget(self.set_frame_resolution)
        self.Framenumber_24 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_24.setFont(font)
        self.Framenumber_24.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_24.setObjectName("Framenumber_24")
        self.horizontalLayout_2.addWidget(self.Framenumber_24)
        self.Framenumber_4 = QtWidgets.QLabel(self.Resolution)
        self.Framenumber_4.setGeometry(QtCore.QRect(110, 30, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_4.setFont(font)
        self.Framenumber_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_4.setObjectName("Framenumber_4")
        self.Framenumber_5 = QtWidgets.QLabel(self.Resolution)
        self.Framenumber_5.setGeometry(QtCore.QRect(190, 30, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_5.setFont(font)
        self.Framenumber_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_5.setObjectName("Framenumber_5")
        self.shape_1 = QtWidgets.QLabel(self.Resolution)
        self.shape_1.setGeometry(QtCore.QRect(100, 50, 51, 41))
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
        self.shape_0 = QtWidgets.QLabel(self.Resolution)
        self.shape_0.setGeometry(QtCore.QRect(180, 50, 51, 41))
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
        self.Framenumber = QtWidgets.QLabel(self.groupBox_15)
        self.Framenumber.setGeometry(QtCore.QRect(20, 140, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber.setFont(font)
        self.Framenumber.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber.setObjectName("Framenumber")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_15)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 160, 141, 31))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("color: rgb(0, 0, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.frame_number = QtWidgets.QLineEdit(self.groupBox_15)
        self.frame_number.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_number.setFont(font)
        self.frame_number.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_number.setObjectName("frame_number")
        self.Framenumber_2 = QtWidgets.QLabel(self.groupBox_15)
        self.Framenumber_2.setGeometry(QtCore.QRect(160, 140, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_2.setFont(font)
        self.Framenumber_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_2.setObjectName("Framenumber_2")
        self.Framenumber_3 = QtWidgets.QLabel(self.groupBox_15)
        self.Framenumber_3.setGeometry(QtCore.QRect(100, 160, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_3.setFont(font)
        self.Framenumber_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_3.setObjectName("Framenumber_3")
        self.n_ind = QtWidgets.QLineEdit(self.groupBox_15)
        self.n_ind.setGeometry(QtCore.QRect(310, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_ind.setFont(font)
        self.n_ind.setAlignment(QtCore.Qt.AlignCenter)
        self.n_ind.setObjectName("n_ind")
        self.label_6 = QtWidgets.QLabel(self.groupBox_15)
        self.label_6.setGeometry(QtCore.QRect(300, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 240, 401, 211))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_13.setGeometry(QtCore.QRect(30, 40, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_27 = QtWidgets.QLabel(self.groupBox_13)
        self.label_27.setGeometry(QtCore.QRect(50, 90, 22, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_13)
        self.label_28.setGeometry(QtCore.QRect(50, 30, 28, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.min_prop = QtWidgets.QLineEdit(self.groupBox_13)
        self.min_prop.setGeometry(QtCore.QRect(21, 116, 89, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_prop.setFont(font)
        self.min_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.min_prop.setObjectName("min_prop")
        self.max_prop = QtWidgets.QLineEdit(self.groupBox_13)
        self.max_prop.setGeometry(QtCore.QRect(21, 56, 89, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_prop.setFont(font)
        self.max_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.max_prop.setObjectName("max_prop")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_14.setGeometry(QtCore.QRect(170, 40, 201, 151))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_14.setObjectName("groupBox_14")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_14)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 40, 191, 103))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 0, 1, 1, 1)
        self.output_max_prop = QtWidgets.QLabel(self.layoutWidget3)
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
        self.gridLayout_5.addWidget(self.output_max_prop, 1, 0, 1, 1)
        self.output_median_prop = QtWidgets.QLabel(self.layoutWidget3)
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
        self.gridLayout_5.addWidget(self.output_median_prop, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 2, 1, 1, 1)
        self.output_min_prop = QtWidgets.QLabel(self.layoutWidget3)
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
        self.gridLayout_5.addWidget(self.output_min_prop, 3, 0, 1, 1)
        self.output_sd_prop = QtWidgets.QLabel(self.layoutWidget3)
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
        self.gridLayout_5.addWidget(self.output_sd_prop, 3, 1, 1, 1)
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_16.setGeometry(QtCore.QRect(20, 600, 861, 261))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_16.setObjectName("groupBox_16")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_20.setGeometry(QtCore.QRect(10, 30, 321, 221))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_20.setObjectName("groupBox_20")
        self.label2_2 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_2.setEnabled(True)
        self.label2_2.setGeometry(QtCore.QRect(60, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_2.setFont(font)
        self.label2_2.setAcceptDrops(False)
        self.label2_2.setTextFormat(QtCore.Qt.AutoText)
        self.label2_2.setScaledContents(True)
        self.label2_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_2.setWordWrap(True)
        self.label2_2.setObjectName("label2_2")
        self.calc_dist_scale = QtWidgets.QPushButton(self.groupBox_20)
        self.calc_dist_scale.setEnabled(True)
        self.calc_dist_scale.setGeometry(QtCore.QRect(50, 57, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_dist_scale.setFont(font)
        self.calc_dist_scale.setMouseTracking(False)
        self.calc_dist_scale.setObjectName("calc_dist_scale")
        self.label2_3 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_3.setEnabled(True)
        self.label2_3.setGeometry(QtCore.QRect(20, 110, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_3.setFont(font)
        self.label2_3.setTextFormat(QtCore.Qt.AutoText)
        self.label2_3.setScaledContents(False)
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setObjectName("label2_3")
        self.label2_9 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_9.setEnabled(True)
        self.label2_9.setGeometry(QtCore.QRect(10, 180, 71, 31))
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
        self.label2_8 = QtWidgets.QLabel(self.groupBox_20)
        self.label2_8.setEnabled(True)
        self.label2_8.setGeometry(QtCore.QRect(90, 174, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_8.setFont(font)
        self.label2_8.setAcceptDrops(False)
        self.label2_8.setTextFormat(QtCore.Qt.AutoText)
        self.label2_8.setScaledContents(False)
        self.label2_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_8.setWordWrap(True)
        self.label2_8.setObjectName("label2_8")
        self.distance_scale = QtWidgets.QLineEdit(self.groupBox_20)
        self.distance_scale.setGeometry(QtCore.QRect(180, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_scale.setFont(font)
        self.distance_scale.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_scale.setObjectName("distance_scale")
        self.distance_scale_know = QtWidgets.QLineEdit(self.groupBox_20)
        self.distance_scale_know.setGeometry(QtCore.QRect(120, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_scale_know.setFont(font)
        self.distance_scale_know.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_scale_know.setObjectName("distance_scale_know")
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_21.setGeometry(QtCore.QRect(340, 30, 261, 221))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_21.setObjectName("groupBox_21")
        self.label2_12 = QtWidgets.QLabel(self.groupBox_21)
        self.label2_12.setEnabled(True)
        self.label2_12.setGeometry(QtCore.QRect(80, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_12.setFont(font)
        self.label2_12.setAcceptDrops(False)
        self.label2_12.setStyleSheet("color: rgb(239, 41, 41);")
        self.label2_12.setTextFormat(QtCore.Qt.AutoText)
        self.label2_12.setScaledContents(True)
        self.label2_12.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_12.setWordWrap(True)
        self.label2_12.setObjectName("label2_12")
        self.label2_10 = QtWidgets.QLabel(self.groupBox_21)
        self.label2_10.setEnabled(True)
        self.label2_10.setGeometry(QtCore.QRect(30, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_10.setFont(font)
        self.label2_10.setAcceptDrops(False)
        self.label2_10.setAutoFillBackground(False)
        self.label2_10.setTextFormat(QtCore.Qt.AutoText)
        self.label2_10.setScaledContents(True)
        self.label2_10.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_10.setWordWrap(True)
        self.label2_10.setObjectName("label2_10")
        self.interaction_threshold = QtWidgets.QLineEdit(self.groupBox_21)
        self.interaction_threshold.setGeometry(QtCore.QRect(80, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.interaction_threshold.setFont(font)
        self.interaction_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.interaction_threshold.setObjectName("interaction_threshold")
        self.label2_4 = QtWidgets.QLabel(self.groupBox_21)
        self.label2_4.setEnabled(True)
        self.label2_4.setGeometry(QtCore.QRect(10, 130, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_4.setFont(font)
        self.label2_4.setAcceptDrops(False)
        self.label2_4.setAutoFillBackground(False)
        self.label2_4.setTextFormat(QtCore.Qt.AutoText)
        self.label2_4.setScaledContents(True)
        self.label2_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_4.setWordWrap(True)
        self.label2_4.setObjectName("label2_4")
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_22.setGeometry(QtCore.QRect(610, 30, 241, 231))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_22.setFont(font)
        self.groupBox_22.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_22.setObjectName("groupBox_22")
        self.label2_13 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_13.setEnabled(True)
        self.label2_13.setGeometry(QtCore.QRect(70, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_13.setFont(font)
        self.label2_13.setAcceptDrops(False)
        self.label2_13.setStyleSheet("color: rgb(239, 41, 41);")
        self.label2_13.setTextFormat(QtCore.Qt.AutoText)
        self.label2_13.setScaledContents(True)
        self.label2_13.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_13.setWordWrap(True)
        self.label2_13.setObjectName("label2_13")
        self.label2_11 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_11.setEnabled(True)
        self.label2_11.setGeometry(QtCore.QRect(30, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_11.setFont(font)
        self.label2_11.setAcceptDrops(False)
        self.label2_11.setAutoFillBackground(False)
        self.label2_11.setTextFormat(QtCore.Qt.AutoText)
        self.label2_11.setScaledContents(True)
        self.label2_11.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_11.setWordWrap(True)
        self.label2_11.setObjectName("label2_11")
        self.thersh_min_mov = QtWidgets.QLineEdit(self.groupBox_22)
        self.thersh_min_mov.setGeometry(QtCore.QRect(21, 121, 96, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thersh_min_mov.setFont(font)
        self.thersh_min_mov.setAlignment(QtCore.Qt.AlignCenter)
        self.thersh_min_mov.setObjectName("thersh_min_mov")
        self.label2_14 = QtWidgets.QLabel(self.groupBox_22)
        self.label2_14.setEnabled(True)
        self.label2_14.setGeometry(QtCore.QRect(30, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2_14.setFont(font)
        self.label2_14.setAcceptDrops(False)
        self.label2_14.setAutoFillBackground(False)
        self.label2_14.setTextFormat(QtCore.Qt.AutoText)
        self.label2_14.setScaledContents(True)
        self.label2_14.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label2_14.setWordWrap(True)
        self.label2_14.setObjectName("label2_14")
        self.thersh_max_mov = QtWidgets.QLineEdit(self.groupBox_22)
        self.thersh_max_mov.setGeometry(QtCore.QRect(124, 121, 96, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thersh_max_mov.setFont(font)
        self.thersh_max_mov.setAlignment(QtCore.Qt.AlignCenter)
        self.thersh_max_mov.setObjectName("thersh_max_mov")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_22)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 70, 141, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label2_6 = QtWidgets.QLabel(self.layoutWidget4)
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
        self.horizontalLayout.addWidget(self.label2_6)
        self.label2_7 = QtWidgets.QLabel(self.layoutWidget4)
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
        self.horizontalLayout.addWidget(self.label2_7)
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_17.setGeometry(QtCore.QRect(900, 120, 571, 321))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_17.setObjectName("groupBox_17")
        self.Framenumber_6 = QtWidgets.QLabel(self.groupBox_17)
        self.Framenumber_6.setGeometry(QtCore.QRect(30, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_6.setFont(font)
        self.Framenumber_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_6.setObjectName("Framenumber_6")
        self.combo_roi = QtWidgets.QComboBox(self.groupBox_17)
        self.combo_roi.setGeometry(QtCore.QRect(30, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.combo_roi.setFont(font)
        self.combo_roi.setObjectName("combo_roi")
        self.combo_roi.addItem("")
        self.combo_roi.addItem("")
        self.Framenumber_7 = QtWidgets.QLabel(self.groupBox_17)
        self.Framenumber_7.setEnabled(True)
        self.Framenumber_7.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_7.setFont(font)
        self.Framenumber_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_7.setObjectName("Framenumber_7")
        self.roi_shape_crop = QtWidgets.QComboBox(self.groupBox_17)
        self.roi_shape_crop.setEnabled(False)
        self.roi_shape_crop.setGeometry(QtCore.QRect(20, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roi_shape_crop.setFont(font)
        self.roi_shape_crop.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.roi_shape_crop.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.roi_shape_crop.setCurrentText("")
        self.roi_shape_crop.setObjectName("roi_shape_crop")
        self.roi_shape_crop.addItem("")
        self.roi_shape_crop.addItem("")
        self.calc_dist = QtWidgets.QPushButton(self.groupBox_17)
        self.calc_dist.setEnabled(True)
        self.calc_dist.setGeometry(QtCore.QRect(10, 160, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_dist.setFont(font)
        self.calc_dist.setObjectName("calc_dist")
        self.label2 = QtWidgets.QLabel(self.groupBox_17)
        self.label2.setEnabled(True)
        self.label2.setGeometry(QtCore.QRect(0, 210, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label2.setFont(font)
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setScaledContents(True)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.distance_crop = QtWidgets.QLineEdit(self.groupBox_17)
        self.distance_crop.setEnabled(True)
        self.distance_crop.setGeometry(QtCore.QRect(40, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_crop.setFont(font)
        self.distance_crop.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_crop.setObjectName("distance_crop")
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_18.setGeometry(QtCore.QRect(220, 30, 341, 181))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_18.setObjectName("groupBox_18")
        self.deter_center = QtWidgets.QPushButton(self.groupBox_18)
        self.deter_center.setEnabled(False)
        self.deter_center.setGeometry(QtCore.QRect(110, 40, 111, 41))
        self.deter_center.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(255, 100, 100), stop:0.395 rgb(255, 80, 80), stop:0.605 rgb(255, 50,50), stop:1 rgb(255, 0, 0));\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.deter_center.setObjectName("deter_center")
        self.label1 = QtWidgets.QLabel(self.groupBox_18)
        self.label1.setEnabled(True)
        self.label1.setGeometry(QtCore.QRect(0, 90, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setScaledContents(True)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label3 = QtWidgets.QLabel(self.groupBox_18)
        self.label3.setEnabled(True)
        self.label3.setGeometry(QtCore.QRect(0, 120, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label3.setFont(font)
        self.label3.setTextFormat(QtCore.Qt.AutoText)
        self.label3.setScaledContents(True)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.Framenumber_10 = QtWidgets.QLabel(self.groupBox_18)
        self.Framenumber_10.setGeometry(QtCore.QRect(40, 30, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_10.setFont(font)
        self.Framenumber_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_10.setText("")
        self.Framenumber_10.setPixmap(QtGui.QPixmap("images/icon/select_blue.png"))
        self.Framenumber_10.setScaledContents(True)
        self.Framenumber_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_10.setObjectName("Framenumber_10")
        self.groupBox_29 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_29.setGeometry(QtCore.QRect(290, 220, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.groupBox_29.setFont(font)
        self.groupBox_29.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_29.setObjectName("groupBox_29")
        self.thresh_option = QtWidgets.QComboBox(self.groupBox_29)
        self.thresh_option.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thresh_option.setFont(font)
        self.thresh_option.setObjectName("thresh_option")
        self.thresh_option.addItem("")
        self.thresh_option.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox_29)
        self.label.setGeometry(QtCore.QRect(120, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tresh_value = QtWidgets.QLineEdit(self.groupBox_29)
        self.tresh_value.setGeometry(QtCore.QRect(120, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tresh_value.setFont(font)
        self.tresh_value.setAlignment(QtCore.Qt.AlignCenter)
        self.tresh_value.setObjectName("tresh_value")
        self.layoutWidget5 = QtWidgets.QWidget(self.tab)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.splitter_4 = QtWidgets.QSplitter(self.tab)
        self.splitter_4.setGeometry(QtCore.QRect(791, 11, 111, 111))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.run_video = QtWidgets.QPushButton(self.splitter_4)
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
        self.stop_view_video = QtWidgets.QPushButton(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stop_view_video.setFont(font)
        self.stop_view_video.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icon/stop_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_view_video.setIcon(icon3)
        self.stop_view_video.setIconSize(QtCore.QSize(40, 40))
        self.stop_view_video.setObjectName("stop_view_video")
        self.splitter_3 = QtWidgets.QSplitter(self.tab)
        self.splitter_3.setGeometry(QtCore.QRect(21, 22, 671, 71))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.upload_video = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(True)
        self.upload_video.setFont(font)
        self.upload_video.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.upload_video.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.upload_video.setAcceptDrops(False)
        self.upload_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.upload_video.setAutoFillBackground(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icon/uplaod_video1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_video.setIcon(icon4)
        self.upload_video.setIconSize(QtCore.QSize(40, 40))
        self.upload_video.setShortcut("")
        self.upload_video.setObjectName("upload_video")
        self.read_parameters = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.read_parameters.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icon/read_parameters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.read_parameters.setIcon(icon5)
        self.read_parameters.setIconSize(QtCore.QSize(40, 40))
        self.read_parameters.setObjectName("read_parameters")
        self.save_parameters = QtWidgets.QPushButton(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_parameters.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icon/save_parameters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_parameters.setIcon(icon6)
        self.save_parameters.setIconSize(QtCore.QSize(40, 40))
        self.save_parameters.setObjectName("save_parameters")
        ethoflow.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.run_video_simple_ground = QtWidgets.QPushButton(self.tab1)
        self.run_video_simple_ground.setGeometry(QtCore.QRect(410, 300, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.run_video_simple_ground.setFont(font)
        self.run_video_simple_ground.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_video_simple_ground.setIcon(icon2)
        self.run_video_simple_ground.setIconSize(QtCore.QSize(50, 45))
        self.run_video_simple_ground.setObjectName("run_video_simple_ground")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 40, 301, 391))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.check_save_data = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_save_data.setGeometry(QtCore.QRect(20, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_save_data.setFont(font)
        self.check_save_data.setChecked(False)
        self.check_save_data.setObjectName("check_save_data")
        self.check_save_video = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_save_video.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_save_video.setFont(font)
        self.check_save_video.setChecked(False)
        self.check_save_video.setObjectName("check_save_video")
        self.show_video_processing = QtWidgets.QCheckBox(self.groupBox_2)
        self.show_video_processing.setGeometry(QtCore.QRect(20, 92, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.show_video_processing.setFont(font)
        self.show_video_processing.setChecked(False)
        self.show_video_processing.setObjectName("show_video_processing")
        self.check_end_video = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_end_video.setGeometry(QtCore.QRect(20, 130, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_end_video.setFont(font)
        self.check_end_video.setChecked(False)
        self.check_end_video.setObjectName("check_end_video")
        self.combo_id = QtWidgets.QComboBox(self.groupBox_2)
        self.combo_id.setGeometry(QtCore.QRect(80, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_id.setFont(font)
        self.combo_id.setObjectName("combo_id")
        self.combo_id.addItem("")
        self.combo_id.addItem("")
        self.Framenumber_8 = QtWidgets.QLabel(self.groupBox_2)
        self.Framenumber_8.setGeometry(QtCore.QRect(10, 230, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_8.setFont(font)
        self.Framenumber_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_8.setText("")
        self.Framenumber_8.setPixmap(QtGui.QPixmap("images/icon/id.png"))
        self.Framenumber_8.setScaledContents(True)
        self.Framenumber_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_8.setObjectName("Framenumber_8")
        self.check_regions = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_regions.setGeometry(QtCore.QRect(20, 155, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_regions.setFont(font)
        self.check_regions.setChecked(False)
        self.check_regions.setObjectName("check_regions")
        self.check_regions_ind = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_regions_ind.setGeometry(QtCore.QRect(20, 188, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_regions_ind.setFont(font)
        self.check_regions_ind.setChecked(False)
        self.check_regions_ind.setObjectName("check_regions_ind")
        self.video_time_in_frame = QtWidgets.QLineEdit(self.groupBox_2)
        self.video_time_in_frame.setGeometry(QtCore.QRect(80, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.video_time_in_frame.setFont(font)
        self.video_time_in_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.video_time_in_frame.setObjectName("video_time_in_frame")
        self.Framenumber_9 = QtWidgets.QLabel(self.groupBox_2)
        self.Framenumber_9.setGeometry(QtCore.QRect(20, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_9.setFont(font)
        self.Framenumber_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_9.setObjectName("Framenumber_9")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_19.setGeometry(QtCore.QRect(40, 560, 661, 271))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_19.setObjectName("groupBox_19")
        self.processing = QtWidgets.QLabel(self.groupBox_19)
        self.processing.setGeometry(QtCore.QRect(80, 30, 491, 51))
        self.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.processing.setAlignment(QtCore.Qt.AlignCenter)
        self.processing.setObjectName("processing")
        self.processed_frame_number = QtWidgets.QLCDNumber(self.groupBox_19)
        self.processed_frame_number.setGeometry(QtCore.QRect(310, 100, 141, 41))
        self.processed_frame_number.setStyleSheet("color: rgb(0, 0, 255);")
        self.processed_frame_number.setObjectName("processed_frame_number")
        self.Framenumber_37 = QtWidgets.QLabel(self.groupBox_19)
        self.Framenumber_37.setGeometry(QtCore.QRect(130, 110, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_37.setFont(font)
        self.Framenumber_37.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_37.setObjectName("Framenumber_37")
        self.Framenumber_12 = QtWidgets.QLabel(self.groupBox_19)
        self.Framenumber_12.setGeometry(QtCore.QRect(150, 200, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_12.setFont(font)
        self.Framenumber_12.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_12.setObjectName("Framenumber_12")
        self.display_spent_time = QtWidgets.QLabel(self.groupBox_19)
        self.display_spent_time.setGeometry(QtCore.QRect(300, 190, 191, 41))
        self.display_spent_time.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.display_spent_time.setAlignment(QtCore.Qt.AlignCenter)
        self.display_spent_time.setObjectName("display_spent_time")
        self.Framenumber_16 = QtWidgets.QLabel(self.groupBox_19)
        self.Framenumber_16.setGeometry(QtCore.QRect(90, 240, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_16.setFont(font)
        self.Framenumber_16.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_16.setObjectName("Framenumber_16")
        self.prop_detection = QtWidgets.QLabel(self.groupBox_19)
        self.prop_detection.setGeometry(QtCore.QRect(300, 230, 191, 41))
        self.prop_detection.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.prop_detection.setAlignment(QtCore.Qt.AlignCenter)
        self.prop_detection.setObjectName("prop_detection")
        self.video_progressBar = QtWidgets.QProgressBar(self.groupBox_19)
        self.video_progressBar.setGeometry(QtCore.QRect(130, 150, 401, 41))
        self.video_progressBar.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"")
        self.video_progressBar.setProperty("value", 0)
        self.video_progressBar.setObjectName("video_progressBar")
        self.groupBox_23 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_23.setGeometry(QtCore.QRect(410, 40, 321, 241))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_23.setFont(font)
        self.groupBox_23.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_23.setObjectName("groupBox_23")
        self.select_regions = QtWidgets.QPushButton(self.groupBox_23)
        self.select_regions.setEnabled(True)
        self.select_regions.setGeometry(QtCore.QRect(80, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_regions.setFont(font)
        self.select_regions.setObjectName("select_regions")
        self.Framenumber_17 = QtWidgets.QLabel(self.groupBox_23)
        self.Framenumber_17.setGeometry(QtCore.QRect(50, 110, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_17.setFont(font)
        self.Framenumber_17.setAcceptDrops(False)
        self.Framenumber_17.setScaledContents(True)
        self.Framenumber_17.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_17.setWordWrap(True)
        self.Framenumber_17.setObjectName("Framenumber_17")
        self.Framenumber_21 = QtWidgets.QLabel(self.groupBox_23)
        self.Framenumber_21.setGeometry(QtCore.QRect(10, 40, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_21.setFont(font)
        self.Framenumber_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_21.setText("")
        self.Framenumber_21.setPixmap(QtGui.QPixmap("images/icon/select_blue.png"))
        self.Framenumber_21.setScaledContents(True)
        self.Framenumber_21.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_21.setObjectName("Framenumber_21")
        self.groupBox_28 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_28.setGeometry(QtCore.QRect(780, 40, 691, 391))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_28.setFont(font)
        self.groupBox_28.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_28.setObjectName("groupBox_28")
        self.make_imgs_mask = QtWidgets.QPushButton(self.groupBox_28)
        self.make_imgs_mask.setGeometry(QtCore.QRect(330, 320, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.make_imgs_mask.setFont(font)
        self.make_imgs_mask.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../../home/rodrigo/.designer/backup/images/icon/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.make_imgs_mask.setIcon(icon7)
        self.make_imgs_mask.setIconSize(QtCore.QSize(50, 50))
        self.make_imgs_mask.setObjectName("make_imgs_mask")
        self.Framenumber_25 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_25.setGeometry(QtCore.QRect(60, 30, 611, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_25.setFont(font)
        self.Framenumber_25.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_25.setWordWrap(True)
        self.Framenumber_25.setObjectName("Framenumber_25")
        self.Framenumber_26 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_26.setGeometry(QtCore.QRect(60, 100, 621, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_26.setFont(font)
        self.Framenumber_26.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_26.setWordWrap(True)
        self.Framenumber_26.setObjectName("Framenumber_26")
        self.Framenumber_27 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_27.setGeometry(QtCore.QRect(60, 180, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_27.setFont(font)
        self.Framenumber_27.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_27.setWordWrap(True)
        self.Framenumber_27.setObjectName("Framenumber_27")
        self.start_img = QtWidgets.QLineEdit(self.groupBox_28)
        self.start_img.setGeometry(QtCore.QRect(210, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_img.setFont(font)
        self.start_img.setAlignment(QtCore.Qt.AlignCenter)
        self.start_img.setObjectName("start_img")
        self.Framenumber_28 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_28.setGeometry(QtCore.QRect(60, 250, 491, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_28.setFont(font)
        self.Framenumber_28.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_28.setWordWrap(True)
        self.Framenumber_28.setObjectName("Framenumber_28")
        self.Framenumber_22 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_22.setGeometry(QtCore.QRect(10, 40, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_22.setFont(font)
        self.Framenumber_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_22.setText("")
        self.Framenumber_22.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_22.setScaledContents(True)
        self.Framenumber_22.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_22.setObjectName("Framenumber_22")
        self.Framenumber_29 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_29.setGeometry(QtCore.QRect(10, 110, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_29.setFont(font)
        self.Framenumber_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_29.setText("")
        self.Framenumber_29.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_29.setScaledContents(True)
        self.Framenumber_29.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_29.setObjectName("Framenumber_29")
        self.Framenumber_30 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_30.setGeometry(QtCore.QRect(10, 190, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_30.setFont(font)
        self.Framenumber_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_30.setText("")
        self.Framenumber_30.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_30.setScaledContents(True)
        self.Framenumber_30.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_30.setObjectName("Framenumber_30")
        self.Framenumber_31 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_31.setGeometry(QtCore.QRect(10, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_31.setFont(font)
        self.Framenumber_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_31.setText("")
        self.Framenumber_31.setPixmap(QtGui.QPixmap("images/icon/tips.png"))
        self.Framenumber_31.setScaledContents(True)
        self.Framenumber_31.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_31.setObjectName("Framenumber_31")
        self.Framenumber_32 = QtWidgets.QLabel(self.groupBox_28)
        self.Framenumber_32.setGeometry(QtCore.QRect(450, 300, 61, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_32.setFont(font)
        self.Framenumber_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_32.setText("")
        self.Framenumber_32.setPixmap(QtGui.QPixmap("images/icon/make_data.png"))
        self.Framenumber_32.setScaledContents(True)
        self.Framenumber_32.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_32.setObjectName("Framenumber_32")
        self.line = QtWidgets.QFrame(self.tab1)
        self.line.setGeometry(QtCore.QRect(740, 20, 41, 871))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.run_video_complex_ground = QtWidgets.QPushButton(self.tab1)
        self.run_video_complex_ground.setGeometry(QtCore.QRect(390, 370, 341, 51))
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
        self.close_2 = QtWidgets.QPushButton(self.tab1)
        self.close_2.setGeometry(QtCore.QRect(1380, 0, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close_2.setFont(font)
        self.close_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.close_2.setIcon(icon1)
        self.close_2.setIconSize(QtCore.QSize(40, 40))
        self.close_2.setObjectName("close_2")
        self.stop_view_video_2 = QtWidgets.QPushButton(self.tab1)
        self.stop_view_video_2.setGeometry(QtCore.QRect(510, 450, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stop_view_video_2.setFont(font)
        self.stop_view_video_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stop_view_video_2.setIcon(icon3)
        self.stop_view_video_2.setIconSize(QtCore.QSize(40, 40))
        self.stop_view_video_2.setObjectName("stop_view_video_2")
        ethoflow.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.n_amostrad_frame = QtWidgets.QLineEdit(self.tab_2)
        self.n_amostrad_frame.setGeometry(QtCore.QRect(200, 740, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_amostrad_frame.setFont(font)
        self.n_amostrad_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.n_amostrad_frame.setObjectName("n_amostrad_frame")
        self.Framenumber_13 = QtWidgets.QLabel(self.tab_2)
        self.Framenumber_13.setGeometry(QtCore.QRect(150, 720, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_13.setFont(font)
        self.Framenumber_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_13.setObjectName("Framenumber_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 20, 341, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Framenumber_14 = QtWidgets.QLabel(self.groupBox_3)
        self.Framenumber_14.setGeometry(QtCore.QRect(40, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_14.setFont(font)
        self.Framenumber_14.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_14.setObjectName("Framenumber_14")
        self.Framenumber_18 = QtWidgets.QLabel(self.groupBox_3)
        self.Framenumber_18.setGeometry(QtCore.QRect(40, 110, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_18.setFont(font)
        self.Framenumber_18.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_18.setObjectName("Framenumber_18")
        self.n_behaviour_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.n_behaviour_1.setGeometry(QtCore.QRect(120, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_behaviour_1.setFont(font)
        self.n_behaviour_1.setAlignment(QtCore.Qt.AlignCenter)
        self.n_behaviour_1.setObjectName("n_behaviour_1")
        self.n_behaviour_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.n_behaviour_2.setGeometry(QtCore.QRect(120, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_behaviour_2.setFont(font)
        self.n_behaviour_2.setAlignment(QtCore.Qt.AlignCenter)
        self.n_behaviour_2.setObjectName("n_behaviour_2")
        self.make_imgs_behavior = QtWidgets.QPushButton(self.groupBox_3)
        self.make_imgs_behavior.setGeometry(QtCore.QRect(120, 210, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.make_imgs_behavior.setFont(font)
        self.make_imgs_behavior.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.make_imgs_behavior.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.make_imgs_behavior.setIcon(icon2)
        self.make_imgs_behavior.setIconSize(QtCore.QSize(40, 40))
        self.make_imgs_behavior.setObjectName("make_imgs_behavior")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(850, 20, 311, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.percent_behviour_ocorred = QtWidgets.QLabel(self.groupBox_4)
        self.percent_behviour_ocorred.setGeometry(QtCore.QRect(60, 250, 191, 51))
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
        self.Framenumber_23 = QtWidgets.QLabel(self.groupBox_4)
        self.Framenumber_23.setGeometry(QtCore.QRect(60, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Framenumber_23.setFont(font)
        self.Framenumber_23.setAcceptDrops(False)
        self.Framenumber_23.setAutoFillBackground(False)
        self.Framenumber_23.setMidLineWidth(0)
        self.Framenumber_23.setScaledContents(False)
        self.Framenumber_23.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_23.setWordWrap(True)
        self.Framenumber_23.setObjectName("Framenumber_23")
        self.run_behaviour = QtWidgets.QPushButton(self.groupBox_4)
        self.run_behaviour.setGeometry(QtCore.QRect(110, 150, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.run_behaviour.setFont(font)
        self.run_behaviour.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_behaviour.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_behaviour.setIcon(icon2)
        self.run_behaviour.setIconSize(QtCore.QSize(40, 40))
        self.run_behaviour.setObjectName("run_behaviour")
        self.Framenumber_33 = QtWidgets.QLabel(self.groupBox_4)
        self.Framenumber_33.setGeometry(QtCore.QRect(40, 40, 51, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Framenumber_33.setFont(font)
        self.Framenumber_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Framenumber_33.setText("")
        self.Framenumber_33.setPixmap(QtGui.QPixmap("images/icon/upload_model.png"))
        self.Framenumber_33.setScaledContents(True)
        self.Framenumber_33.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_33.setObjectName("Framenumber_33")
        self.upload_model = QtWidgets.QPushButton(self.groupBox_4)
        self.upload_model.setGeometry(QtCore.QRect(100, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upload_model.setFont(font)
        self.upload_model.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.upload_model.setIcon(icon7)
        self.upload_model.setIconSize(QtCore.QSize(50, 50))
        self.upload_model.setObjectName("upload_model")
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_24.setGeometry(QtCore.QRect(470, 350, 441, 171))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_24.setFont(font)
        self.groupBox_24.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_24.setObjectName("groupBox_24")
        self.stimate_progressBar = QtWidgets.QProgressBar(self.groupBox_24)
        self.stimate_progressBar.setGeometry(QtCore.QRect(20, 40, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stimate_progressBar.setFont(font)
        self.stimate_progressBar.setProperty("value", 0)
        self.stimate_progressBar.setObjectName("stimate_progressBar")
        self.Framenumber_15 = QtWidgets.QLabel(self.groupBox_24)
        self.Framenumber_15.setGeometry(QtCore.QRect(90, 110, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Framenumber_15.setFont(font)
        self.Framenumber_15.setAlignment(QtCore.Qt.AlignCenter)
        self.Framenumber_15.setObjectName("Framenumber_15")
        self.display_spent_time_meansure = QtWidgets.QLabel(self.groupBox_24)
        self.display_spent_time_meansure.setGeometry(QtCore.QRect(200, 110, 181, 41))
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
        self.groupBox_25 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_25.setGeometry(QtCore.QRect(20, 20, 431, 651))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_25.setFont(font)
        self.groupBox_25.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_25.setObjectName("groupBox_25")
        self.groupBox_26 = QtWidgets.QGroupBox(self.groupBox_25)
        self.groupBox_26.setGeometry(QtCore.QRect(50, 40, 341, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_26.setFont(font)
        self.groupBox_26.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_26.setObjectName("groupBox_26")
        self.stimated_sd_area = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_sd_area.setGeometry(QtCore.QRect(160, 60, 101, 21))
        self.stimated_sd_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_sd_area.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_sd_area.setObjectName("stimated_sd_area")
        self.label_16 = QtWidgets.QLabel(self.groupBox_26)
        self.label_16.setGeometry(QtCore.QRect(30, 40, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.stimated_area = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_area.setGeometry(QtCore.QRect(40, 60, 101, 21))
        self.stimated_area.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_area.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_area.setObjectName("stimated_area")
        self.label_20 = QtWidgets.QLabel(self.groupBox_26)
        self.label_20.setGeometry(QtCore.QRect(150, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.stimated_sd_len = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_sd_len.setGeometry(QtCore.QRect(160, 120, 101, 21))
        self.stimated_sd_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_sd_len.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_sd_len.setObjectName("stimated_sd_len")
        self.stimated_len = QtWidgets.QLabel(self.groupBox_26)
        self.stimated_len.setGeometry(QtCore.QRect(40, 120, 101, 21))
        self.stimated_len.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.stimated_len.setAlignment(QtCore.Qt.AlignCenter)
        self.stimated_len.setObjectName("stimated_len")
        self.label_19 = QtWidgets.QLabel(self.groupBox_26)
        self.label_19.setGeometry(QtCore.QRect(150, 100, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_15 = QtWidgets.QLabel(self.groupBox_26)
        self.label_15.setGeometry(QtCore.QRect(30, 100, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.Framenumber_11 = QtWidgets.QLabel(self.groupBox_26)
        self.Framenumber_11.setGeometry(QtCore.QRect(30, 150, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_11.setFont(font)
        self.Framenumber_11.setAcceptDrops(False)
        self.Framenumber_11.setMidLineWidth(0)
        self.Framenumber_11.setScaledContents(False)
        self.Framenumber_11.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_11.setWordWrap(True)
        self.Framenumber_11.setObjectName("Framenumber_11")
        self.groupBox_27 = QtWidgets.QGroupBox(self.groupBox_25)
        self.groupBox_27.setGeometry(QtCore.QRect(50, 300, 341, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_27.setFont(font)
        self.groupBox_27.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_27.setObjectName("groupBox_27")
        self.label_17 = QtWidgets.QLabel(self.groupBox_27)
        self.label_17.setGeometry(QtCore.QRect(20, 55, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.body_prop = QtWidgets.QLabel(self.groupBox_27)
        self.body_prop.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.body_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.body_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.body_prop.setObjectName("body_prop")
        self.sd_body_prop = QtWidgets.QLabel(self.groupBox_27)
        self.sd_body_prop.setGeometry(QtCore.QRect(180, 90, 101, 21))
        self.sd_body_prop.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(30, 30, 255);\n"
"")
        self.sd_body_prop.setAlignment(QtCore.Qt.AlignCenter)
        self.sd_body_prop.setObjectName("sd_body_prop")
        self.label_21 = QtWidgets.QLabel(self.groupBox_27)
        self.label_21.setGeometry(QtCore.QRect(180, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.Framenumber_20 = QtWidgets.QLabel(self.groupBox_27)
        self.Framenumber_20.setGeometry(QtCore.QRect(70, 130, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Framenumber_20.setFont(font)
        self.Framenumber_20.setAcceptDrops(False)
        self.Framenumber_20.setMidLineWidth(0)
        self.Framenumber_20.setScaledContents(False)
        self.Framenumber_20.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Framenumber_20.setWordWrap(True)
        self.Framenumber_20.setObjectName("Framenumber_20")
        self.Framenumber_19 = QtWidgets.QLabel(self.groupBox_25)
        self.Framenumber_19.setGeometry(QtCore.QRect(10, 610, 101, 41))
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
        self.run_estimates = QtWidgets.QPushButton(self.groupBox_25)
        self.run_estimates.setGeometry(QtCore.QRect(160, 530, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.run_estimates.setFont(font)
        self.run_estimates.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_estimates.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_estimates.setIcon(icon2)
        self.run_estimates.setIconSize(QtCore.QSize(40, 40))
        self.run_estimates.setObjectName("run_estimates")
        self.close_3 = QtWidgets.QPushButton(self.tab_2)
        self.close_3.setGeometry(QtCore.QRect(1380, 0, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.close_3.setFont(font)
        self.close_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.close_3.setIcon(icon1)
        self.close_3.setIconSize(QtCore.QSize(40, 40))
        self.close_3.setObjectName("close_3")
        ethoflow.addTab(self.tab_2, "")

        self.retranslateUi(ethoflow)
        ethoflow.setCurrentIndex(0)
        self.combo_roi.setCurrentIndex(-1)
        self.roi_shape_crop.setCurrentIndex(-1)
        self.thresh_option.setCurrentIndex(0)
        self.combo_id.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ethoflow)

    def retranslateUi(self, ethoflow):
        _translate = QtCore.QCoreApplication.translate
        ethoflow.setWindowTitle(_translate("ethoflow", "Ethoflow"))
        self.close.setText(_translate("ethoflow", "Close"))
        self.groupBox_5.setTitle(_translate("ethoflow", "Detection parameters"))
        self.groupBox_9.setTitle(_translate("ethoflow", "Length"))
        self.groupBox_10.setTitle(_translate("ethoflow", "Input"))
        self.label_4.setText(_translate("ethoflow", "Max"))
        self.max_len.setText(_translate("ethoflow", "100000"))
        self.label_5.setText(_translate("ethoflow", "Min"))
        self.min_len.setText(_translate("ethoflow", "0"))
        self.groupBox_11.setTitle(_translate("ethoflow", "Output"))
        self.label_11.setText(_translate("ethoflow", "Max"))
        self.label_14.setText(_translate("ethoflow", "Median"))
        self.output_max_len.setText(_translate("ethoflow", "------"))
        self.output_median_len.setText(_translate("ethoflow", "------"))
        self.label_12.setText(_translate("ethoflow", "Min"))
        self.label_13.setText(_translate("ethoflow", "SD"))
        self.output_min_len.setText(_translate("ethoflow", "------"))
        self.output_sd_len.setText(_translate("ethoflow", "------"))
        self.groupBox_6.setTitle(_translate("ethoflow", "Area"))
        self.groupBox_7.setTitle(_translate("ethoflow", "Input"))
        self.min_area.setText(_translate("ethoflow", "0"))
        self.label_2.setText(_translate("ethoflow", "Max"))
        self.max_area.setText(_translate("ethoflow", "100000"))
        self.label_3.setText(_translate("ethoflow", "Min"))
        self.groupBox_8.setTitle(_translate("ethoflow", "Output"))
        self.label_7.setText(_translate("ethoflow", "Max"))
        self.label_10.setText(_translate("ethoflow", "Median"))
        self.output_max_area.setText(_translate("ethoflow", "------"))
        self.output_median_area.setText(_translate("ethoflow", "------"))
        self.label_8.setText(_translate("ethoflow", "Min"))
        self.label_9.setText(_translate("ethoflow", "SD"))
        self.output_min_area.setText(_translate("ethoflow", "------"))
        self.output_sd_area.setText(_translate("ethoflow", "------"))
        self.groupBox_15.setTitle(_translate("ethoflow", "Video"))
        self.Resolution.setTitle(_translate("ethoflow", "Resolution"))
        self.set_frame_resolution.setText(_translate("ethoflow", "100"))
        self.Framenumber_24.setText(_translate("ethoflow", "%"))
        self.Framenumber_4.setText(_translate("ethoflow", "Y"))
        self.Framenumber_5.setText(_translate("ethoflow", "X"))
        self.shape_1.setText(_translate("ethoflow", "------"))
        self.shape_0.setText(_translate("ethoflow", "------"))
        self.Framenumber.setText(_translate("ethoflow", "Frame"))
        self.frame_number.setText(_translate("ethoflow", "0"))
        self.Framenumber_2.setText(_translate("ethoflow", "Total"))
        self.Framenumber_3.setText(_translate("ethoflow", "of"))
        self.n_ind.setText(_translate("ethoflow", "1"))
        self.label_6.setText(_translate("ethoflow", "<html><head/><body><p>N individuos</p></body></html>"))
        self.groupBox_12.setTitle(_translate("ethoflow", "Proportion"))
        self.groupBox_13.setTitle(_translate("ethoflow", "Input"))
        self.label_27.setText(_translate("ethoflow", "Min"))
        self.label_28.setText(_translate("ethoflow", "Max"))
        self.min_prop.setText(_translate("ethoflow", "0"))
        self.max_prop.setText(_translate("ethoflow", "100000"))
        self.groupBox_14.setTitle(_translate("ethoflow", "Output"))
        self.label_30.setText(_translate("ethoflow", "Max"))
        self.label_31.setText(_translate("ethoflow", "Median"))
        self.output_max_prop.setText(_translate("ethoflow", "------"))
        self.output_median_prop.setText(_translate("ethoflow", "------"))
        self.label_29.setText(_translate("ethoflow", "Min"))
        self.label_32.setText(_translate("ethoflow", "SD"))
        self.output_min_prop.setText(_translate("ethoflow", "------"))
        self.output_sd_prop.setText(_translate("ethoflow", "------"))
        self.groupBox_16.setTitle(_translate("ethoflow", "Analysis parameters"))
        self.groupBox_20.setTitle(_translate("ethoflow", "Scale"))
        self.label2_2.setText(_translate("ethoflow", "Select 2 points for know distance"))
        self.calc_dist_scale.setText(_translate("ethoflow", "calculate "))
        self.label2_3.setText(_translate("ethoflow", "Put real scale distance (e.g. cm)"))
        self.label2_9.setText(_translate("ethoflow", "Attention:"))
        self.label2_8.setText(_translate("ethoflow", "after adjusting the resolution"))
        self.distance_scale.setText(_translate("ethoflow", "1"))
        self.distance_scale_know.setText(_translate("ethoflow", "1"))
        self.groupBox_21.setTitle(_translate("ethoflow", "Interaction"))
        self.label2_12.setText(_translate("ethoflow", "Observation:"))
        self.label2_10.setText(_translate("ethoflow", "Put the interaction threshold"))
        self.interaction_threshold.setText(_translate("ethoflow", "0.8"))
        self.label2_4.setText(_translate("ethoflow", "Interaction will be considered when individuals approach a shorter distance. Put real distance (e.g. cm)"))
        self.groupBox_22.setTitle(_translate("ethoflow", "Movement"))
        self.label2_13.setText(_translate("ethoflow", "Observation:"))
        self.label2_11.setText(_translate("ethoflow", "Put the movement threshold"))
        self.thersh_min_mov.setText(_translate("ethoflow", "0.02"))
        self.label2_14.setText(_translate("ethoflow", "Put real distance (e.g. cm)"))
        self.thersh_max_mov.setText(_translate("ethoflow", "0.3"))
        self.label2_6.setText(_translate("ethoflow", "Low"))
        self.label2_7.setText(_translate("ethoflow", "High"))
        self.groupBox_17.setTitle(_translate("ethoflow", "ROI and threshold"))
        self.Framenumber_6.setText(_translate("ethoflow", "Select"))
        self.combo_roi.setItemText(0, _translate("ethoflow", "No"))
        self.combo_roi.setItemText(1, _translate("ethoflow", "Yes"))
        self.Framenumber_7.setText(_translate("ethoflow", "Shape"))
        self.roi_shape_crop.setItemText(0, _translate("ethoflow", "Circle"))
        self.roi_shape_crop.setItemText(1, _translate("ethoflow", "Rectangle"))
        self.calc_dist.setText(_translate("ethoflow", "Calculate distance"))
        self.label2.setText(_translate("ethoflow", "-> select center and edge (2 points)"))
        self.distance_crop.setText(_translate("ethoflow", "0"))
        self.groupBox_18.setTitle(_translate("ethoflow", "Choose arena"))
        self.deter_center.setText(_translate("ethoflow", "Select"))
        self.label1.setText(_translate("ethoflow", "Select the center of the arena (1 point)"))
        self.label3.setText(_translate("ethoflow", "-> select upper left and lower right (2 points)"))
        self.groupBox_29.setTitle(_translate("ethoflow", "Threshold"))
        self.thresh_option.setItemText(0, _translate("ethoflow", "Manual"))
        self.thresh_option.setItemText(1, _translate("ethoflow", "Automatic"))
        self.label.setText(_translate("ethoflow", "Value"))
        self.tresh_value.setText(_translate("ethoflow", "95"))
        self.run_video.setText(_translate("ethoflow", "Run "))
        self.stop_view_video.setText(_translate("ethoflow", "Stop"))
        self.upload_video.setText(_translate("ethoflow", "Upload video"))
        self.read_parameters.setText(_translate("ethoflow", "Read parameters"))
        self.save_parameters.setText(_translate("ethoflow", "Save parameters"))
        ethoflow.setTabText(ethoflow.indexOf(self.tab), _translate("ethoflow", "Settings"))
        self.run_video_simple_ground.setText(_translate("ethoflow", "Run simple background"))
        self.groupBox_2.setTitle(_translate("ethoflow", "Outputs"))
        self.check_save_data.setText(_translate("ethoflow", "Save data"))
        self.check_save_video.setText(_translate("ethoflow", "Save video"))
        self.show_video_processing.setText(_translate("ethoflow", "Show video in processing"))
        self.check_end_video.setText(_translate("ethoflow", "Notify when finished"))
        self.combo_id.setItemText(0, _translate("ethoflow", "No"))
        self.combo_id.setItemText(1, _translate("ethoflow", "Yes"))
        self.check_regions.setText(_translate("ethoflow", "Regions"))
        self.check_regions_ind.setText(_translate("ethoflow", "Regions by individuals"))
        self.video_time_in_frame.setText(_translate("ethoflow", "100"))
        self.Framenumber_9.setText(_translate("ethoflow", "Video time in frame"))
        self.groupBox_19.setTitle(_translate("ethoflow", "Processing summary"))
        self.processing.setText(_translate("ethoflow", "------"))
        self.Framenumber_37.setText(_translate("ethoflow", "Frame number ="))
        self.Framenumber_12.setText(_translate("ethoflow", "Time spent ="))
        self.display_spent_time.setText(_translate("ethoflow", "------"))
        self.Framenumber_16.setText(_translate("ethoflow", "True detection rate ="))
        self.prop_detection.setText(_translate("ethoflow", "------"))
        self.groupBox_23.setTitle(_translate("ethoflow", "Regions"))
        self.select_regions.setText(_translate("ethoflow", "Select regions"))
        self.Framenumber_17.setText(_translate("ethoflow", "Presse Enter, then: - Press \"q\" to quit selecting boxes  - Press any other key to select next region"))
        self.groupBox_28.setTitle(_translate("ethoflow", "Make data for mask R-CNN"))
        self.make_imgs_mask.setText(_translate("ethoflow", "Make data"))
        self.Framenumber_25.setText(_translate("ethoflow", "The images will be save in path: \"\'make_mask_rcnn_data/mask_imgs\""))
        self.Framenumber_26.setText(_translate("ethoflow", "In the \"video time in frame\" place the amount of images that will be generated. This should be <= the number of backgrounds"))
        self.Framenumber_27.setText(_translate("ethoflow", "Make images separate for training and validation"))
        self.start_img.setText(_translate("ethoflow", "1"))
        self.Framenumber_28.setText(_translate("ethoflow", "Entry start image value. It is to when save different .json file"))
        self.run_video_complex_ground.setText(_translate("ethoflow", "Run complex background"))
        self.close_2.setText(_translate("ethoflow", "Close"))
        self.stop_view_video_2.setText(_translate("ethoflow", "Stop"))
        ethoflow.setTabText(ethoflow.indexOf(self.tab1), _translate("ethoflow", "Analyses"))
        self.n_amostrad_frame.setText(_translate("ethoflow", "100"))
        self.Framenumber_13.setText(_translate("ethoflow", "Video time in frame"))
        self.groupBox_3.setTitle(_translate("ethoflow", "Make data for train"))
        self.Framenumber_14.setText(_translate("ethoflow", "N images for complex behavior"))
        self.Framenumber_18.setText(_translate("ethoflow", "N images for non behavior"))
        self.n_behaviour_1.setText(_translate("ethoflow", "10"))
        self.n_behaviour_2.setText(_translate("ethoflow", "10"))
        self.make_imgs_behavior.setText(_translate("ethoflow", "Run "))
        self.groupBox_4.setTitle(_translate("ethoflow", "AI behaviour analyses"))
        self.percent_behviour_ocorred.setText(_translate("ethoflow", "------"))
        self.Framenumber_23.setText(_translate("ethoflow", "Behavior occurrence (%)"))
        self.run_behaviour.setText(_translate("ethoflow", "Run "))
        self.upload_model.setText(_translate("ethoflow", "Upload CNN"))
        self.groupBox_24.setTitle(_translate("ethoflow", "Processing summary"))
        self.Framenumber_15.setText(_translate("ethoflow", "Time spent ="))
        self.display_spent_time_meansure.setText(_translate("ethoflow", "------"))
        self.groupBox_25.setTitle(_translate("ethoflow", "Measurements"))
        self.groupBox_26.setTitle(_translate("ethoflow", "Area and length"))
        self.stimated_sd_area.setText(_translate("ethoflow", "------"))
        self.label_16.setText(_translate("ethoflow", "Median area"))
        self.stimated_area.setText(_translate("ethoflow", "------"))
        self.label_20.setText(_translate("ethoflow", "SD  area"))
        self.stimated_sd_len.setText(_translate("ethoflow", "------"))
        self.stimated_len.setText(_translate("ethoflow", "------"))
        self.label_19.setText(_translate("ethoflow", "SD length"))
        self.label_15.setText(_translate("ethoflow", "Median length"))
        self.Framenumber_11.setText(_translate("ethoflow", "Area and length estimates based on random frames where there is no cross."))
        self.groupBox_27.setTitle(_translate("ethoflow", "Proportion"))
        self.label_17.setText(_translate("ethoflow", "Median"))
        self.body_prop.setText(_translate("ethoflow", "------"))
        self.sd_body_prop.setText(_translate("ethoflow", "------"))
        self.label_21.setText(_translate("ethoflow", "SD"))
        self.Framenumber_20.setText(_translate("ethoflow", "Area / length ratio in any frame (with cross or not)"))
        self.Framenumber_19.setText(_translate("ethoflow", "Unit = pixels"))
        self.run_estimates.setText(_translate("ethoflow", "Run "))
        self.close_3.setText(_translate("ethoflow", "Close"))
        ethoflow.setTabText(ethoflow.indexOf(self.tab_2), _translate("ethoflow", "Deep analyses"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ethoflow = QtWidgets.QTabWidget()
    ui = Ui_ethoflow()
    ui.setupUi(ethoflow)
    ethoflow.show()
    sys.exit(app.exec_())
