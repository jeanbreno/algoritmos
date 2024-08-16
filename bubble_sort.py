def bubble_sort(arr):
    list_size = len(arr)
    print("Lista inicial:", arr)

    for i in range(list_size):
        print(f"\nLoop {i + 1}:")
        swapped = False
        for j in range(0, list_size - i - 1):
            print(f"  Comparando {arr[j]} e {arr[j + 1]}", end="")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  -> Troca para {arr}")
            else:
                print("  - Sem troca")
        print(f"Estado da lista apos o loop {i + 1}: {arr}")
        if not swapped:
            print("Nenhuma troca feita, lista ja esta ordenada.")
            break
    return arr

unordered_list = [69,68,33,98,205,104,2,87,54,20,11,12]
ordered_list=bubble_sort(unordered_list)
print("Lista ordenada: ", ordered_list)
