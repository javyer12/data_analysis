import logging
import sys

# 1. Configuración básica del logger
# Define el nombre del archivo de log
NOMBRE_ARCHIVO_LOG = 'mi_aplicacion.log'

# Obtiene el logger con el nombre del módulo actual
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # Establece el nivel mínimo de logs a capturar

# 2. Define un controlador para la consola (StreamHandler)
consola_handler = logging.StreamHandler(sys.stdout)
consola_handler.setLevel(logging.INFO) # Muestra INFO y superiores en consola

# 3. Define un controlador para el archivo (FileHandler)
archivo_handler = logging.FileHandler(NOMBRE_ARCHIVO_LOG)
archivo_handler.setLevel(logging.DEBUG) # Guarda DEBUG y superiores en archivo

# 4. Define un formato para los mensajes de log
# Incluye tiempo, nivel y mensaje
FORMATO = '%(asctime)s - %(levelname)s - %(messageS)s'
formatter = logging.Formatter(FORMATO)

# Asigna el formato a ambos handlers
consola_handler.setFormatter(formatter)
archivo_handler.setFormatter(formatter)

# 5. Añade los handlers al logger
logger.addHandler(consola_handler)
logger.addHandler(archivo_handler)

# --- Uso del logger ---

try:
    with open("mi_aplicacion.log", "r") as f:
        f.write(logger.debug('Este es un mensaje de depuración (no sale en consola)') )
        f.write(logger.info('La aplicación ha comenzado su ejecución.') )
        f.write(logger.warning('Advertencia: La conexión a la base de datos es lenta.') )
        f.write(logger.error('Error: No se pudo procesar el archivo X.') )  
except Exception as e:
    print("Ocurrió un error al escribir en el archivo de log:", e)