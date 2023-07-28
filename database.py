import sqlite3
from os import path, getcwd

#Esta clase Crea la tabla de contenido de la base de datos
#Las metodos de clase de db son para insertar los valores en la tabla openAI
#x3l4-s7on3
class db:
    def __init__(self, db='DatosOpenAI.db'):
        self.conn = sqlite3.connect(path.join(os.getcwd(), "db", db))
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS openAI (
            id	INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
            fecha	TEXT,
            datos       TEXT
        )
        """)
        self.conn.commit()
#Este metodo de clase inserta los valores a la tabla llamada openAI
    def insertar(self, var1,var2):
        self.cur.execute(
            "INSERT INTO openAI VALUES (NULL, ?,?)", (var1,var2))
        self.conn.commit()
        return True

    def ver(self):
        self.cur.execute("SELECT * FROM openAI")
        rows = self.cur.fetchall()
        return rows

    def buscarId(self, id):
        self.cur.execute("SELECT * FROM openAI WHERE id=?", (id,))
        rows = self.cur.fetchall()
        return rows
#
    def Buscar(self,var1,var2):
        self.cur.execute(
            "SELECT * FROM openAI WHERE =? fecha=? OR  datos=?", (var1, var2))
        rows = self.cur.fetchall()
        return rows
        pass
    def eliminar(self, id):
        self.cur.execute("DELETE FROM openAI WHERE id=?", (id,))
        self.conn.commit()
        return True

    def __del__(self):
        self.conn.close()
