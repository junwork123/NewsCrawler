# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.edit_keyword = QtWidgets.QPlainTextEdit(self.widget)
        self.edit_keyword.setGeometry(QtCore.QRect(10, 30, 621, 71))
        self.edit_keyword.setPlainText("")
        self.edit_keyword.setObjectName("edit_keyword")
        self.label_search = QtWidgets.QLabel(self.widget)
        self.label_search.setGeometry(QtCore.QRect(10, 10, 56, 12))
        self.label_search.setObjectName("label_search")
        self.box_search_options = QtWidgets.QGroupBox(self.widget)
        self.box_search_options.setGeometry(QtCore.QRect(10, 110, 621, 141))
        self.box_search_options.setObjectName("box_search_options")
        self.comboBox = QtWidgets.QComboBox(self.box_search_options)
        self.comboBox.setGeometry(QtCore.QRect(21, 40, 61, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.spin_min = QtWidgets.QSpinBox(self.box_search_options)
        self.spin_min.setGeometry(QtCore.QRect(110, 100, 42, 22))
        self.spin_min.setMaximum(59)
        self.spin_min.setObjectName("spin_min")
        self.label_period = QtWidgets.QLabel(self.box_search_options)
        self.label_period.setGeometry(QtCore.QRect(72, 103, 241, 16))
        self.label_period.setObjectName("label_period")
        self.spin_hour = QtWidgets.QSpinBox(self.box_search_options)
        self.spin_hour.setGeometry(QtCore.QRect(23, 101, 42, 22))
        self.spin_hour.setMaximum(23)
        self.spin_hour.setObjectName("spin_hour")
        self.spin_sec = QtWidgets.QSpinBox(self.box_search_options)
        self.spin_sec.setGeometry(QtCore.QRect(190, 100, 42, 22))
        self.spin_sec.setMaximum(59)
        self.spin_sec.setObjectName("spin_sec")
        self.label = QtWidgets.QLabel(self.box_search_options)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 611, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 460, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 460, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.edit_keyword, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_search.setText(_translate("MainWindow", "검색어"))
        self.box_search_options.setTitle(_translate("MainWindow", "검색옵션"))
        self.comboBox.setItemText(0, _translate("MainWindow", "OR"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AND"))
        self.label_period.setText(_translate("MainWindow", "시간                분                 초 마다 검색"))
        self.label.setText(_translate("MainWindow", "검색어 결합"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "검색설정"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "검색결과"))
        self.pushButton.setText(_translate("MainWindow", "검색시작"))
        self.pushButton_2.setText(_translate("MainWindow", "종  료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

