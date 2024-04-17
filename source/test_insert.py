from conection import crear_conexion
conect = crear_conexion()
cursor = conect.cursor()

cursor.execute("""
INSERT INTO respuestas (id_campaign, id_supervisor, id_user, no_siniestro, fecha_evaluacion, id_tipo, id_proceso, id_aud, id_pregunta, respuesta, sla, comentarios)
VALUES (
	(
	SELECT id_campaign 
	FROM pt_anaylst_teggium
	WHERE id_user = '00000001'
	),
	(
	SELECT id_supervisor 
	FROM pt_anaylst_teggium
	WHERE id_user = '00000001'
	),
	'00000001',
--NO SINIESTRO, FECHA EVALUACION
	'23454367',
	'15-04-2024',
	(
	SELECT id_tipo 
	FROM tipos_evaluaciones
	WHERE tipo_evaluacion = 'General'
	),
	(
	SELECT id_proceso 
	FROM procesos_pt
	WHERE nombre_proceso = 'Validación documental para personas físicas'
	),
	(
	SELECT id_aud 
	FROM auditores_calidad
	WHERE name_aud = 'Andrea Vazquez Vazquez'
	),
	(
	SELECT id_pregunta 
	FROM preguntas 
	WHERE pregunta = 'Identificación oficial'
	AND id_proceso = 1
	),
--RESPUESTA, SLA, COMENTARIO
	'Si', 'Dentro', 'Echele ganas mijo')

""")
