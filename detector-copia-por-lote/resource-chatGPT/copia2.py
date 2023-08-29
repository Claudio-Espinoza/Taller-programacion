import os  # Gestiona todas las demás funciones
import shutil  # Uso la función de copiar los elementos de los directorios

RUTA_ORIGEN = 'remoto/confidencial'
RUTA_DESTINO = 'local/datos_incriminatorios'
PALABRAS_BUSCADAS = ["maltrato", "hambre", "malos tratos"]


def mostrar_archivos_incriminatorios():
    archivos = os.listdir(RUTA_ORIGEN)  # Retorna el contenido dentro de una determinada ruta
    print(f"Se encontraron {len(archivos)} archivos:")
    for indice, archivo in enumerate(archivos):
        path = str(RUTA_DESTINO) + "/" + str(archivo)  # Creo una path (dirección de ruta) señalando los directorios
        datos = os.stat(path)  # Retorna la información de los archivos contenidos por el path (La ruta)
        print(f"{indice + 1}.- {archivo} \t Tamaño: {datos.st_size}")  # Devuelve el tamaño
    print()


def traspasar_archivos():
    archivos = os.listdir(RUTA_ORIGEN)
    for archivo in archivos:
        # Con esta función propia de la libreria, se guarda las rutas dentro de la libreria
        registrar_origen = os.path.join(RUTA_ORIGEN, archivo)
        registrar_destino = os.path.join(RUTA_DESTINO, archivo)
        shutil.copy(registrar_origen, registrar_destino)  # Se copia el contenido previamente registrado


def obtener_datos_archivos():  # Se aplica la misma logia previamente mostrada
    archivos = os.listdir(RUTA_DESTINO)
    for archivo in archivos:
        path = str(RUTA_DESTINO) + "/" + str(archivo)
        lectura = open(path, "r")  # Se abre la lectura
        contenido = lectura.read()  # Se guarda el contenido del archivo dentro de una variable
        lectura.close()  # Cierro la lectura (No es obligatorio)
        for palabra in PALABRAS_BUSCADAS:
            if palabra in contenido:
                print(f"En el archivo {archivo}: Fue encontrada la palabra {palabra}")
            else:
                print(f"En el archivo {archivo}: No fue encontrada la palabra {palabra}")
        print()


if __name__ == '__main__':
    mostrar_archivos_incriminatorios()
    traspasar_archivos()
    obtener_datos_archivos()
