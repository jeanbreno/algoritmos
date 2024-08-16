def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Troca: {arr}")
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"Pivô {pivot} colocado na posição {i + 1}: {arr}")
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        indice_pivot = partition(arr, low, high)
        
        print(f"Sublista após particionamento: {arr[low:high+1]} com pivô em {arr[indice_pivot]}")

        quicksort(arr, low, indice_pivot - 1)
        quicksort(arr, indice_pivot + 1, high)

# Exemplo de uso
example_list = [10, 7, 8, 9, 1, 5]
print("Lista original:", example_list)
quicksort(example_list, 0, len(example_list) - 1)
print("Lista ordenada:", example_list)
