# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBConnect



class studente_DAO():
    @staticmethod
    def getAllIscritti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.nome,s.cognome,s.matricola,c.codins
                from corso c, studente s,iscrizione i
                where i.matricola =s.matricola  and c.codins =i.codins """

        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getcercaStudente():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.matricola,s.nome ,s.cognome, c.codins
                from studente s, corso c, iscrizione i
                where i.matricola =s.matricola and c.codins =i.codins 
                group by s.matricola, s.nome,s.cognome, c.codins  """

        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCercaCorsiIscritto():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select i.matricola, c.codins, c.nome AS nomeCorso, s.cognome, s.nome
                from iscrizione i , corso c, studente s
                where i.codins = c.codins and i.matricola=s.matricola
                group by i.matricola, c.codins, c.nome , s.cognome """

        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCercaCorsiIscritto():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """"""
        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res