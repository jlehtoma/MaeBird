# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/configdialog.ui'
#
# Created: Sun Jun 26 21:46:33 2011
#      by: pyside-uic 0.2.10 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_configDialog(object):
    def setupUi(self, configDialog):
        configDialog.setObjectName("configDialog")
        configDialog.resize(451, 365)
        self.horizontalLayout = QtGui.QHBoxLayout(configDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtGui.QScrollArea(configDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 348, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.settingsTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.saveloadCheckBox = QtGui.QCheckBox(self.settingsTab)
        self.saveloadCheckBox.setObjectName("saveloadCheckBox")
        self.verticalLayout_5.addWidget(self.saveloadCheckBox)
        self.debuggingCheckBox = QtGui.QCheckBox(self.settingsTab)
        self.debuggingCheckBox.setObjectName("debuggingCheckBox")
        self.verticalLayout_5.addWidget(self.debuggingCheckBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.tabWidget.addTab(self.settingsTab, "")
        self.selectionTab = QtGui.QWidget()
        self.selectionTab.setObjectName("selectionTab")
        self.tabWidget.addTab(self.selectionTab, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableLayout = QtGui.QVBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.verticalLayout_7.addLayout(self.tableLayout)
        self.tabWidget.addTab(self.tab, "")
        self.fieldsTab = QtGui.QWidget()
        self.fieldsTab.setObjectName("fieldsTab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.fieldsTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fieldScrollArea = QtGui.QScrollArea(self.fieldsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldScrollArea.sizePolicy().hasHeightForWidth())
        self.fieldScrollArea.setSizePolicy(sizePolicy)
        self.fieldScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.fieldScrollArea.setWidgetResizable(True)
        self.fieldScrollArea.setObjectName("fieldScrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 306, 258))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.fieldLayout = QtGui.QVBoxLayout()
        self.fieldLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.fieldLayout.setObjectName("fieldLayout")
        self.verticalLayout_6.addLayout(self.fieldLayout)
        self.fieldScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.fieldScrollArea)
        self.tabWidget.addTab(self.fieldsTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(configDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(configDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), configDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), configDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(configDialog)

    def retranslateUi(self, configDialog):
        configDialog.setWindowTitle(QtGui.QApplication.translate("configDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.saveloadCheckBox.setText(QtGui.QApplication.translate("configDialog", "Save/Load database and table on startup", None, QtGui.QApplication.UnicodeUTF8))
        self.debuggingCheckBox.setText(QtGui.QApplication.translate("configDialog", "Show debugging messages", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("configDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectionTab), QtGui.QApplication.translate("configDialog", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("configDialog", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("configDialog", "Show/hide fields", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fieldsTab), QtGui.QApplication.translate("configDialog", "Fields", None, QtGui.QApplication.UnicodeUTF8))

