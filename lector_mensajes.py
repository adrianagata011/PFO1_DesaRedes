# =============================
# Programación sobre Redes - 3°A
# Profesor: Germán Ríos
# Estudiante: Adrián Agata
# =============================

import sqlite3
import os
import sys

# =============================
# Mostrar mensajes en tabla
# =============================
def mostrar_mensaje(id_, contenido, fecha_envio, ip_cliente):
    print("{:<5} | {:<40} | {:<20} | {:<15}".format(id_, contenido[:40], fecha_envio, ip_cliente))

# =============================
# Leer mensajes de la base de datos
# =============================
def leer_mensajes():
    if not os.path.exists("mensajes.db"):
        print("[ERROR] No se encontró el archivo 'mensajes.db'.")
        print("Por favor, asegúrate de que exista y tenga datos.")
        sys.exit(1)

    try:
        conn = sqlite3.connect("mensajes.db")
        cursor = conn.cursor()

        # Verificar si existe la tabla 'mensajes'
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='mensajes'
        """)
        tabla = cursor.fetchone()

        if not tabla:
            print("[ERROR] La base de datos no contiene la tabla 'mensajes'.")
            print("Ejecuta el servidor primero para inicializar la base de datos correctamente.")
            sys.exit(1)

        # Si existe la tabla, leer los mensajes
        cursor.execute("SELECT id, contenido, fecha_envio, ip_cliente FROM mensajes ORDER BY id ASC")
        mensajes = cursor.fetchall()
        conn.close()

        if mensajes:
            print("\n=== MENSAJES GUARDADOS ===")
            print("{:<5} | {:<40} | {:<20} | {:<15}".format("ID", "Contenido", "Fecha de Envío", "IP Cliente"))
            print("-" * 90)
            for mensaje in mensajes:
                mostrar_mensaje(*mensaje)
        else:
            print("[INFO] No hay mensajes en la base de datos.")

    except sqlite3.Error as e:
        print(f"[ERROR] Error al leer la base de datos: {e}")
        sys.exit(1)

# =============================
# Programa principal
# =============================
if __name__ == "__main__":
    leer_mensajes()
