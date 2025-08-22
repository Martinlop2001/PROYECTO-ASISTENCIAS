


import sqlite3

conexion = sqlite3.connect("database.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profesores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    correo TEXT,
    dni NUMERIC
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    correo TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
)
""")