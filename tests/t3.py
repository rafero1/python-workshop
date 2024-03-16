from do_test import do_test, do_test_void

# complete as funções abaixo
# substitua "raise NotImplementedError" pelo seu código


def t_print_impares_entre(x, y):
    """
    Deve imprimir no console todos os numeros impares entre x e y

    Dica: use print() para imprimir algo no console
    """
    raise NotImplementedError


do_test_void(t_print_impares_entre, (0, 10), (11, 111))


def t_print_lista(lista):
    """ Deve imprimir no console os items da lista,
    no formato de string separado por virgula
    Ex: [1, 2, 3] -> "1, 2, 3"
    """
    raise NotImplementedError


do_test_void(t_print_lista, ["a", "b", "c"], [1, 2, 3])


def t_busca_linear(item, lista):
    """
    Deve retornar o índice do item na lista, ou -1 caso o item não exista na lista

    Para obter o índice de um item em uma lista, use lista.index(item)

    """
    raise NotImplementedError


do_test(t_busca_linear, (("molho", ["carne", "macarrão", "molho"]), 2), ((
    "frango", ["carne", "macarrão", "molho"]), -1))


def t_fatorial(x):
    """
    Deve calcular e retornar o fatorial de x
    O fatorial de um número inteiro x (representado como x!) é o produto de todos
    os números inteiros positivos de 1 até x (incluso)

    Exemplo: 5! = 5 * 4 * 3 * 2 * 1, portanto 5! = 120

    Dica: range(n1, n2) retorna uma lista de números entre n1 e n2
    """
    raise NotImplementedError


do_test(t_fatorial, (5, 120), (10, 3628800), (4, 24))


def t_print_fatorial(x):
    """
    Deve imprimir no console o uma string que representa
    o calculo do fatorial de um numero inteiro x

    Ex: Se x for 5, essa função deve imprimir no console o seguinte: "5! = 5 * 4 * 3 * 2 * 1"

    Dica: para combinar um inteiro com uma string, use str() para transforma-lo em uma string
    Ex: str(x) + "!" = "5!"
    """
    raise NotImplementedError


do_test_void(t_print_fatorial, 5, 7)


def t_peso_medio(lista_pesos):
    """
    Deve calcular e retornar o peso médio de uma lista de pesos

    O peso médio é a soma de todos os pesos dividido pela quantidade de pesos

    Dica: use sum(lista) para somar todos os valores de uma lista
    """
    raise NotImplementedError


do_test(t_peso_medio, ([70, 80, 60], 70),
        ([100, 200, 300], 200), ([1, 2, 3], 2))

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

do_test(t_verificar_senha, ("Abc123!@", True), ("abc123", False), ("Abc123", False), ("Abc123@", False), ("Abc123!@a", False))