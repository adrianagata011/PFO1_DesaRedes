# Trabajo Práctico: Comunicación Cliente-Servidor en Python

**Cátedra:** Programación sobre Redes - 3°A  
**Profesor:** Germán Ríos  
**Estudiante:** Adrián Agata

---

## ✨ Descripción General

Este proyecto implementa una comunicación básica **cliente-servidor** utilizando **Sockets TCP/IP** en Python.  
Los mensajes enviados desde el cliente son almacenados en una **base de datos SQLite**, y pueden ser posteriormente consultados mediante un lector independiente.

El sistema consta de **tres programas**:

- `servidor.py` → Gestiona conexiones entrantes y guarda mensajes en la base de datos.
- `cliente.py` → Envía mensajes al servidor y recibe respuestas.
- `lector_mensajes.py` → Permite consultar los mensajes almacenados en la base de datos.

---

## 📄 Descripción de cada programa

### 1. `servidor.py`
- Crea un socket TCP/IP y escucha en `localhost:5000`.
- Acepta conexiones entrantes de clientes.
- Cada mensaje recibido se guarda en `mensajes.db` junto con:
  - Contenido del mensaje
  - Fecha y hora de envío
  - Dirección IP del cliente
- Muestra en tiempo real todos los mensajes recibidos en formato de tabla.

---

### 2. `cliente.py`
- Se conecta al servidor en `localhost:5000`.
- Permite al usuario ingresar mensajes manualmente.
- Cada mensaje enviado recibe una confirmación del servidor.
- Permite finalizar la sesión escribiendo `"éxito"`.

---

### 3. `lector_mensajes.py`
- Accede a la base de datos `mensajes.db`.
- Verifica que exista la tabla `mensajes`.
- Recupera y muestra todos los mensajes almacenados en formato de tabla.
- Indica si no existen mensajes o si hay errores en la base de datos.

---

## ⚙️ Requisitos

- **Python 3.7** o superior
- Librerías utilizadas:
  - `socket`
  - `sqlite3`
  - `datetime`
  - `os`
  - `sys`

*(Todas las librerías son estándar de Python, no es necesario instalar paquetes externos.)*

---

## 🚀 Instrucciones para ejecución

1. **Iniciar el servidor:**
   ```bash
   python servidor.py
   ```
2. **En una nueva terminal, iniciar el cliente:**
   ```bash
    python cliente.py   
   ```
3. **Consultar mensajes almacenados (opcional):**
   ```bash
    python lector_mensajes.py
   ```

## 💬 Ejemplos de salida en consola

### Ejemplo de ejecución en `servidor.py`
```plaintext
[INFO] Servidor escuchando en localhost:5000...

=== MENSAJES RECIBIDOS - Presione Ctrl+C para salir ===
ID    | Contenido                               | Fecha de Envío         | IP Cliente
------------------------------------------------------------------------------------------
99    | Conexión recibida                       | 2025-04-27 14:33:21    | 127.0.0.1
1     | Hola servidor!                         | 2025-04-27 14:33:25    | 127.0.0.1
2     | ¿Cómo estás?                           | 2025-04-27 14:33:30    | 127.0.0.1
99    | Conexión cerrada                        | 2025-04-27 14:33:35    | 127.0.0.1
```

### Ejemplo de ejecución en cliente.py
```plaintext
[INFO] Conexión exitosa con el servidor.
[INFO] Conectado al servidor. Puedes empezar a enviar mensajes.
Escribe un mensaje (o 'éxito' para salir): Hola servidor!
[SERVER] Mensaje recibido: 2025-04-27 14:33:25
Escribe un mensaje (o 'éxito' para salir): ¿Cómo estás?
[SERVER] Mensaje recibido: 2025-04-27 14:33:30
Escribe un mensaje (o 'éxito' para salir): éxito
[INFO] Cerrando la conexión.
```

### Ejemplo de ejecución en lector_mensajes.py
```plaintext
=== MENSAJES GUARDADOS ===
ID    | Contenido                               | Fecha de Envío         | IP Cliente
------------------------------------------------------------------------------------------
1     | Hola servidor!                         | 2025-04-27 14:33:25    | 127.0.0.1
2     | ¿Cómo estás?                           | 2025-04-27 14:33:30    | 127.0.0.1
```