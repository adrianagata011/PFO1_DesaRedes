# =============================
# Programación sobre Redes - 3°A
# Profesor: Germán Ríos
# Estudiante: Adrián Agata
# =============================

import socket
import sys

# =============================
# Conectarse al servidor
# =============================
def conectar_al_servidor():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    cliente_socket.settimeout(5)  # Timeout para evitar que el cliente se quede esperando indefinidamente

    try:
        # Intentar conectar con el servidor en localhost:5000
        cliente_socket.connect(('localhost', 5000))
        print("[INFO] Conexión exitosa con el servidor.")
        return cliente_socket
    except socket.error as e:
        if e.errno == 10061:  # Error de conexión rechazada
            print("[ERROR] Ya hay una conexión activa con el servidor.")
        else:
            print(f"[ERROR] No se pudo conectar al servidor: {e}")
        sys.exit(1)

# =============================
# Enviar mensajes al servidor
# =============================
def enviar_mensajes(cliente_socket):
    print("[INFO] Conectado al servidor. Puedes empezar a enviar mensajes.")
    
    while True:
        mensaje = input("Escribe un mensaje (o 'éxito' para salir): ")
        
        if mensaje.lower() == "éxito":
            print("[INFO] Cerrando la conexión.")
            break
        
        # Enviar el mensaje al servidor
        cliente_socket.send(mensaje.encode('utf-8'))
        
        # Recibir la respuesta del servidor
        try:
            respuesta = cliente_socket.recv(1024).decode('utf-8')
            print(f"[SERVER] {respuesta}")
        except socket.timeout:
            print("[ERROR] Tiempo de espera agotado. El servidor no respondió.")
            break
    
    cliente_socket.close()

# =============================
# Programa principal
# =============================
if __name__ == "__main__":
    cliente_socket = conectar_al_servidor()
    enviar_mensajes(cliente_socket)
