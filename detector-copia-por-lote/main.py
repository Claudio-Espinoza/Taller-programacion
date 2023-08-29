from detector_lote import seleccionar_archivos_para_revision as detector
import os as gestor

RUTA_RESOURCE_ALUMNO = "resource"
RUTA_RESOURCE_GPT = "resource-chatGPT"


def comparar_carpetas():
    archivos_alumnos = gestor.listdir(RUTA_RESOURCE_ALUMNO)
    archivos_gpt = gestor.listdir(RUTA_RESOURCE_GPT)

    for indice_alumno in archivos_alumnos:
        path = str(RUTA_RESOURCE_ALUMNO) + "/" + str(indice_alumno)

        for indice_gpt in archivos_gpt:
            path_gpt = str(RUTA_RESOURCE_GPT) + "/" + str(indice_gpt)
            detector(path_gpt, path)
    print()




def mostrar_archivos_incriminatorios(ruta, tipo_archivo):
    archivos = gestor.listdir(ruta)
    print(f"{tipo_archivo} - Se encontro {len(archivos)} archivos:")
    for archivo in archivos:
        print(f"- {archivo}")
    print()


if __name__ == '__main__':
    print()
    mostrar_archivos_incriminatorios(RUTA_RESOURCE_GPT, "GPT")
    mostrar_archivos_incriminatorios(RUTA_RESOURCE_ALUMNO, "ALUMNO")

    comparar_carpetas()