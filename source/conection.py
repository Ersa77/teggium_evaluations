import sqlite3
#Establecer la conexión a la base de datos
conexion = sqlite3.connect('database/mybd')
cursor = conexion.cursor()

#Funcion para llamar al cursor en otros archivos (ya se, se ve redundante, pero ahorita me quiero centrar en las consultas equisde :v)
def crear_conexion():
    conexion = sqlite3.connect('database/mybd')
    return conexion

#Funcion (y primera prueba) para consultar el nombre del analista segun su username uwu
def usuario_analista_evaluador(username):
    cursor.execute("""
                    SELECT name_aud, nombre_rol 
                    FROM auditores_calidad e
                    JOIN roles d USING (id_rol)
                    WHERE username = ?""", (username,))
    resultado= cursor.fetchone()

    nombre=resultado[0]
    rol= resultado[1]
    return nombre, rol


