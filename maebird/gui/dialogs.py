#!/usr/bin/env python2.5

from PySide.QtCore import (Slot, QDateTime, Qt)
from PySide.QtGui import (QCheckBox, QCompleter, QDataWidgetMapper, QDialog,
                          QMessageBox)

from config import DATETIME_FORMAT

from gui.ui_configdialog import Ui_configDialog
from gui.ui_modeldialog import Ui_modelDialog
from gui.ui_infodialog import Ui_infoDialog
from gui.ui_observations import Ui_observationDialog

from mblogging import Logger

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
        self.logger.info('Debug set to: %s' % str(parent.logger.debugging))
        
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
    
    ''' A dialog delegate that handles the displaying of the observation model
    in a suitable GUI dialog.
    '''
    
    FIRST, PREV, NEXT, LAST, CURRENT = range(5)
    ADD, DELETE, SHOW = range(3)
    
    def __init__(self, model, index, parent=None):
        super(ObservationDialog, self).__init__(parent)
        
        self.logger = Logger('root.observationDialog')
        self.logger.debug('Debug set to: %s' % str(parent.logger.debugging))
        
        self.setupUi(self)
#        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        # An observation model is passed to the constructor as a parameter
        self.model = model
        
        # Build a QCompleter that is based on a species model's species name.
        # This way user can start typing the name in a line edit and the 
        # completion will suggest suitable species names based on the model
        
        # TODO: language for the species name completion needs to be handled
        # TODO: both completers have model column indexes hard coded in, thus
        # they will break if the model is modified
        sppCompleter = QCompleter(self)
        sppCompleter.setModel(self.model.data_model)
        sppCompleter.setCompletionColumn(4)
        sppCompleter.setCompletionMode(QCompleter.InlineCompletion)
        sppCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.sppLineEdit.setCompleter(sppCompleter)
        
        # Build a QCompleter that is based on a species model's abbreviation.
        # This way user can start typing the abbreviation in a line edit and the 
        # completion will suggest suitable species names based on the model
        abbrCompleter = QCompleter(self)
        abbrCompleter.setModel(self.model.data_model)
        abbrCompleter.setCompletionColumn(1)
        abbrCompleter.setCompletionMode(QCompleter.InlineCompletion)
        self.abbrLineEdit.setCompleter(abbrCompleter)
        
        # The underlying (observation) model is automatically updated through 
        # a QDataWidgetMapper
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(model)
        # ID is mapped to a disabled dummy label in order to include it in the
        # WidgetMapper --> not very elegant
        self.mapper.addMapping(self.idLineEdit, model.ID)
        self.mapper.addMapping(self.sppLineEdit, model.SPECIES)
        self.mapper.addMapping(self.abbrLineEdit, model.ABBR)
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
        
        self.sppLineEdit.editingFinished.connect(self.update_fields)
        
    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        
        now = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(now)
        self.sppLineEdit.setFocus()
        self.mapper.setCurrentIndex(row)

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
        
    def reject(self):
        QDialog.reject(self)

    def accept(self):
        self.mapper.submit()
        QDialog.accept(self)
    
    def saveRecord(self, where):
        ''' Method saves the current row in the self.mapper and moves the 
        data model cursor to a given location.
        '''
        
        if self.sppLineEdit.text() == "":
            QMessageBox.warning(self, "Warning",
                "You must enter a species name!", QMessageBox.Ok)
            return
        
        # Get the current index and submit changes to the underlying model
        row = self.mapper.currentIndex()
        self.mapper.submit()
        
        # Move the data model cursor to a given location
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

    def update_fields(self):
        '''Called when editing of the sppLineEdit stops, etc. species name input
        is complete. Species name will be searched from the model and 
        corresponding abbreviation string and ID number will be set.'''
        item = self.sppLineEdit.text()
        item = item.capitalize()
        # Match the user entered name to an abbreviation in the species model        
        matches =  self.model.data_model.match(self.model.data_model.index(0, 4),
                                               Qt.DisplayRole,
                                               item,
                                               hits=1,
                                               flags=Qt.MatchExactly)
        if matches:
            # There should be only one match
            match_row = matches[0].row()
            abbreviation = self.model.data_model.index(match_row, 
                                            self.model.data_model.ABBR).data()
            # Also get the ID for updating the model
            id = self.model.data_model.index(match_row, 
                                            self.model.data_model.ID).data()
            self.abbrLineEdit.setText(abbreviation)