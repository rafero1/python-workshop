import os


def t_padronizar_nomes_de_arquivos(raiz):
  """
    Renomeie todos os arquivos de um diretório para que o nome de cada arquivo siga o formato snake_case. Ex: "arquivo_n.txt"

    Dicas:
    - use "for item in os.scandir(diretorio)" para iterar sobre os arquivos de um diretório
    - use item.is_file() para verificar se um item é um arquivo
    - use item.name para obter o nome (filename) de um arquivo
    - use item.path para obter o caminho completo de um arquivo
    - use os.rename(caminho_do_arquivo, novo_caminho_do_arquivo) para renomear um arquivo. Lembre-se que o caminho do arquivo é o caminho completo.
    """
  raise NotImplementedError


if __name__ == "__main__":
  raiz = os.path.join(os.path.dirname(__file__), "arquivos")
  t_padronizar_nomes_de_arquivos(raiz)
