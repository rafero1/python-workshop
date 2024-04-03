from random import randint
"""
Crie um jogo onde o computador escolhe um número aleatório entre 1 e 100,
e o jogador tem que adivinhar o número em no máximo 10 tentativas.

Sempre que o jogador errar, o computador deve dizer se o número correto é maior ou menor
que o número que o jogador escreveu.

Dicas:
- use a função randint(x, y) do módulo random para gerar um número aleatório entre x e y. Ela já está importada no início do arquivo.
- use input() para receber o número do jogador e atribua a uma variável
- use int(x) para converter uma variável x para inteiro
- use um loop while com if-else para repetir as tentativas do jogador até que ele acerte o número ou esgote as tentativas

Execute o jogo rodando o seguinte comando no terminal dentro da pasta raiz do projeto:
python exercises/number_game.py
"""


def adivinhe_o_numero(min=1, max=100, chances=10):
  raise NotImplementedError


if __name__ == "__main__":
  adivinhe_o_numero()
