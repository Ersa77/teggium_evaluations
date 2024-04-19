def guardar_valores(**kwargs):
    nombre = kwargs.get("nombre", None)
    edad = kwargs.get("edad", None)
    ciudad = kwargs.get("ciudad", None)

    # Hacer algo con las variables
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Ciudad:", ciudad)

# Ejemplo de uso
nombre = "Eros"
edad = 24
ciudad = "Queretaro"
guardar_valores(nombre = nombre, edad = edad, ciudad = ciudad)