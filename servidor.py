# =============================
# Programación sobre Redes - 3°A
# Profesor: Germán Ríos
# Estudiante: Adrián Agata
# =============================

import socket
import sqlite3
from datetime import datetime
import sys

# =============================
# Inicializar la base de datos
# =============================
def inicializar_db():
    try:
        conn = sqlite3.connect("mensajes.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo inicializar la base de datos: {e}")
        sys.exit(1)

# =============================
# Guardar mensaje en la DB
# =============================
def guardar_mensaje_db(contenido, fecha_envio, ip_cliente):
    try:
        conn = sqlite3.connect("mensajes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (contenido, fecha_envio, ip_cliente))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"[ERROR] Error al guardar el mensaje: {e}")

# =============================
# Mostrar mensaje en formato tabla
# =============================
def mostrar_mensaje(id_, contenido, fecha_envio, ip_cliente):
    print("{:<5} | {:<40} | {:<20} | {:<15}".format(id_, contenido[:40], fecha_envio, ip_cliente))

# =============================
# Inicializar el socket
# =============================
def inicializar_socket():
    try:
        # Configuración del socket TCP/IP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 5000))  # Escuchar en localhost:5000
        server_socket.listen(5)  # Hasta 5 conexiones en espera
        server_socket.settimeout(1)  # ➡️ Agregado: timeout para no bloquear indefinidamente
        print("[INFO] Servidor escuchando en localhost:5000...")
        return server_socket
    except socket.error as e:
        if e.errno == 10048:
            print("[ERROR] El puerto 5000 ya está en uso. Intenta con otro puerto.")
        else:
            print(f"[ERROR] No se pudo iniciar el socket: {e}")
        sys.exit(1)

# ======================================
# Aceptar conexiones y recibir mensajes
# ======================================
def aceptar_conexiones(server_socket):
    print("\n=== MENSAJES RECIBIDOS - Presione Ctrl+C para salir ===")
    print("{:<5} | {:<40} | {:<20} | {:<15}".format("ID", "Contenido", "Fecha de Envío", "IP Cliente"))
    print("-" * 90)

    id_contador = obtener_ultimo_id()
    mensajes_sesion = 0

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue  # ➡️ No había conexión, vuelve al loop
            except Exception as e:
                print(f"[ERROR] Error inesperado en accept: {e}")
                break

            ip_cliente = client_address[0]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mostrar_mensaje(99, "Conexión recibida", timestamp, ip_cliente)

            try:
                while True:
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data:
                        break

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    guardar_mensaje_db(data, timestamp, ip_cliente)

                    id_contador += 1
                    mensajes_sesion += 1

                    mostrar_mensaje(id_contador, data, timestamp, ip_cliente)

                    # Aquí se asegura de enviar una respuesta al cliente
                    respuesta = f"Mensaje recibido: {timestamp}"
                    client_socket.send(respuesta.encode('utf-8'))  # Enviamos la respuesta

            except Exception as e:
                print(f"[ERROR] Error durante la comunicación con el cliente: {e}")

            finally:
                client_socket.close()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                mostrar_mensaje(99, "Conexión cerrada", timestamp, ip_cliente)

    except KeyboardInterrupt:
        print("\n\n[INFO] Servidor detenido manualmente con Ctrl+C")
        print(f"[RESUMEN] Total de mensajes recibidos en esta sesión: {mensajes_sesion} 📩")
    except Exception as e:
        print(f"[ERROR] Error general del servidor: {e}")
    finally:
        server_socket.close()
        print("[INFO] Socket cerrado. Adiós 👋")
        sys.exit(0)

# =============================
# Obtener el último ID en la DB
# =============================
def obtener_ultimo_id():
    try:
        conn = sqlite3.connect("mensajes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM mensajes")
        last_id = cursor.fetchone()[0]
        conn.close()
        if last_id is None:
            return 0
        return last_id
    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo leer el último ID: {e}")
        return 0

# =============================
# Programa principal del servidor
# =============================
if __name__ == "__main__":
    inicializar_db()
    servidor = inicializar_socket()
    aceptar_conexiones(servidor)
