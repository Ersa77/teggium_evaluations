import os
import sqlite3
#Esta funcion es para establecer la conexión a la base de datos
def crear_conexion():
    conexion = sqlite3.connect('database/mybd')
    return conexion
