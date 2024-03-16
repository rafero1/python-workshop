#
# Funções
#

# Funções são procedimentos que realizam tarefas específicas.
# Funções podem receber parâmetros e retornar valores, ou apenas realizar um conjunto de instruções
# existem funções nativas do Python, como print(), input(), len()
# Podemos definir funções personalizadas usando a palavra chafe def

# Formato:
# def nome_da_funcao(parametros):
#   corpo_da_função
#   return valor

# O corpo da função deve estar indentado.

# Exemplo correto:
# def soma(x, y):
#   return x + y

# Exemplo incorreto:
# def soma(x, y):
# return x + y


# Função sem parâmetros e sem retorno
def teste():
    print("Olá, Mundo!")


# Execute a função chamando o seu nome seguido de parênteses
teste()


# Função com parâmetros e sem retorno
def mais_um(x):
    x += 1


# Função com parâmetros e com retorno
def soma(x, y):
    return x + y


# Podemos tipar os parâmetros e o retorno da função
def soma2(x: int, y: int) -> int:
    return x + y


# Podemos fornecer valores padrão para os parâmetros
# Parâmetros com valores padrão devem ser os últimos parâmetros
def soma_p(x, y = 0):
    return x + y


# Não podemos ter múltiplas funções com o mesmo nome no mesmo escopo, mesmo que os parâmetros sejam diferentes

# Encadeamento de funções
# É possível chamar uma função dentro de outra função
x = soma(10, soma(5, 5))


# podemos também especificar o nome dos parâmetros na chamada da função
x = soma(y=10, x=5)

#
# Escopo
#

# Variáveis declaradas no escopo pai são visíveis no escopo filho
x = 5


def teste2():
    print(x)


# variáveis declaradas dentro de funções são visíveis apenas no escopo da função
def teste3():
    f_x = 10
    print(f_x)


# parâmetros são visíveis apenas no escopo da função
# parâmetros ou variáveis de mesmo nome subsuem variáveis declaradas no escopo pai
def teste4(x: int):
    print(x)


def teste5():
    x = 10
    print(x)


#
# Control Flow
#


# if, elif, else são estruturas de controle de fluxo condicional
def teste6(x: int, y: int):
    z = soma(x, y)

    resposta = ""

    if z > 100:
        resposta = "maior que 100"
    elif z > 10:
        resposta = "maior que 10"
    else:
        resposta = "menor ou igual a 10"

    return resposta


# While é uma estrutura de controle de fluxo de repetição
# o while executa o bloco de código enquanto a condição for verdadeira
def print_numeros(numero: int, fim: int):
    while numero <= fim:
        print(numero)
        numero += 1


# Lista (List): Conjunto de valores ordenados, acessíveis por índice
# o índice começa em 0
carrinho = ["arroz", "feijão", "macarrão", "frango"]

# acessar um valor da lista
print(carrinho[0])

# lista vazia
lista_vazia = []

# For também é uma estrutura de controle de fluxo de repetição
# For executa o bloco de código para cada item da lista
for item in carrinho:
    print(item)

for numero in [1, 2, 3]:
    print(soma(numero, numero))

# range() é uma função nativa do Python que retorna uma lista de números
# Formato: range(fim), range(inicio, fim) ou range(inicio, fim, passo)
for i in range(5):
    print(i)

# inicio é incluso, porém fim não é incluso.
# Ou seja, range(0, 3) retona [0, 1, 2]
for i in range(0, 3):
    print(i)

for i in range(0, 10, 2):
    print(i)
