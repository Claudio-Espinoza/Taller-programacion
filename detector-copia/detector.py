import difflib



def compare_python_files(file1_path, file2_path):
    with open(file1_path, "r") as file1:
        lines1 = file1.readlines()

    with open(file2_path, "r") as file2:
        lines2 = file2.readlines()

    differ = difflib.Differ()
    diff = list(differ.compare(lines1, lines2))

    similar_lines = [line[2:] for line in diff if line.startswith("  ")]

    similarity_percentage = (len(similar_lines) / max(len(lines1), len(lines2))) * 100

    return similarity_percentage, similar_lines


def main():
    file1_path = "resource/prueba_1.py"
    file2_path = "resource/prueba_3.py"

    similarity_percentage = compare_python_files(file1_path, file2_path)

    print(f"Porcentaje de similitud: {similarity_percentage:.1f}%")
    print("Líneas similares:")


if __name__ == "__main__":
    main()
