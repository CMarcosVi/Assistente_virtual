import os

def search_file(file_name, search_path="C:/"):
    """
    Função que procura um arquivo no sistema de arquivos dado um nome de arquivo.

    :param file_name: Nome do arquivo a ser procurado.
    :param search_path: Diretório onde a busca será iniciada. O padrão é "C:/", mas pode ser alterado.
    :return: Caminho completo do arquivo, se encontrado, ou uma mensagem indicando que não foi encontrado.
    """
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Arquivo encontrado: {file_path}")
            return file_path
    print(f"Arquivo '{file_name}' não encontrado no diretório {search_path}.")
    return None

# Exemplo de uso
search_file("notepad.exe")  # Substitua 'notepad.exe' pelo nome do arquivo que deseja procurar


