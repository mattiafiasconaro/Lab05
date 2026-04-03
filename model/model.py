from database.studente_DAO import studente_DAO
from database.corso_DAO import corso_DAO



class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return corso_DAO.getAllCorsi()

    def getAllIscritti(self):
        return studente_DAO.getAllIscritti()

    def getcercaStudente(self):
        return studente_DAO.getcercaStudente()

    def getCercaCorsiIscritto(self):
        return studente_DAO.getCercaCorsiIscritto()

    def getIscriviti(self,matricola,codins):
        return studente_DAO.getIscriviti(matricola,codins)

