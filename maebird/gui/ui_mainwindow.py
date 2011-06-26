# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/mainwindow.ui'
#
# Created: Sun Jun 26 21:46:33 2011
#      by: pyside-uic 0.2.10 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centralLayout = QtGui.QVBoxLayout()
        self.centralLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.centralLayout.setObjectName("centralLayout")
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setEnabled(True)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.centralLayout.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.centralLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.searchPrevButton = QtGui.QToolButton(self.centralwidget)
        self.searchPrevButton.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/image34.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchPrevButton.setIcon(icon)
        self.searchPrevButton.setObjectName("searchPrevButton")
        self.horizontalLayout.addWidget(self.searchPrevButton)
        self.search = QtGui.QLineEdit(self.centralwidget)
        self.search.setText("")
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.searchNextButton = QtGui.QToolButton(self.centralwidget)
        self.searchNextButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/image39.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchNextButton.setIcon(icon1)
        self.searchNextButton.setObjectName("searchNextButton")
        self.horizontalLayout.addWidget(self.searchNextButton)
        self.deleteButton = QtGui.QToolButton(self.centralwidget)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/image50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.addButton = QtGui.QToolButton(self.centralwidget)
        self.addButton.setEnabled(False)
        self.addButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/image32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon3)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.fullscreenToggle = QtGui.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/image40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fullscreenToggle.setIcon(icon4)
        self.fullscreenToggle.setObjectName("fullscreenToggle")
        self.horizontalLayout.addWidget(self.fullscreenToggle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionLoadDb = QtGui.QAction(MainWindow)
        self.actionLoadDb.setObjectName("actionLoadDb")
        self.actionSelectTable = QtGui.QAction(MainWindow)
        self.actionSelectTable.setObjectName("actionSelectTable")
        self.menuHelp.addAction(self.actionLoadDb)
        self.menuHelp.addAction(self.actionSelectTable)
        self.menuHelp.addAction(self.actionProperties)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MaeBird", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchPrevButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.searchNextButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.fullscreenToggle.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("MainWindow", "P&roperties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadDb.setText(QtGui.QApplication.translate("MainWindow", "&Load database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadDb.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectTable.setText(QtGui.QApplication.translate("MainWindow", "&Select table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectTable.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))

import maebird_rc
