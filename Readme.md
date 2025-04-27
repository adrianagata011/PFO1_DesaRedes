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
3. **Enviar mensajes desde el cliente.**
   ```bash
    # Escribir cualquier texto.
    # Para finalizar la sesión: escribir "éxito"
   ```
4. **Consultar mensajes almacenados (opcional):**
   ```bash
python lector_mensajes.py
   ```
