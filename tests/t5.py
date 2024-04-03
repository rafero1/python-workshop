import os
from datetime import datetime

# complete as funções abaixo
# substitua "raise NotImplementedError" pelo seu código

# Ao terminar, execute o comando abaixo no Shell para testar:
# python tests/t5.test.py

def t_escrever_log(caminho, linha):
  """
    Crie um arquivo de log usando o caminho e linha de texto fornecido.
    Se o arquivo de log já existir no caminho fornecido, adicione a linha de texto ao final do arquivo.
    Toda linha de texto deve ser possuir a data e hora atual antes do texto, no formato "[YYYY-MM-DD HH:MM:SS.SSS] texto"
    A biblioteca datetime já foi importada para você.

    Atenção:
    - Cuidado ao escrever arquivos, pois você pode sobrescrever arquivos importantes caso o caminho esteja errado.
    - Teste em um novo diretório.

    Dicas:
    - use "with open(caminho, 'a', encoding='utf-8')" para abrir o arquivo no modo de adição (append)
    - use datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") para retornar uma string com a data e hora atual no formato desejado
    - use file.write() para escrever no arquivo
    """
  raise NotImplementedError


def t_ler_log(caminho):
  """
    Leia o conteúdo de um arquivo de log e retorne como uma string.

    Dicas:
    - use "with open(caminho, 'r', encoding='utf-8')" para abrir o arquivo no modo de leitura
    - use file.read() para ler o conteúdo do arquivo
    """
  raise NotImplementedError


