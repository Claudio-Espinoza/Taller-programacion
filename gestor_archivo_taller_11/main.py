import os
import shutil

RUTA_ORIGEN = 'remoto/confidencial'
RUTA_DESTINO = 'local/datos_incriminatorios'
PALABRAS_BUSCADAS = ["maltrato", "hambre", "malos tratos"]


def mostrar_archivos_incriminatorios():
    archivos = os.listdir(RUTA_ORIGEN)
    print(f"Se encontraron {len(archivos)} archivos:")
    for indice, archivo in enumerate(archivos):
        path = str(RUTA_DESTINO) + "/" + str(archivo)
        informacion = os.stat(path)
        print(f"{indice+1}.- {archivo} \t Tamaño: {informacion.st_size}")
    print()


def traspasar_archivos():
    archivos = os.listdir(RUTA_ORIGEN)
    for archivo in archivos:
        registrar_origen = os.path.join(RUTA_ORIGEN, archivo)
        registrar_destino = os.path.join(RUTA_DESTINO, archivo)
        shutil.copy(registrar_origen, registrar_destino)


def obtener_informacion_archivos():
    archivos = os.listdir(RUTA_DESTINO)
    for archivo in archivos:
        path = str(RUTA_DESTINO) + "/" + str(archivo)
        lectura = open(path, "r")
        contenido = lectura.read()
        lectura.close()
        for palabra in PALABRAS_BUSCADAS:
            if palabra in contenido:
                print(f"En el archivo {archivo}: Fue encontrada la palabra {palabra}")
            else:
                print(f"En el archivo {archivo}: No fue encontrada la palabra {palabra}")
        print()


if __name__ == '__main__':
    mostrar_archivos_incriminatorios()
    traspasar_archivos()
    obtener_informacion_archivos()
