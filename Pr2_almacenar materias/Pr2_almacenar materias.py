print(" ")
print("Alvaro Campechano Estrada 3W")
print(" ")
 # Definimos una lista con las materias del curso
materias = [
    "Pensamiento matemático",
    "Español",
    "Inglés",
    "Química",
    "Civismo",
    "Francés"
]

# Función para mostrar las materias
def mostrar_materias(lista_materias):
    print("Materias del curso:")
    for materia in lista_materias:
        print(f"- {materia}")

# Llamamos a la función para mostrar las materias
mostrar_materias(materias)
