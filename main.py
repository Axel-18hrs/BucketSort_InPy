import random
import time

def generar_vector_double(minon=0, length=10, values=5):
    _list = []
    for i in range(minon, length):
        if i < values:
            new_valor = random.random()
            _list.append(new_valor)
        else:
            break
    return _list

def generar_vector(minon=0, length=10, values=5):
    _list = []
    for i in range(minon, length):
        if i < values:
            new_valor = random.randint(minon, length)
            if new_valor in _list:
                i -= 1
                continue
            _list.append(new_valor)
        else:
            break
    return _list

def print_array(arr):
    for item in arr:
        print(item, end=" ")
    print()

def print_bucket_state(buckets):
    print("Current state of buckets:")
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i}: {', '.join(map(str, bucket))}")
    print()

def bucket_sort_double(array):
    # Crear buckets vacíos
    buckets = [[] for _ in range(len(array))]

    # Insertar elementos en sus respectivos buckets
    for element in array:
        buckets[int(element * len(array))].append(element)

    # Imprimir el estado de los buckets después de la inserción
    print_bucket_state(buckets)

    # Iniciar la medición del tiempo
    start_time = time.time()

    # Ordenar los elementos de cada cubo
    for i in range(len(array)):
        buckets[i].sort()

    # Imprimir el estado de los buckets después de la ordenación
    print_bucket_state(buckets)

    # Obtener los elementos ordenados
    k = 0
    for i in range(len(array)):
        for item in buckets[i]:
            array[k] = item
            k += 1

    # Detener la medición del tiempo y calcular la duración
    end_time = time.time()
    duration = end_time - start_time

    print(f"El proceso ha tardado: {duration:.6f} segundos")

def bucket_sort_int(array):
    # Encuentra el valor máximo en el array
    max_val = max(array)

    # Crea una lista de buckets vacíos
    buckets = [[] for _ in range(max_val + 1)]

    # Distribuye los elementos en los buckets
    for element in array:
        buckets[element].append(element)

    # Imprime el estado de los buckets antes de la ordenación
    print_bucket_state(buckets)

    # Iniciar la medición del tiempo
    start_time = time.time()

    # Ordena cada cubo individualmente
    for i in range(len(buckets)):
        buckets[i].sort()

    # Imprime el estado de los buckets después de la ordenación
    print_bucket_state(buckets)

    # Concatena los elementos ordenados de cada cubo
    index = 0
    for i in range(len(buckets)):
        for item in buckets[i]:
            array[index] = item
            index += 1

    # Detener la medición del tiempo y calcular la duración
    end_time = time.time()
    duration = end_time - start_time

    print(f"El proceso ha tardado: {duration:.6f} segundos")

if __name__ == "__main__":
    while True:
        print("\nSeleccione una opción:")
        print("1. Utilizar el arreglo directamente (números enteros)")
        print("2. Utilizar el método que genera un vector (números enteros)")
        print("3. Utilizar el arreglo directamente (números decimales)")
        print("4. Utilizar el método que genera un vector (números decimales)")
        print("0. Salir")

        try:
            option = int(input())
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")
            continue

        if option == 1:
            array1 = [4, 2, 3, 5, 5, 7, 1]
            print("Array antes de ordenar:")
            print_array(array1)
            bucket_sort_int(array1)
            print("\nArray después de ordenar:")
            print_array(array1)
        elif option == 2:
            array2 = generar_vector()
            print("Array antes de ordenar:")
            print_array(array2)
            bucket_sort_int(array2)
            print("\nArray después de ordenar:")
            print_array(array2)
        elif option == 3:
            array3 = [0.42, 0.33, 0.37, 0.57, 0.40]
            print("Array antes de ordenar:")
            print_array(array3)
            bucket_sort_double(array3)
            print("\nArray después de ordenar:")
            print_array(array3)
        elif option == 4:
            array4 = generar_vector_double()
            print("Array antes de ordenar:")
            print_array(array4)
            bucket_sort_double(array4)
            print("\nArray después de ordenar:")
            print_array(array4)
        elif option == 0:
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 0 al 4.")

        input("Presione Enter para continuar...")
