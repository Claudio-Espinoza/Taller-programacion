import difflib


def leer_archivo(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()
    return lines


def comparar_archivo(archivo_gpt, archivo_alumno):
    differ = difflib.Differ()
    diff = list(differ.compare(archivo_gpt, archivo_alumno))

    return [line[2:] for line in diff if line.startswith("  ")]


def mostrar_comparacion(archivo_gpt, archivo_alumno):
    lineas_similares = comparar_archivo(archivo_gpt, archivo_alumno)

    similarity_percentage = (len(lineas_similares) / max(len(archivo_gpt), len(archivo_alumno))) * 100
    return similarity_percentage


def comparar_python_files(ruta_gpt, ruta_alumno):
    archivo_alumno = leer_archivo(ruta_alumno)
    archivo_gpt = leer_archivo(ruta_gpt)

    return mostrar_comparacion(archivo_gpt, archivo_alumno)


def seleccionar_archivos_para_revision(archivo_gpt, archivo_original, indice_gpt, indice_estudiante):
    similarity_percentage = comparar_python_files(archivo_gpt, archivo_original)

    print(f"Coincidencia entre:{indice_gpt} - {indice_estudiante}:\t Similitud(%): {similarity_percentage:.2f}%")
