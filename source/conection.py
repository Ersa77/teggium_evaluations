import sqlite3
from PyQt5.QtWidgets import QLabel, QComboBox
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
                    WHERE username = ?;""", (username,))
    resultado= cursor.fetchone()
    nombre= resultado[0]
    rol= resultado[1]
    return nombre, rol

def llenar_campaings(self):
        cursor.execute("SELECT name_campaign FROM campaigns;")
        resultados= cursor.fetchall()
        for resultado in resultados:
            self.campania.addItem(resultado[0])

def llenar_supervisor(self, campaign):
     self.supervisor.addItem("-Seleccionar-",0)
     cursor.execute("""
                    SELECT nombre_supervisor FROM supervisores 
                    JOIN campaigns USING (id_campaign)
                    WHERE name_campaign = ?""", (campaign,))
     resultados= cursor.fetchall()
     for resultado in resultados:
          self.supervisor.addItem(resultado[0])

def llenar_analistas(self, campaign, supervisor):
     self.analyst_name.addItem("-Seleccionar-", 0)
     cursor.execute("""
                    SELECT name_anaylst FROM pt_anaylst_teggium 
                    JOIN supervisores USING (id_supervisor)
                    JOIN campaigns USING (id_campaign) 
                    WHERE name_campaign = ?
                    AND nombre_supervisor = ?""", (campaign,supervisor))
     resultados= cursor.fetchall()
     for resultado in resultados:
          self.analyst_name.addItem(resultado[0])

def llenar_tipos_evaluaciones(self):
     self.tipo_evaluacion.addItem("-Seleccionar-",0)
     cursor.execute("SELECT tipo_evaluacion FROM tipos_evaluaciones")
     resultados= cursor.fetchall()
     for resultado in resultados:
          self.tipo_evaluacion.addItem(resultado[0])

def llenar_activity(self):
     self.activity.addItem("-Seleccionar-",0)
     cursor.execute("SELECT nombre_proceso FROM procesos_pt;")
     resultados= cursor.fetchall()
     for resultado in resultados:
          self.activity.addItem(resultado[0])
        
def llenar_evaluador(self):
     self.analista_calidad.addItem("-Seleccionar-",0)
     cursor.execute("SELECT name_aud FROM auditores_calidad WHERE id_rol = 1;")
     #los id_rol:
     #1 analista calidad (evaluador)
     #2 desarrollador
     #3 supervisor
     #4 gerente
     resultados= cursor.fetchall()
     for resultado in resultados:
          self.analista_calidad.addItem(resultado[0])

def traer_preguntas(self, proceso_pt):
     cursor.execute("""
                    SELECT id_pregunta, pregunta, ponderacion, tipo_pregunta
                    FROM preguntas
                    JOIN procesos_pt USING (id_proceso)
                    JOIN tipos_preguntas USING (id_tipo_pregunta)
                    WHERE nombre_proceso = ?
                    AND (tipo_pregunta = 'Calidad de atención' OR tipo_pregunta= 'Proceso')""", (proceso_pt,))
     resultados= cursor.fetchall()
     return resultados

def traer_desviaciones(self, proceso_pt):
     cursor.execute("""
                    SELECT id_pregunta, pregunta, ponderacion, tipo_pregunta
                    FROM preguntas
                    JOIN procesos_pt USING (id_proceso)
                    JOIN tipos_preguntas USING (id_tipo_pregunta)
                    WHERE nombre_proceso = ?
                    AND (tipo_pregunta = 'Errores operativos' OR tipo_pregunta= 'Desviaciones graves')""", (proceso_pt,))
     resultados= cursor.fetchall()
     return resultados
def obtenerEvaluacionID(self):
     cursor.execute("""
                    SELECT MAX(id_evaluacion) AS "ID_EVALUACION" FROM respuestas""")
     evaluacionID= cursor.fetchall()
     numero = evaluacionID[0][0] if evaluacionID else None
     return numero

def insertar_cosas(self, id_evaluacion,analyst, siniestro, fecha_evaluacion, tipo_evaluacion, proceso, evaluadora, pregunta, respuesta, sla, comentario, resultado):
     cursor.execute("""
                    INSERT INTO respuestas (id_evaluacion,id_campaign, id_supervisor, id_user, no_siniestro, fecha_evaluacion, id_tipo, id_proceso, id_aud, id_pregunta, respuesta, sla, comentarios, resultado_final)
                    VALUES (?,
                         (
                         SELECT id_campaign 
                         FROM pt_anaylst_teggium
                         WHERE name_anaylst = ?
                         ),
                         (
                         SELECT id_supervisor 
                         FROM pt_anaylst_teggium
                         WHERE name_anaylst = ?
                         ),
                         (
                         SELECT id_user 
                         FROM pt_anaylst_teggium 
                         WHERE name_anaylst = ?
                         ),
                    --NO SINIESTRO, FECHA EVALUACION
                         ?,
                         ?,
                         (
                         SELECT id_tipo 
                         FROM tipos_evaluaciones 
                         WHERE tipo_evaluacion = ?
                         ),
                         (
                         SELECT id_proceso 
                         FROM procesos_pt
                         WHERE nombre_proceso = ?
                         ),
                         (
                         SELECT id_aud 
                         FROM auditores_calidad
                         WHERE name_aud = ?
                         ),
                         (
                         SELECT id_pregunta 
                         FROM preguntas 
                         WHERE pregunta = ?
                         AND id_proceso =	(SELECT id_proceso 
                                                  FROM procesos_pt
                                                  WHERE nombre_proceso = ?)
                         ),
                    --RESPUESTA, SLA, COMENTARIO, RESULTADO FINAL
                         ?, ?, ?, ?)""",\
                    (id_evaluacion,analyst, analyst, analyst, siniestro, fecha_evaluacion, tipo_evaluacion, proceso, evaluadora, pregunta, proceso, respuesta, sla, comentario, resultado))
     conexion.commit()