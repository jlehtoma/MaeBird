from PySide.QtCore import Qt
from PySide.QtSql import (QSqlRelationalTableModel, QSqlRelation)

class ModelFactory(object):
    
    def __init__(self):
        self.__models = {FamilyModel.name: FamilyModel,
                         ObservationsModel.name: ObservationsModel,
                         OrderModel.name: OrderModel,
                         SpeciesModel.name: SpeciesModel}
    
    def get_model(self, modelname):
        ''' Dynamic factory / getter method. Model name provided as a parameter
        can (1) return a new model class for instantiation or (2) return a 
        an existing bound class attribute (instance of a model class).    
        '''
        modelname = unicode(modelname)
        try:
            # Model has already been instantiated and bound as an object 
            # attribute
            if modelname in self.__dict__.keys():
                return self.__dict__[modelname]
            # Model has not been instantiated, return a new class for object
            # instantiation
            else:
                model = self.__models[modelname]
                self.__dict__[modelname] = model
                return model
        except KeyError:
            raise NotImplementedError, 'Model %s not implemented' % modelname
    
    @property
    def model_names(self):
        return [unicode(key) for key in self.__models.keys()]

#===============================================================================
#  Custom models
    
class FamilyModel(QSqlRelationalTableModel):
    name = 'family'
    ID = 0
    NAME_FIN = 1
    NAME_SCI = 2
    FORDER = 3
    
    def __init__(self, parent=None): 
        super(FamilyModel, self).__init__(parent)
        
        self.setSort(FamilyModel.ID, Qt.AscendingOrder)
        self.setTable(FamilyModel.name)
        self.setRelation(FamilyModel.FORDER, QSqlRelation('forder', 'ID', 'NAME_FIN'))
        self.setHeaderData(FamilyModel.ID, Qt.Horizontal, "Id")
        self.setHeaderData(FamilyModel.NAME_FIN, Qt.Horizontal, "Finnish name")
        self.setHeaderData(FamilyModel.NAME_SCI, Qt.Horizontal, "Scientific name")
        self.setHeaderData(FamilyModel.FORDER, Qt.Horizontal, "Order")
        self.select()
        
        self.editable = False
        
    def get_data(self, index, language):
        if language.lower() == 'fin':
            return self.data(self.index(index, FamilyModel.NAME_FIN))
        elif language.lower() == 'sci':
            return self.data(self.index(index, FamilyModel.NAME_SCI))
        return None 

class ObservationsModel(QSqlRelationalTableModel):
    name = 'observations'
    # Define column IDs
    ID = 0
    SPECIES = 1
    COUNT = 2
    TIME = 3
    LOCATION = 4
    NOTES = 5
    
    def __init__(self, parent=None): 
        super(ObservationsModel, self).__init__(parent)
        self.setSort(ObservationsModel.ID, Qt.AscendingOrder)
        self.setTable(ObservationsModel.name)
        self.setRelation(ObservationsModel.SPECIES, QSqlRelation('species', 
                                                                 'ID', 
                                                                 'NAME_FIN'))
        self.setHeaderData(ObservationsModel.ID, Qt.Horizontal, "Id")
        self.setHeaderData(ObservationsModel.SPECIES, Qt.Horizontal, "Species")
        self.setHeaderData(ObservationsModel.COUNT, Qt.Horizontal, "Count")
        self.setHeaderData(ObservationsModel.TIME, Qt.Horizontal, "Time")
        self.setHeaderData(ObservationsModel.LOCATION, Qt.Horizontal, 
                           "Location")
        self.setHeaderData(ObservationsModel.NOTES, Qt.Horizontal, "Notes")
        self.select()
        
        self.editable = True
        # Observation model has an associated data model that defines what the
        # observation actually are. For now, observation model only describes 
        # species defined in SpeciesModel
        self.data_model = SpeciesModel()
    
class OrderModel(QSqlRelationalTableModel):
    name = 'forder'
    ID = 0
    NAME_FIN = 1
    NAME_SCI = 2
       
    def __init__(self, parent=None): 
        super(OrderModel, self).__init__(parent)
        self.setSort(OrderModel.ID, Qt.AscendingOrder)
        self.setTable(OrderModel.name)
        self.setHeaderData(OrderModel.ID, Qt.Horizontal, "Id")
        self.setHeaderData(OrderModel.ORDER_FIN, Qt.Horizontal, "Finnish name")
        self.setHeaderData(OrderModel.ORDER_SCI, Qt.Horizontal, "Scientific name")
        self.select()
        
        self.editable = False

    def get_data(self, index, language):
        if language.lower() == 'fin':
            return self.data(self.index(index, OrderModel.NAME_FIN))
        elif language.lower() == 'sci':
            return self.data(self.index(index, OrderModel.NAME_SCI))
        return None 

class SpeciesModel(QSqlRelationalTableModel):
    
    name = 'species'
    ID = 0
    ABBR = 1
    NAME_SCI = 2
    SEMI = 3
    NAME_FIN = 4
    NAME_SWE = 5
    NAME_ENG = 6
    FAMILY = 7
    ELIS = 8
    
    def __init__(self, parent=None):
        super(SpeciesModel, self).__init__(parent)
        self.setSort(SpeciesModel.ID, Qt.AscendingOrder)
        self.setTable(SpeciesModel.name)
        self.setRelation(SpeciesModel.FAMILY, QSqlRelation('family', 'ID', 'NAME_FIN'))
        self.setHeaderData(SpeciesModel.ID, Qt.Horizontal, "Id")
        self.setHeaderData(SpeciesModel.ABBR, Qt.Horizontal, "Abreviation")
        self.setHeaderData(SpeciesModel.NAME_SCI, Qt.Horizontal, "Scientific name")
        self.setHeaderData(SpeciesModel.SEMI, Qt.Horizontal, "Seminatural")
        self.setHeaderData(SpeciesModel.NAME_FIN, Qt.Horizontal, "Finnish name")
        self.setHeaderData(SpeciesModel.NAME_SWE, Qt.Horizontal, "Swedish name")
        self.setHeaderData(SpeciesModel.NAME_ENG, Qt.Horizontal, "English name")
        self.setHeaderData(SpeciesModel.FAMILY, Qt.Horizontal, "Family")
        self.setHeaderData(SpeciesModel.ELIS, Qt.Horizontal, "Seen")
        self.select()
        
        self.editable = False
        
        self.currentrow = None
        
        # Initially sorted by the primary key
        self.__sorted = [Qt.AscendingOrder, -1, -1, -1, -1, -1, -1, -1, -1]
    
    def get_data(self, index, language):
        if language.lower() == 'eng':
            return self.data(self.index(index, SpeciesModel.NAME_ENG))
        elif language.lower() == 'fin':
            return self.data(self.index(index, SpeciesModel.NAME_FIN))
        elif language.lower() == 'sci':
            return self.data(self.index(index, SpeciesModel.NAME_SCI))
        elif language.lower() == 'swe':
            return self.data(self.index(index, SpeciesModel.NAME_SWE))
        return None 
    
    def isSorted(self, index):
        if index in range(0, len(self.__sorted)):
            return self.__sorted[index]
    
    def setSorted(self, index, value):
        if index in range(0, len(self.__sorted)) and value in (Qt.AscendingOrder,
                                                               Qt.DescendingOrder,
                                                               - 1):
            map(lambda x:-1, self.__sorted)
            self.__sorted[index] = value
            
if __name__ == '__main__':
    m = ModelFactory()
    print m.model_names
