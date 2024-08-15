class HashTable:
    def __init__(self, size):
        """
        Inicializa a tabela hash com um determinado tamanho.

        Parâmetros:
        size (int): O tamanho da tabela hash.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Cria uma lista de listas (encadeamento)

    def hash_function(self, key):
        """
        Função hash simples que converte a chave em um índice.

        Parâmetros:
        key (int/str): A chave que será transformada em índice.

        Retorna:
        int: O índice na tabela hash.
        """
    
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insere um par chave-valor na tabela hash.

        Parâmetros:
        key (int/str): A chave para o valor.
        value (any): O valor associado à chave.
        """
        index = self.hash_function(key)
        print(f"Inserindo '{value}' com a chave '{key}' no índice {index}")

        # Verifica se a chave já existe e atualiza o valor
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Chave '{key}' já existe, valor atualizado para '{value}'")
                return

        # Se a chave não existir, adiciona o novo par chave-valor
        self.table[index].append([key, value])
        print(f"Chave '{key}' e valor '{value}' inseridos na lista no índice {index}")

    def search(self, key):
        """
        Busca um valor na tabela hash dado uma chave.

        Parâmetros:
        key (int/str): A chave para procurar o valor.

        Retorna:
        any: O valor associado à chave, ou None se não for encontrado.
        """
        index = self.hash_function(key)
        print(f"Procurando pela chave '{key}' no índice {index}")

        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Valor '{pair[1]}' encontrado para a chave '{key}'")
                return pair[1]

        print(f"Chave '{key}' não encontrada")
        return None

    def delete(self, key):
        """
        Remove um par chave-valor da tabela hash.

        Parâmetros:
        key (int/str): A chave a ser removida.
        """
        index = self.hash_function(key)
        print(f"Removendo a chave '{key}' no índice {index}")

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                removed_value = self.table[index].pop(i)
                print(f"Chave '{key}' removida com valor '{removed_value[1]}'")
                return

        print(f"Chave '{key}' não encontrada para remoção")


# Exemplo de uso
hash_table = HashTable(10)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)
hash_table.insert("grape", 40)

print("\n--- Busca ---")
hash_table.search("banana")
hash_table.search("grape")
hash_table.search("cherry")  # Não está na tabela

print("\n--- Remoção ---")
hash_table.delete("orange")
hash_table.delete("cherry")  # Não está na tabela
