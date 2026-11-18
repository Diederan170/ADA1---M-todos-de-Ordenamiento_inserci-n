def ordenamiento_insercion(calificaciones):
    """
    Ordena una lista de calificaciones de menor a mayor
    utilizando el algoritmo de Ordenamiento por Inserción.
    """
    datos = calificaciones.copy()
    n = len(datos)

    print(f"\nCalificaciones ingresadas sin ordenar: {datos}\n")

    # Se asume que el primer elemento (índice 0) ya está ordenado
    for i in range(1, n):
        clave = datos[i]
        j = i - 1

        # Desplaza hacia la derecha los elementos mayores que 'clave'
        while j >= 0 and datos[j] > clave:
            datos[j + 1] = datos[j]
            j -= 1

        # Inserta 'clave' en el espacio libre que le corresponde
        datos[j + 1] = clave
        print(f"Iteración {i} (insertando {clave}): {datos}")

    return datos


def capturar_calificaciones():
    """Solicita al usuario la cantidad de alumnos y sus calificaciones."""
    while True:
        try:
            cantidad = int(input("¿Cuántas calificaciones deseas capturar? (mínimo 2): "))
            if cantidad >= 2:
                break
            print("Error: Ingresa al menos 2 calificaciones.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    calificaciones = []
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingresa la calificación del alumno #{i + 1} (0 a 100): "))
                if 0 <= nota <= 100:
                    calificaciones.append(int(nota) if nota.is_integer() else nota)
                    break
                print("Error: La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Ingresa un número válido.")

    return calificaciones


if __name__ == "__main__":
    print("=== ORDENAMIENTO POR INSERCIÓN: CALIFICACIONES ===")
    lista_calificaciones = capturar_calificaciones()
    resultado = ordenamiento_insercion(lista_calificaciones)
    print(f"\nCalificaciones ordenadas de menor a mayor: {resultado}")