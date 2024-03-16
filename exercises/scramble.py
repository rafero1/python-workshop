from random import shuffle, choice

"""
Palavras embaralhadas

Escreva um programa que leia uma lista de palavras fornecida, escolha uma, embaralhe as suas letras e peça para o usuário adivinhar a palavra original numa quantidade limitada de tentativas.

Dicas:
- use a função choice(lista) do módulo para escolher uma palavra aleatória da lista
- separe a palavra escolhida em uma lista de letras com list(palavra)
- use a função shuffle(lista) do módulo para embaralhar as letras da palavra
- use input() para receber a palavra do usuário e atribua a uma variável
- use um loop while com if-else para repetir as tentativas do jogador até que ele acerte a palavra ou esgote as tentativas

atenção! maiusculas e minusculas são letras diferentes
"""


def palavras_embaralhadas(palavras, chances):
    raise NotImplementedError


if __name__ == "__main__":
    palavras = ['casa', 'papel', 'moeda', 'molho']

    palavras_embaralhadas(palavras=palavras, chances=3)
