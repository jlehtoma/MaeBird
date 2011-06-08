#!/usr/bin/env python2.5

from PySide.QtCore import (Slot, QDateTime, Qt)
from PySide.QtGui import (QCheckBox, QCompleter, QDataWidgetMapper, QDialog,
                          QMessageBox)

from config import DATETIME_FORMAT

from gui.ui_configdialog import Ui_configDialog
from gui.ui_modeldialog import Ui_modelDialog
from gui.ui_infodialog import Ui_infoDialog
from gui.ui_observations import Ui_observationDialog

class ConfigDialog(QDialog, Ui_configDialog):
    
    def __init__(self, saveload, parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.saveloadCheckBox.setChecked(saveload)
        
        fields = []
        for i in range(0, parent.tableView.model().columnCount()):
            fields.append((parent.tableView.model().headerData(i, Qt.Horizontal),
                           parent.tableView.isColumnHidden(i)))
        self.populate_fields(fields)
        
        # Check whether debugging is used
        self.debuggingCheckBox.setChecked(parent.logger.debugging)
        
        # Set the first tab sheet visible
        self.tabWidget.setCurrentIndex(0)
        
    def accept(self):
        QDialog.accept(self)
    
    def hidden_fields(self):
        return [self.fieldLayout.itemAt(i).widget().isChecked() for i in range(self.fieldLayout.count())]
    
    def populate_fields(self, fields):
        for field, hidden in fields:
            item = QCheckBox(self.fieldScrollArea)
            item.setObjectName(field)
            item.setText(field)
            item.setChecked(not hidden)
            self.fieldLayout.addWidget(item)
    
    def saveload_previous(self):
        return self.saveloadCheckBox.isChecked()

class InfoDialog(QDialog, Ui_infoDialog):
    
    def __init__(self, model, index, parent=None):
        super(InfoDialog, self).__init__(parent)
        self.parent = parent
        self.model = model
        self.index = index
        
        self.setupUi(self)
        self.update_ui()
        
    def update_ui(self):
        
        name = '<h1>%s</h1>' % self.model.get_data(self.index, 'fin')
        self.sppCommonLabel.setText(name)
        
        name = '(<i>%s</i>)' % self.model.get_data(self.index, 'sci')
        self.sppSciLabel.setText(name)
        
        lang = self.parent.languages['secondary']
        name = '%s: %s' % (lang, self.model.get_data(self.index, lang))
        self.sppSecLabel.setText(name)

        lang = self.parent.languages['tertiary']
        name = '%s: %s' % (lang, self.model.get_data(self.index, lang))
        self.sppTerLabel.setText(name)

class ModelDialog(QDialog, Ui_modelDialog):
    
    def __init__(self, models, parent=None):
        super(ModelDialog, self).__init__(parent)
        self.setupUi(self)
        self.modelListWidget.addItems(models)
        self.modelListWidget.doubleClicked.connect(self.accept)
        
    def selected_model(self):
        return self.modelListWidget.currentItem().text()
    
class ObservationDialog(QDialog, Ui_observationDialog):
    
    FIRST, PREV, NEXT, LAST, CURRENT = range(5)
    ADD, DELETE, SHOW = range(3)
    
    def __init__(self, model, index, parent=None):
        super(ObservationDialog, self).__init__(parent)
        self.setupUi(self)
        #self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        self.model = model
        self.data_model = model.data_model
        
        # TODO: language for the species name completion needs to be handled
        sppCompleter = QCompleter(self)
        sppCompleter.setModel(self.data_model)
        sppCompleter.setCompletionColumn(4)
        sppCompleter.setCompletionMode(QCompleter.InlineCompletion)
        sppCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.sppLineEdit.setCompleter(sppCompleter)
        
        abbrCompleter = QCompleter(self)
        abbrCompleter.setModel(self.data_model)
        abbrCompleter.setCompletionColumn(1)
        abbrCompleter.setCompletionMode(QCompleter.InlineCompletion)
        self.abbrLineEdit.setCompleter(abbrCompleter)
        
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(model)
        self.mapper.addMapping(self.sppLineEdit, model.SPECIES)
        self.mapper.addMapping(self.countSpinBox, model.COUNT)
        self.mapper.addMapping(self.dateTimeEdit, model.TIME)
        self.mapper.addMapping(self.locLineEdit, model.LOCATION)
        self.mapper.addMapping(self.notesTextEdit, model.NOTES)
        self.mapper.setCurrentModelIndex(index)
        
        self.firstButton.clicked.connect(
                            lambda: self.saveRecord(ObservationDialog.FIRST))
        self.prevButton.clicked.connect(
                            lambda: self.saveRecord(ObservationDialog.PREV))
        self.nextButton.clicked.connect(
                            lambda: self.saveRecord(ObservationDialog.NEXT))
        self.lastButton.clicked.connect(
                            lambda: self.saveRecord(ObservationDialog.LAST))
        self.saveButton.clicked.connect(
                            lambda: self.saveRecord(ObservationDialog.CURRENT))
        self.closeButton.clicked.connect(self.reject)
        
    def addRecord(self):
        row = self.model.rowCount()    
        self.mapper.submit()
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        now = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(now)
        self.sppLineEdit.setFocus()

    def deleteRecord(self):
        species = self.sppLineEdit.text()
        obstime = self.dateTimeEdit.dateTime().toString(
                                            DATETIME_FORMAT)
        if (QMessageBox.question(self,
                "Delete",
                "Delete observation of <br>%s on %s?" % (species, obstime),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        row = self.mapper.currentIndex()
        self.model.removeRow(row)
        self.model.submitAll()
        if row + 1 >= self.model.rowCount():
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        
#    def reject(self):
#        self.accept()

    def accept(self):
        
        self.mapper.submit()
        QDialog.accept(self)
    
    def saveRecord(self, where):
        
        if self.sppLineEdit.text() == "":
            QMessageBox.warning(self, "Warning",
                "You must enter a species name!", QMessageBox.Ok)
            return
        row = self.mapper.currentIndex()
        self.mapper.submit()
        if where == ObservationDialog.FIRST:
            row = 0
        elif where == ObservationDialog.PREV:
            row = 0 if row <= 1 else row - 1
        elif where == ObservationDialog.NEXT:
            row += 1
            if row >= self.model.rowCount():
                row = self.model.rowCount() - 1
        elif where == ObservationDialog.LAST:
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)
    
    @Slot()    
    def on_sppLineEdit_editingFinished(self):
        '''Called when editing of the sppLineEdit stops, etc. species name input
        is complete. Species name will be searched from the model and corresponding
        abbreviation string and ID number will be set.'''
            
        row = self.mapper.currentIndex()
        item = self.sppLineEdit.text()
        
        match =  self.model.match(self.model.index(0, 2),
                                       Qt.DisplayRole,
                                       item,
                                       hits=1,
                                       flags=Qt.MatchExactly)
        if match:
            print match