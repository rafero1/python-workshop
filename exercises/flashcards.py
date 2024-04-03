import os
"""
Flashcards são cartões usados para memorização de conteúdo. Eles são compostos por duas faces, uma com uma pergunta e outra com a resposta. O objetivo é que o estudante leia a pergunta e tente responder de memória, para depois verificar a resposta na outra face do cartão.

Escreva um programa que simule um conjunto de flashcards. O programa deve apresentar uma pergunta ao usuário e pedir para ele responder. Após a resposta, o programa deve apresentar a resposta correta, indicando se o usuário acertou ou errou. Em seguida, o programa deve apresentar a próxima pergunta e repetir o processo, até que todas as perguntas tenham sido respondidas.

As perguntas e respostas devem ser lidas de um arquivo de texto. No arquivo, cada linha deve conter uma pergunta e a resposta correspondente, separadas por um caractere especial, como (|). Ex: "Qual é a capital do Brasil?|Brasília"

Requisitos:
- Crie uma classe Game:
    - Ela será responsável por gerenciar o jogo. Modifique-a conforme necessário.
    - Deve possuir, no mínimo, os atributos flashcards, flashcard_atual, acertos e erros
    - Deve possuir, no mínimo, o método start_game(), que inicia o jogo
- Crie uma classe Flashcards:
    - Ela será responsável por representar os flashcards. Modifique-a conforme necessário.
    - Deve possuir, no mínimo, os atributos pergunta e resposta
- Leia as perguntas e respostas do arquivo de texto e armazene-as em uma lista de Flashcards
    Dica: você pode criar um método para ler o arquivo e criar os objetos Flashcards, ou fazer isso no construtor da classe Game
    Dica: use with open(arquivo, "r", encoding="utf-8") as file para abrir o arquivo no modo leitura, e file.readlines() para ler as linhas do arquivo
- Embaralhe as perguntas antes de apresentá-las ao usuário
- Use um loop para apresentar as perguntas ao usuário e pedir para ele responder
- Se a resposta do usuário estiver correta, apresente uma mensagem de acerto. Caso contrário, apresente a resposta correta
- Atualize os atributos acertos e erros em Game conforme o usuário acertar ou errar as perguntas
- No final do jogo, calcule e mostre a porcentagem de acertos e erros
- Se a porcentagem de acertos for maior que 70%, parabenize o usuário. Caso contrário, sugira que ele estude mais.
"""


class Flashcard:

  def __init__(self):
    raise NotImplementedError


class Game:

  def __init__(self, arquivo):
    self.arquivo = arquivo

  def start_game(self):
    raise NotImplementedError


if __name__ == "__main__":
  arquivo = os.path.join(os.path.dirname(__file__), "flashcards.txt")
  game = Game(arquivo)
  game.start_game()
