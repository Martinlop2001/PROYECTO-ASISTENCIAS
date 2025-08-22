



from servicios import gestion_alumno, gestion_materia, gestion_profesor


def mostrar_menu():

    while True:
        print("\n--- Menu ---")
        print("1. Profesores")
        print("2. Alumnos")
        print("3. Materias")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            gestion_profesor.menu_profesores()
        elif opcion == "2":
            gestion_alumno.menu_alumnos()
        elif opcion == "3":
            gestion_materia.menu_materia()
        elif opcion == "0":
            break