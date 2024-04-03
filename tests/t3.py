from do_test import do_test, do_test_void

# complete as funções abaixo
# substitua "raise NotImplementedError" pelo seu código


def t_print_impares_entre(x, y):
  """
    Deve imprimir no console todos os numeros impares entre x e y

    Dica: use print() para imprimir algo no console
    """
  raise NotImplementedError


def t_print_lista(lista):
  """ Deve imprimir no console os items da lista,
    no formato de string separado por virgula
    Ex: [1, 2, 3] -> "1, 2, 3"
    """
  raise NotImplementedError


def t_add_sufix_lista(lista, sufixo):
  """
    Deve retornar uma nova lista com o sufixo adicionado a cada item da lista
    Ex: ["a", "b", "c"], "!" -> ["a!", "b!", "c!"]
    """
  raise NotImplementedError


def t_busca_linear(item, lista):
  """
    Deve retornar o índice do item na lista, ou -1 caso o item não exista na lista

    Para obter o índice de um item em uma lista, use lista.index(item)

    """
  raise NotImplementedError


def t_contagem_char(lista, caractere):
  """
    Deve retornar a quantidade de vezes que o caractere aparece nas palavras da lista
    Ex: ["a", "ba", "c"], "a" -> 2
    """
  raise NotImplementedError


def t_fatorial(x):
  """
    Deve calcular e retornar o fatorial de x
    O fatorial de um número inteiro x (representado como x!) é o produto de todos
    os números inteiros positivos de 1 até x (incluso)

    Exemplo: 5! = 5 * 4 * 3 * 2 * 1, portanto 5! = 120

    Dica: range(n1, n2) retorna uma lista de números entre n1 e n2
    """
  raise NotImplementedError


def t_print_fatorial(x):
  """
    Deve imprimir no console o uma string que representa
    o calculo do fatorial de um numero inteiro x

    Ex: Se x for 5, essa função deve imprimir no console o seguinte: "5! = 5 * 4 * 3 * 2 * 1"

    Dica: para combinar um inteiro com uma string, use str() para transforma-lo em uma string
    Ex: str(x) + "!" = "5!"
    """
  raise NotImplementedError


def t_dict_invertido(dicionario):
  """
    Deve retornar um dicionário com as chaves e valores invertidos

    Ex: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
  raise NotImplementedError


def t_set_diferenca(set1, set2):
  """
    Deve retornar um set com os elementos que estão em set1 mas não em set2.
    Se não houver elementos diferentes, retorne um set vazio

    Ex: {1, 2, 3}, {3, 4} -> {1, 2}
    """
  raise NotImplementedError


def t_peso_medio(lista_pesos):
  """
    Deve calcular e retornar o peso médio de uma lista de pesos

    O peso médio é a soma de todos os pesos dividido pela quantidade de pesos
    Ex: [70, 80, 60] -> (70 + 80 + 60) / 3 = 70

    Dica: use sum(lista) para somar todos os valores de uma lista
    """
  raise NotImplementedError


def t_verificar_senha(senha):
  """
    Deve retornar True se a senha bate com os requisitos abaixo, False caso contrário:

    - Pelo menos 8 caracteres
    - Pelo menos uma letra minúscula
    - Pelo menos uma letra maiúscula
    - Pelo menos um número
    - Pelo menos um caractere especial: !@#$%^&*()-+
    """
  raise NotImplementedError
