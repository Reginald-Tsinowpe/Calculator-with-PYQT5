# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



#TO DO: Write code for an animated slide-in/drop-down widget when the menuTheme button is clicked
#TO DO: Write code to change the theme

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from datetime import datetime
import json

class Ui_History_Window(object):
    def load_history(self):
        with open("history.json", 'r') as self.history_json_file:
            for i in self.history_json_file:
                line_data = json.loads(i)
                for key, value in line_data.items():
                    self.history_groupbox = QtWidgets.QGroupBox(key)
                    self.history_groupbox_Vlayout = QtWidgets.QVBoxLayout()
                    self.history_groupbox.setLayout(self.history_groupbox_Vlayout)
                    self.history_groupbox_Vlayout.setAlignment(QtCore.Qt.AlignRight)

                    for i in value:
                        index_in_value = QtWidgets.QLabel(i)
                        self.history_groupbox_Vlayout.addWidget(index_in_value)

                    self.verticalLayout_2.addWidget(self.history_groupbox)
                    self.v_groupbox_spacer = QtWidgets.QSpacerItem(1, 20)
                    self.verticalLayout_2.addItem(self.v_groupbox_spacer)


    def Sort_History(self, reversed):
        store_default_in = {}

        with open('history.json', 'r') as data_to_sort:
            for i in data_to_sort:
                write_to_dict = json.loads(i)
                for key, value in write_to_dict.items():
                    store_default_in[key] = value

        sorted_data = sorted(store_default_in.items(), key=lambda x: x[0], reverse=reversed)
        sorted_dict = dict(sorted_data)

        with open("history.json", 'w') as sorted_write_to_file:
            for key, value in sorted_dict.items():
                json.dump({key: value}, sorted_write_to_file)
                sorted_write_to_file.write('\n')

        """for i in reversed(range(self.verticalLayout_2.count())):
            print("for loop started running.")

            item = self.verticalLayout_2.itemAt(i)
            widget = item.widget()
            if isinstance(widget, QtWidgets.QGroupBox):
                self.verticalLayout_2.takeAt(i)
                widget.deleteLater()"""

        try:
            for i in range(self.verticalLayout_2.count() - 1, -1, -1):
                item = self.verticalLayout_2.itemAt(i)
                widget = item.widget()
                if isinstance(widget, QtWidgets.QGroupBox):
                    self.verticalLayout_2.takeAt(i)
                    widget.deleteLater()
                if isinstance(item, QtWidgets.QSpacerItem):
                    self.verticalLayout_2.takeAt(i)
        except Exception as e:
            print(e)

        self.load_history()


    def setupUi(self, History_Window):
        History_Window.setObjectName("History_Window")
        History_Window.resize(426, 482)
        History_Window.setMinimumSize(QtCore.QSize(426, 482))
        History_Window.setMaximumSize(QtCore.QSize(426, 482))
        History_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(History_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.History_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.History_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.History_scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.History_scrollArea.setWidgetResizable(True)
        self.History_scrollArea.setObjectName("History_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 408, 443))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.History_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.History_scrollArea)
        History_Window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(History_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")

        self.menuSort = QtWidgets.QMenu(self.menubar)
        self.menuSort.setObjectName("menuSort")
        History_Window.setMenuBar(self.menubar)

        self.actionOldest_First = QtWidgets.QAction(History_Window)
        self.actionOldest_First.setObjectName("actionOldest_First")

        self.actionNewest_First = QtWidgets.QAction(History_Window)
        self.actionNewest_First.setObjectName("actionNewest_First")

        self.actionOldest_First.triggered.connect(lambda: self.Sort_History(False))
        self.actionNewest_First.triggered.connect(lambda: self.Sort_History(True))

        self.menuSort.addAction(self.actionOldest_First)
        self.menuSort.addAction(self.actionNewest_First)
        self.menubar.addAction(self.menuSort.menuAction())

        self.retranslateUi(History_Window)
        QtCore.QMetaObject.connectSlotsByName(History_Window)



    def retranslateUi(self, History_Window):
        _translate = QtCore.QCoreApplication.translate
        History_Window.setWindowTitle(_translate("History_Window", "MainWindow"))
        self.menuSort.setTitle(_translate("History_Window", "Sort"))
        self.actionOldest_First.setText(_translate("History_Window", "Oldest First"))
        self.actionNewest_First.setText(_translate("History_Window", "Newest First"))





class Ui_MainWindow(object):

    def __init__(self):
        self.centralwidget = None
        self.first_button = True
        self.record = False
        self.record_history = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 404)
        MainWindow.setMinimumSize(QtCore.QSize(397, 404))
        MainWindow.setMaximumSize(QtCore.QSize(397, 404))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(397, 383))
        self.centralwidget.setMaximumSize(QtCore.QSize(397, 383))
        self.centralwidget.setObjectName("centralwidget")

        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(80, 70, 75, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_8.clicked.connect(lambda: self.button_clicked(self.button_8))

        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(80, 140, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_5.clicked.connect(lambda: self.button_clicked(self.button_5))

        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(160, 220, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_3.clicked.connect(lambda: self.button_clicked(self.button_3))

        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(0, 140, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_4.clicked.connect(lambda: self.button_clicked(self.button_4))

        self.subtract = QtWidgets.QPushButton(self.centralwidget)
        self.subtract.setGeometry(QtCore.QRect(320, 220, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setKerning(True)
        self.subtract.setFont(font)
        self.subtract.setObjectName("subtract")
        self.subtract.clicked.connect(lambda: self.button_clicked(self.subtract))

        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(0, 300, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.point.setFont(font)
        self.point.setObjectName("point")
        self.point.clicked.connect(lambda: self.button_clicked(self.point))

        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(160, 70, 75, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.button_9.clicked.connect(lambda: self.button_clicked(self.button_9))

        self.sum = QtWidgets.QPushButton(self.centralwidget)
        self.sum.setGeometry(QtCore.QRect(240, 220, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.sum.setFont(font)
        self.sum.setObjectName("sum")
        self.sum.clicked.connect(lambda: self.button_clicked(self.sum))

        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(0, 220, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_1.clicked.connect(lambda: self.button_clicked(self.button_1))

        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(240, 140, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.multiply.clicked.connect(lambda: self.button_clicked(self.multiply))

        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(0, 70, 75, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_7.setFont(font)
        self.button_7.setShortcut("")
        self.button_7.setDefault(False)
        self.button_7.setObjectName("button_7")
        self.button_7.clicked.connect(lambda: self.button_clicked(self.button_7))

        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(320, 140, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        self.divide.clicked.connect(lambda: self.button_clicked(self.divide))

        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(160, 140, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_6.clicked.connect(lambda: self.button_clicked(self.button_6))

        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(80, 220, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_2.clicked.connect(lambda: self.button_clicked(self.button_2))

        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(80, 300, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_0.clicked.connect(lambda: self.button_clicked(self.button_0))

        self.clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all.setGeometry(QtCore.QRect(240, 70, 155, 71))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.clear_all.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.clear_all.setFont(font)
        self.clear_all.setMouseTracking(False)
        self.clear_all.setAutoDefault(False)
        self.clear_all.setDefault(False)
        self.clear_all.setFlat(False)
        self.clear_all.setObjectName("clear_all")
        self.clear_all.clicked.connect(lambda: self.button_clicked(self.clear_all))

###     THE PUSHBUTTON BELOW SHOULD JUST BE 'DELETE', NOT 'DELETE_2'
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(310, 0, 85, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setKerning(True)
        self.delete_2.setFont(font)
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(lambda: self.button_clicked(self.delete_2))

        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(160, 300, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.equal.clicked.connect(lambda: self.button_clicked(self.equal))

        self.open_p = QtWidgets.QPushButton(self.centralwidget)
        self.open_p.setGeometry(QtCore.QRect(240, 300, 75, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.open_p.setFont(font)
        self.open_p.setObjectName("open_p")
        self.open_p.clicked.connect(lambda: self.button_clicked(self.open_p))

        self.close_p = QtWidgets.QPushButton(self.centralwidget)
        self.close_p.setGeometry(QtCore.QRect(320, 300, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.close_p.setFont(font)
        self.close_p.setObjectName("close_p")
        self.close_p.clicked.connect(lambda: self.button_clicked(self.close_p))


        self.input_display = QtWidgets.QLabel(self.centralwidget)
        self.input_display.setGeometry(QtCore.QRect(0, 0, 301, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        self.input_display.setFont(font)
        self.input_display.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"}")
        self.input_display.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.input_display.setIndent(0)
        self.input_display.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.input_display.setObjectName("input_display")


        self.result_display = QtWidgets.QLabel(self.centralwidget)
        self.result_display.setGeometry(QtCore.QRect(210, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.result_display.setFont(font)
        self.result_display.setStyleSheet("QLabel{\n"
"    color:grey;\n"
"}")
        self.result_display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result_display.setIndent(0)
        self.result_display.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.result_display.setObjectName("result_display")

            #The Button at 0,0 to record calculation Entries
        self.record_calulations = QtWidgets.QPushButton(self.centralwidget)
        self.record_calulations.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.record_calulations.setObjectName("record_calculations")
        self.record_calulations.setIcon(QtGui.QIcon("record_512px.png"))
        self.record_calulations.clicked.connect(self.Record_Calculations)


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
        self.menubar.setObjectName("menubar")

        self.menuHISTORY = QtWidgets.QMenu(self.menubar)
        self.menuHISTORY.setObjectName("menuHISTORY")

        self.menuTHEME = QtWidgets.QMenu(self.menubar)
        self.menuTHEME.setObjectName("menuTHEME")


        self.menubar.addAction("HISTORY").triggered.connect(self.Open_History)
        self.menubar.addAction("THEME").triggered.connect(self.Theme_widget)
        #self.menubar.addAction(self.menuTHEME.menuAction())
        #self.menuTHEME.menuAction().triggered.connect(self.Theme_widget)
        # Create additional actions for the menuTHEME
        #change_theme_action = QtWidgets.QAction("Change Theme", self.menuTHEME)
        #change_theme_action.triggered.connect(self.Theme_widget)
        #self.menuTHEME.addAction(change_theme_action)


        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.delete_2, self.button_7)
        MainWindow.setTabOrder(self.button_7, self.button_8)
        MainWindow.setTabOrder(self.button_8, self.button_9)
        MainWindow.setTabOrder(self.button_9, self.clear_all)
        MainWindow.setTabOrder(self.clear_all, self.button_4)
        MainWindow.setTabOrder(self.button_4, self.button_5)
        MainWindow.setTabOrder(self.button_5, self.button_6)
        MainWindow.setTabOrder(self.button_6, self.multiply)
        MainWindow.setTabOrder(self.multiply, self.divide)
        MainWindow.setTabOrder(self.divide, self.button_1)
        MainWindow.setTabOrder(self.button_1, self.button_2)
        MainWindow.setTabOrder(self.button_2, self.button_3)
        MainWindow.setTabOrder(self.button_3, self.sum)
        MainWindow.setTabOrder(self.sum, self.subtract)
        MainWindow.setTabOrder(self.subtract, self.point)
        MainWindow.setTabOrder(self.point, self.button_0)
        MainWindow.setTabOrder(self.button_0, self.equal)
        MainWindow.setTabOrder(self.equal, self.open_p)
        MainWindow.setTabOrder(self.open_p, self.close_p)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt Calculator"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_8.setShortcut(_translate("MainWindow", "8"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_5.setShortcut(_translate("MainWindow", "5"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_3.setShortcut(_translate("MainWindow", "3"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_4.setShortcut(_translate("MainWindow", "4"))
        self.subtract.setText(_translate("MainWindow", "-"))
        self.subtract.setShortcut(_translate("MainWindow", "-"))
        self.point.setText(_translate("MainWindow", "."))
        self.point.setShortcut(_translate("MainWindow", "."))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_9.setShortcut(_translate("MainWindow", "9"))
        self.sum.setText(_translate("MainWindow", "+"))
        self.sum.setShortcut(_translate("MainWindow", "+"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_1.setShortcut(_translate("MainWindow", "1"))
        self.multiply.setText(_translate("MainWindow", "×"))
        self.multiply.setShortcut(_translate("MainWindow", "*"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_7.setShortcut(_translate("MainWindow", "7"))
        self.divide.setText(_translate("MainWindow", "÷"))
        self.divide.setShortcut(_translate("MainWindow", "/"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_6.setShortcut(_translate("MainWindow", "6"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_2.setShortcut(_translate("MainWindow", "2"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_0.setShortcut(_translate("MainWindow", "0"))
        self.clear_all.setText(_translate("MainWindow", "AC"))
        self.clear_all.setShortcut(_translate("MainWindow", "Del"))
        self.delete_2.setText(_translate("MainWindow", "DEL"))
        self.delete_2.setShortcut(_translate("MainWindow", "Backspace"))

        self.equal.setText(_translate("MainWindow", "="))
        #self.equal.setShortcut(_translate("MainWindow", "="))
        #self.equal.setShortcut("=")

        # Create an action associated with the button
        action_equal = QtWidgets.QAction(self.equal)
        action_equal.setText("=")
        # Set multiple shortcuts for the action
        action_equal.setShortcut("Ctrl+E")
        action_equal.setShortcut("Ctrl+Shift+E")
        # Add the action to the QPushButton
        self.equal.addAction(action_equal)
        # Connect the triggered signal of the action to the appropriate function
        action_equal.triggered.connect(self.button_clicked)


        
        self.open_p.setText(_translate("MainWindow", "("))
        self.open_p.setShortcut(_translate("MainWindow", "("))
        self.close_p.setText(_translate("MainWindow", ")"))
        self.close_p.setShortcut(_translate("MainWindow", ")"))

        self.input_display.setText(_translate("MainWindow", "0"))
        self.result_display.setText(_translate("MainWindow", "0"))

        self.menuHISTORY.setTitle(_translate("MainWindow", "HISTORY"))
        self.menuTHEME.setTitle(_translate("MainWindow", "THEME"))


    def Record_Calculations(self):
        if (not self.record):
            self.record_calulations.setStyleSheet("background-color:#507BE6; border:1px solid #507BE6; border-radius:5px;")
            self.record = True
            self.time_now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.record_history[self.time_now] = []

        else:
            self.record = False
            self.record_calulations.setStyleSheet("background-color:transparent; border:1px solid #B1B3B9; border-radius:5px;")
            if (not self.record_history[self.time_now]):
                del self.record_history[self.time_now]


            with open("history.json", 'a') as history_json_file:
                for key, value in self.record_history.items():
                    json.dump({key: value}, history_json_file)
                    history_json_file.write('\n')


    def button_clicked(self, button_name):
        if self.first_button:
            self.input_display.setText('')
            self.first_button = False
        if (button_name.text()!='=' and button_name.text()!='DEL' and button_name.text()!='AC'):
            self.input_display.setText(self.input_display.text() + button_name.text())
        if (button_name.text() == 'DEL'):
            self.input_display.setText(self.input_display.text()[0:-1])
        if (button_name.text() == 'AC'):
            self.input_display.setText('')
            self.result_display.setText('0')
            self.input_display.setText('0')
            self.first_button = True
        if (button_name.text() == '='):
            self.inputted_text = self.input_display.text()
            for i in self.inputted_text:
                if i == '0':
                    self.inputted_text = self.inputted_text[1:]
                else:
                    break
            self.raw_inputted_text = self.inputted_text
            self.inputted_text = self.inputted_text.replace('÷', '/')
            self.inputted_text = self.inputted_text.replace('×', '*')

###     TO-DO: Ensure that all calculation errors are dealt with
            arith_list = ['+', '-', '*', '/']
            try:
                if self.inputted_text[0] in arith_list:
                    self.result = round(eval(f"{self.result_display.text()}{self.inputted_text}"), 5)
                elif (self.inputted_text[0] == '('):
                    self.result = round(eval(f"{self.result_display.text()}*{self.inputted_text}"), 5)
                else:
                    self.result = round(eval(f"{self.inputted_text}"), 5)
            except Exception as e:
                print(f"calculation-error\nException: {e}")


            if self.record:
                if self.inputted_text[0] in arith_list:
                    self.history_input = f"{self.result_display.text()}{self.inputted_text} = {self.result}"
                elif (self.inputted_text[0] == '('):
                    self.history_input = f"{self.result_display.text()}*{self.inputted_text} = {self.result}"
                else:
                    self.history_input = f"{self.inputted_text} = {self.result}"

                self.record_history[self.time_now].append(self.history_input)

            self.input_display.setText('')
            self.result_display.setText(str(self.result))


    def Open_History(self):
        self.History_Window = QtWidgets.QMainWindow()
        self.history_ui = Ui_History_Window()
        self.history_ui.setupUi(self.History_Window)
        self.history_ui.load_history()
        self.History_Window.show()

    def Theme_widget(self):


        dlg = QtWidgets.QDialog()
        dlg.setMaximumSize(200, 100)
        label = QtWidgets.QLabel("I'll work on that later", dlg)
        label.move(30, 50)

        dlg.setWindowTitle("Coming Soon")

        #dlg.setWindowModality(ApplicationModal)
        dlg.exec_()

        print("Theme Menu Option Clicked")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
