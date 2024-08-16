def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        print(f"Right: {right} - Left: {left}")
        mid = (left + right) // 2
        print(f"Verificando a sublista: {arr[left:right+1]}, Índice do meio: {mid}, Valor do meio: {arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            print(f"Elemento {target} é menor que {arr[mid]}, pesquisando na metade esquerda")
            right = mid - 1
        else:
            print(f"Elemento {target} é maior que {arr[mid]}, pesquisando na metade direita")
            left = mid + 1
    
    return None

sorted_list = [2, 3, 4, 10, 40]
target = 10

result = binary_search(sorted_list, target)

if result != None:
    print(f"Elemento {target} encontrado no índice {result}")
else:
    print("Elemento não encontrado")
