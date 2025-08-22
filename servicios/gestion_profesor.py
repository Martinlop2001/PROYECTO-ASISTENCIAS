


from modelos.profesor import Profesor
from db.conexion import conexion, cursor


def menu_profesores():
    while True:
        print("\n--- Gestión de Profesores ---")
        print("1. Agregar profesor")
        print("2. Listar profesores")
        print("3. Editar profesor")
        print("4. Eliminar profesor")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_profesor()
        elif opcion == "2":
            listar_profesor()
        elif opcion == "3":
            editar_profesor()
        elif opcion == "4":
            eliminar_profesor()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")



def agregar_profesor():
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    dni = int(input("DNI: "))

    profesor = Profesor(nombre, apellido, correo, dni)

    cursor.execute("""
            INSERT INTO profesores (nombre, apellido, correo, dni)
            VALUES (?, ?, ?, ?)
        """, (profesor.nombre, profesor.apellido, profesor.correo, profesor.dni))
    
    conexion.commit()
    print("Profesor agregado correctamente.")



def listar_profesor():
    cursor.execute("SELECT * FROM profesores")
    profesores = cursor.fetchall()
    if not profesores:
        print("No hay profesores registrados.")
    else:
        print("\nLista de profesores:")
        for prof in profesores:
            print(f"ID: {prof[0]} | Nombre: {prof[1]} | Apellido: {prof[2]} | Correo: {prof[3]} | DNI: {prof[4]}")



def editar_profesor():
    id_profesor = input("Ingrese el ID del profesor a editar: ")
    cursor.execute("SELECT * FROM profesores WHERE id = ?", (id_profesor,))
    profesor = cursor.fetchone()
    if not profesor:
        print("No se encontró un profesor con ese ID.")
        return

    print("Deje en blanco para mantener el valor actual.")
    nuevo_nombre = input(f"Nombre actual ({profesor[1]}): ") or profesor[1]
    nuevo_apellido = input(f"Apellido actual ({profesor[2]}): ") or profesor[2]
    nuevo_correo = input(f"Correo actual ({profesor[3]}): ") or profesor[3]
    nuevo_dni_input = input(f"DNI actual ({profesor[4]}): ")
    nuevo_dni = int(nuevo_dni_input) if nuevo_dni_input.strip() != "" else profesor[4]

    cursor.execute("""
        UPDATE profesores
        SET nombre = ?, apellido = ?, correo = ?, dni = ?
        WHERE id = ?
    """, (nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_dni, id_profesor))
    conexion.commit()
    print("Profesor actualizado correctamente.")



def eliminar_profesor():
    id_profesor = input("Ingrese el ID del profesor a eliminar: ")
    cursor.execute("SELECT * FROM profesores WHERE id = ?", (id_profesor,))
    profesor = cursor.fetchone()
    if profesor:
        cursor.execute("DELETE FROM profesores WHERE id = ?", (id_profesor,))
        conexion.commit()
        print("Profesor eliminado correctamente.")
    else:
        print("No se encontró un profesor con ese ID.")