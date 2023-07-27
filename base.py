import sqlite3
import os
#Esta clase solo crea el la base de datos donde se van almacenar la tabla de contenido
#No busca una tabla en especifico solo inserta la hora de la busqueda y los archivos buscados por openai
#Este codigo fue creado por xelastone

class datos:
    def __int__(self,db='data_openai.db'):
        self.conexion=sqlite3.connect(db)
        self.cursor=self.conexion.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS OpenAI(id INTEGR UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,Fecha TEXT,Informacion TEXT)')
        self.conexion.commit()

    def insert(self,tiempo,busqueda):
        self.cursor.execute('''INSERT INTO OpenAI VALUES(NULL,?,?)''',(self.tiempo,self.busqueda))
        self.conexion.commit()
    def leer(self,tiempo,busqueda):
        self.cursor.execute('''SELECT FROM * OpenAI''')
        self.conexion.commit()

        self.conexion.commit()
