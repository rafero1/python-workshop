"""
Mad Libs é um jogo onde um jogador é convidado a preencher lacunas em uma história com palavras aleatórias, sem saber o contexto da história. O resultado é uma história provavelmente sem sentido ou engraçada.

Escreva um programa que leia uma história com lacunas e peça para o usuário fornecer palavras. Informe ao usuário apenas o tipo de palavra que ele deve fornecer (substantivo, verbo, adjetivo, etc), sem informar o contexto da história.

Em seguida, use as palavras fornecidas pelo usuário para preencher as lacunas da história e imprima o resultado. Lembre-se de que cada lacuna deve ser preenchida com a palavra apropriada para aquele contexto. Ex: um substantivo deve ser preenchido com um substantivo, um verbo com um verbo, local com local, objeto com objeto, etc.

Dicas:
- use input() para receber as palavras do usuário e atribua a uma variável
- use um loop para pedir ao usuário as palavras de cada lacuna
- use um dicionário para armazenar as palavras fornecidas pelo usuário
- use um método de string para substituir as lacunas da história pelas palavras fornecidas pelo usuário
- use print() para imprimir o resultado final
- algumas palavras podem ser reutilizadas em mais de uma lacuna
"""


def mad_libs(historia: str):
    raise NotImplementedError


if __name__ == "__main__":
    historia = """
    Em um {1} dia, um {2}, muito {3}, resolveu {4} uma {5}.
    Todos os seus amigos ficaram {6}, e no final do dia, foram a sua casa para {7}.
    Porém, o que ningém sabia, é que o pobre {2} estava apenas {8}.
    E assim, todos viveram {9} para sempre.
    Exceto o {2}, que morreu, mas passa bem.
    """

    mad_libs(historia)
