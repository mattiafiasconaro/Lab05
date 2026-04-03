# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import  DBConnect
from model.corso import Corso

class corso_DAO():

    @staticmethod
    def getAllCorsi():
        cnx=DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query="""select nome,codins from corso"""
        cursor.execute(query)

        res=[]

        for row in cursor:
            res.append(row)


        cursor.close()
        cnx.close()
        return res

