


from modelos.materia import Materia
from db.conexion import conexion, cursor


def menu_materia():
    while True:
        print("\n--- Gestión de Materias ---")
        print("1. Agregar materia")
        print("2. Listar materia")
        print("3. Editar materia")
        print("4. Eliminar materia")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_materia()
        elif opcion == "2":
            listar_materia()
        elif opcion == "3":
            editar_materia()
        elif opcion == "4":
            eliminar_materia()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")



def agregar_materia():

    nombre = input("Nombre: ")

    materia = Materia(nombre)

    cursor.execute("INSERT INTO materias (nombre) VALUES (?)", (materia.nombre,))

    conexion.commit()
    print("Materia agregada correctamente.")


def listar_materia():
    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()
    if not materias:
        print("No hay materias registradas.")
    else:
        print("\nLista de Materias: ")
        for mat in materias:
            print(f"ID: {mat[0]} | Nombre: {mat[1]}")



def editar_materia():
    id_materia = input("Ingrese ID de materia a editar: ")
    cursor.execute ("SELECT * FROM materias WHERE id = ?", (id_materia,))
    materia = cursor.fetchone()
    if not materia:
        print("No se encontro materia con ese ID.")
        return
    
    print("Deje en blanco para mantener el valor actual.")

    nuevo_nombre = input(f"Nombre actual de materia ({materia[1]}): ") or materia[1]

    cursor.execute("""
        UPDATE materias
        SET nombre = ?
        WHERE id = ?
        """, (nuevo_nombre, id_materia))
    
    conexion.commit()
    print("Materia actualizada correctamente.")


def eliminar_materia():

    id_materia = input("Ingrese ID materia a eliminar: ")
    cursor.execute("SELECT * FROM materias WHERE id = ?", (id_materia,))
    materia = cursor.fetchone()

    if materia:
        cursor.execute("DELETE FROM materias WHERE id = ?", (id_materia,))
    else:
        print("No se encontro materia con ese ID.")