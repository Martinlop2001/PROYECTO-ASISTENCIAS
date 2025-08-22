



from modelos.alumno import Alumno
from db.conexion import conexion, cursor

def menu_alumnos():
    while True:
        print("\n--- Gestion de Alumnos ---")
        print("1. Agregar alumno")
        print("2. Listar alumnos")
        print("3. Editar alumno")
        print("4. Eliminar alumno")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            listar_alumno()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "0":
            break
        else:
            print ("Opción inválida...")



def agregar_alumno():

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")

    alumno = Alumno(nombre, apellido, correo)

    cursor.execute("""
                INSERT INTO alumnos (nombre, apellido, correo)
                VALUES (?, ?, ?)
            """, (alumno.nombre, alumno.apellido, alumno.correo))

    conexion.commit()
    print("Alumno agregado correctamente.")



def listar_alumno():
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        print("\nLista de alumnos:")
        for alum in alumnos:
            print(f"ID: {alum[0]} | Nombre: {alum[1]} | Apellido: {alum[2]} | Correo: {alum[3]}")


def editar_alumno():
    
    id_alumno = input("Ingrese el ID del alumno a editar: ")
    cursor.execute("SELECT * FROM alumnos WHERE id = ?", (id_alumno,))
    alumno = cursor.fetchone()
    if not alumno:
        print("No se encontro un alumno con ese ID.")
        return

    print("Deje en blanco para mantener el valor actual.")
    nuevo_nombre = input(f"Nombre actual ({alumno[1]}): ") or alumno[1]
    nuevo_apellido = input(f"Apellido actual ({alumno[2]}): ") or alumno[2]
    nuevo_correo = input(f"Correo actual ({alumno[3]}): ") or alumno [3]

    cursor.execute("""
        UPDATE alumnos
        SET nombre = ?, apellido = ?, correo = ?
        WHERE id = ?
        """, (nuevo_nombre, nuevo_apellido, nuevo_correo, id_alumno))

    conexion.commit()
    print("Alumno actualizado correctamente.")


def eliminar_alumno():
    id_alumno = input("Ingrese ID de alumno: ")
    cursor.execute("SELECT * FROM alumnos WHERE id = ?", (id_alumno,))
    alumno = cursor.fetchone()

    if alumno:
        cursor.execute ("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
        conexion.commit()
        print("Alumno aliminado correctamente.")

    else:
        print("No se encontro alumno con ese ID.")