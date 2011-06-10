#!/usr/bin/env python2.5

# Standard imports
import platform
import os, sys

# PySide imports

import PySide
from PySide.QtCore import (Slot, QFile, QSettings, Qt, QTimer)
from PySide.QtGui import (QApplication, QColor, QFileDialog, 
                         QIcon, QMainWindow, QMessageBox, QPalette, QTableView)
from PySide.QtSql import (QSqlDatabase, QSqlRelationalDelegate)

# MaeBird imports
from config import (__APPNAME__, __DB__, __ORG__, __ORGDOMAIN__, 
                    __USER_DATA_DIR__,  __VERSION__)
from gui.dialogs import (ConfigDialog, ModelDialog, ObservationDialog)
from gui.ui_mainwindow import Ui_MainWindow
from maebird.mblogging import Logger

from models import ModelFactory

class MaeBird(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MaeBird, self).__init__(parent)
        
        self.models = ModelFactory()

        self.table = None
        self.languages = {'perimary': 'Fin', 'secondary': 'Eng', 
                         'tertiary': 'Swe'}
        
        self.dbtype = __DB__
        self.dbfile = None
        self.db = None
        
        self.matches = []
        self.currentsearchitem = 0
        
        self.fullscreen = False
        self.setupUi(self)
        
        self.setWindowTitle(__APPNAME__ + ' ' + __VERSION__)
        
        
        # TODO: loading settings should be moved to a separate method
        settings = QSettings()
        
        # Set up logging
        loggingdir = settings.value("Logging/loggingDir")
        if loggingdir == "":
            loggingdir = __USER_DATA_DIR__
        self.logger = Logger('root', loggingdir=loggingdir)
        if settings.value("Settings/debugging"):
            self.logger.debugging = int(settings.value("Settings/debugging"))
            self.logger.debug('Logging initialized')
        
        # Try to load previous session
        if settings.value("Settings/saveSettings"):
            self.saveSettings = int(settings.value("Settings/saveSettings"))
        else:
            self.saveSettings = 1
                      
        if self.saveSettings:
            QTimer.singleShot(0, self.load_initial_data)
            #QTimer.singleShot(0, self.load_initial_model)
        
        self.header = self.tableView.horizontalHeader()
        self.header.sectionDoubleClicked.connect(self.sort_table)
        
        self.search.textEdited.connect(self.update_ui)
        self.search.setFocus()
        self.searchNextButton.clicked.connect(self.update_ui)
        self.searchPrevButton.clicked.connect(self.update_ui)
        
        self.tableView.pressed.connect(self.update_ui)
        
        self.tableView.doubleClicked.connect(
                    lambda: self.handle_observation(ObservationDialog.SHOW))
        self.addButton.clicked.connect(
                    lambda: self.handle_observation(ObservationDialog.ADD))
        self.deleteButton.clicked.connect(
                    lambda: self.handle_observation(ObservationDialog.DELETE))
    
    def closeEvent(self, event):
        settings = QSettings()
        if self.saveSettings:
            db = self.dbfile if self.db is not None else ''
            settings.setValue("Database/LastDb", db)
            
            if self.tableView.model() is not None:
                settings.setValue("Database/DefaultModel", self.tableView.model().name)
            
                visible_fields = [not bool(self.tableView.isColumnHidden(i)) for i in range(0, self.tableView.model().columnCount())]
                settings.setValue("Database/visibleFields", visible_fields)
            settings.setValue("Settings/debugging", int(self.logger.debugging))
        
        settings.setValue("Settings/saveSettings", int(self.saveSettings))
    
    def load_initial_data(self):
        settings = QSettings()
        dbfile = unicode(settings.value("Database/LastDb"))
        modelname = unicode(settings.value("Database/DefaultModel"))
        if dbfile and QFile.exists(dbfile):
            self.load_db(dbfile, modelname=modelname)
            self.logger.debug("Loaded database %s with model %s" % (dbfile,
                                                                     modelname))
        
        if settings.value("Database/visibleFields"):
            visible_fields = [item for item in settings.value("Database/visibleFields")]
        
            # FIXME: in absence of QVariant, deal with values
            visible_fields = [False if item == 'false' else True for item in visible_fields]
            if not all(visible_fields):
                self.logger.debug("Hiding fields %s" % visible_fields)
            self.show_fields(visible_fields)

    def load_db(self, dbname, modelname=None):
        self.db = QSqlDatabase.addDatabase(self.dbtype)
        self.db.setDatabaseName(dbname)
        if not self.db.open():
            QMessageBox.warning(self, "Batabase connection",
                "Database Error: %s" % (self.db.lastError().text()))
            return
        self.dbfile = dbname
        
        if modelname not in self.models.model_names:
            modeldlg = ModelDialog(self.models.model_names)
            if modeldlg.exec_():
                modelname = modeldlg.selected_model()
        
        if modelname:
            self.load_model(modelname)
    
    def load_model(self, modelname):
        ''' Loads a specific database model and sets it to view.  
        '''
        try:
            model = self.models.get_model(modelname)
        except NotImplementedError, e:
            QMessageBox.warning(self, "Database model",
                "Database Model Error: %s" % str(e))
            return
        self.tableView.setModel(model(self))
        self.tableView.setItemDelegate(QSqlRelationalDelegate(self))
        self.tableView.setSelectionMode(QTableView.SingleSelection)
        self.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.tableView.setColumnHidden(0, True)
        self.tableView.resizeColumnsToContents()
        self.update_ui()
        
    @Slot()     
    def on_actionAbout_triggered(self):
        QMessageBox.about(self, "About MaeBird",
                          """<b>MaeBird</b> v %s
                             <p>Copyright &copy; 2010 Joona Lehtomaki.
                            All rights reserved.
                            <p>For keen, not so talented birders.
                            <p>Python %s - Qt %s - PySide %s on %s""" % (
                            __VERSION__, platform.python_version(),
                            PySide.QtCore.__version__, 
                            PySide.__version__, platform.system()))
        
    @Slot()   
    def on_actionLoadDb_triggered(self):
        infile = unicode(QFileDialog.getOpenFileName(self,
                                                    self.trUtf8("Select input database"),
                                                    "./data",
                                                    self.trUtf8("*.*"))[0]) 
        
        if infile:
            self.load_db(infile)
    
    @Slot()   
    def on_actionProperties_triggered(self):
        dialog = ConfigDialog(self.saveSettings, parent=self)
        if dialog.exec_():
            self.saveSettings = dialog.saveload_previous()
            self.show_fields(dialog.hidden_fields())
            self.logger.debugging = dialog.debuggingCheckBox.isChecked()
            
    @Slot()
    def on_actionSelectTable_triggered(self):
        modeldlg = ModelDialog(self.models.model_names)
        if modeldlg.exec_():
            modelname = modeldlg.selected_model()
        
        if modelname:
            self.load_model(modelname)
        
    @Slot()
    def on_fullscreenToggle_clicked(self):
        if not self.fullscreen:
            self.showFullScreen()
            self.fullscreen = True
            self.fullscreenToggle.setIcon(QIcon(':/icons/image40b.png'))
        else:
            self.showNormal()
            self.fullscreen = False
            self.fullscreenToggle.setIcon(QIcon(':/icons/image40.png'))

    def handle_observation(self, operation):
        
        model = self.tableView.model()
        obsdlg = ObservationDialog(model,
                                   self.tableView.currentIndex())
        
        if operation == ObservationDialog.ADD:
            obsdlg.addRecord()
        elif operation == ObservationDialog.DELETE:
            obsdlg.deleteRecord()
        if operation == ObservationDialog.ADD or \
            operation == ObservationDialog.SHOW:
            if obsdlg.exec_():
                pass
        self.update_ui()
    
    @Slot(str)
    def on_search_textEdited(self, txt):
        self.matches = []
        model = self.tableView.model()
        if not model:
            return
        palette = self.search.palette()

        for i in range(0, model.columnCount()):
            if not self.tableView.isColumnHidden(i):
                matches = model.match(model.index(0, i),
                                           Qt.DisplayRole,
                                           txt,
                                           hits=-1,
                                           flags=Qt.MatchContains)
                [self.matches.append(match) for match in matches]
        
        if self.matches:
            self.currentsearchitem = 0
            palette.setColor(QPalette.Active, QPalette.Base,
                             QColor(255, 255, 255))
            self.set_search_item(self.matches[self.currentsearchitem])
        else:
            palette.setColor(QPalette.Active, QPalette.Base,
                             QColor(255, 64, 64))
        self.search.setPalette(palette)
       
    @Slot()
    def on_searchNextButton_clicked(self):
        if self.currentsearchitem < len(self.matches) - 1:
            self.currentsearchitem += 1
            self.set_search_item(self.matches[self.currentsearchitem])
    
    @Slot()
    def on_searchPrevButton_clicked(self):
        if self.currentsearchitem > 0:
            self.currentsearchitem -= 1
            self.set_search_item(self.matches[self.currentsearchitem])
    
    def set_search_item(self, index):
        self.tableView.setCurrentIndex(index)
        
    def set_model_to_view(self, model):
        self.tableView.setModel(model)
        self.tableView.setItemDelegate(QSqlRelationalDelegate(self))
        self.tableView.setSelectionMode(QTableView.SingleSelection)
        self.tableView.setSelectionBehavior(QTableView.SelectRows)
        self.tableView.setColumnHidden(0, True)
        self.tableView.resizeColumnsToContents()
        
    def show_fields(self, visible):
        for i, not_hidden in enumerate(visible):
            if not not_hidden:
                self.tableView.hideColumn(i)
            else:
                self.tableView.showColumn(i)
  
    def sort_table(self, index):
        model = self.tableView.model()
        if model.isSorted(index) == Qt.AscendingOrder:
            model.setSort(index, Qt.DescendingOrder)
            model.setSorted(index, Qt.DescendingOrder)
        else:
            model.setSort(index, Qt.AscendingOrder)
            model.setSorted(index, Qt.AscendingOrder)
            
        model.select()
            
    def update_ui(self):
        
        if len(self.matches) - self.currentsearchitem > 1:
            
            self.searchNextButton.setEnabled(True)
        else:
            self.searchNextButton.setEnabled(False)
        if self.currentsearchitem > 0:
            self.searchPrevButton.setEnabled(True)
        else:
            self.searchPrevButton.setEnabled(False)
        
        if self.tableView.model().editable:
            self.addButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)
            
        if (self.tableView.model().editable and 
                                    self.tableView.currentIndex().row() > -1):
            self.deleteButton.setEnabled(True)
        else:
            self.deleteButton.setEnabled(False)
                    
def main(args):
    app = QApplication(args)
    app.setApplicationName(__APPNAME__)
    app.setApplicationVersion(__VERSION__)
    app.setOrganizationName(__ORG__)
    app.setOrganizationDomain(__ORGDOMAIN__)
    mainwindow = MaeBird()
    mainwindow.show()
    app.exec_()
    del mainwindow

if __name__ == '__main__':
    main(sys.argv)

