from pathlib import Path

# complete as funções abaixo
# substitua "raise NotImplementedError" pelo seu código


def t_escrever_log(caminho, linha):
    """
    Crie um arquivo de log usando o caminho e linha de texto fornecido.
    Se o arquivo de log já existir no caminho fornecido, adicione a linha de texto ao final do arquivo.
    Toda linha de texto deve ser possuir a data e hora atual antes do texto, no formato "[YYYY-MM-DD HH:MM:SS.SSS] texto"
    """


def t_ler_log(caminho):
    """
    Leia o conteúdo de um arquivo de log e retorne como uma string.
    """
    with open(caminho, 'r') as f:
        return f.read()


if __name__ == "__main__":
    current_file_path = Path(__file__).parent.absolute()

    t_escrever_log(current_file_path / 'log.txt', 'linha 1')
    t_escrever_log(current_file_path / 'log.txt', 'linha 2')

    log_text = t_ler_log(current_file_path / 'log.txt')
    print(log_text)
