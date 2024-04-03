# Bibliotecas e Modulos
# O Python possui uma grande quantidade de bibliotecas e módulos nativos que podem ser importados e utilizados em seus programas.

# Abaixo, importamos as funções randint(), choice() e shuffle() do módulo random.
from random import randint, choice, shuffle

#
# Operações e funções com strings
#

nome = "Marcos"
nome_completo = nome + " da " + "Silva"

# slicing: pegar partes de uma string usando índices
# [inicio:fim:passo]
inicial = nome[0]
ultima_letra = nome[-1]
tres_primeiras = nome[:3]
segunda_terceira = nome[1:3]

# iterar uma string caractere por caractere
for letra in "Marcos":
  print(letra)  # M, a, r, c, o, s

# split: separar uma string em uma lista de substrings usando um caractere de separação
# ["54", "23", "12", "73", "85", "24"]
numeros = "54,23,12,73,85,24".split(",")

# join: juntar uma lista de strings em uma única string usando um caractere de junção
# "54,23,12,73,85,24"
numeros = ",".join(["54", "23", "12", "73", "85", "24"])
nome_lista = "Marcos da Silva".split(" ")  # ["Marcos", "da", "Silva"]

# in: verificar se uma string contém outra
nome = "Marcos da Silva"
da_silva = "Silva" in nome  # True
joao = "João" in nome  # False

# upper, lower: caixa alta e caixa baixa
caixa_alta = nome.upper()
caixa_baixa = nome.lower()

# replace: substituir uma substring por outra
nome = "Marcos da Silva"
nome = nome.replace("Marcos", "João")  # "João da Silva"

# len: tamanho de uma string (numero de caracteres)
tamanho = len("Marcos")  # 6

x = 5
y = 3
pi = 3.14159

# F-strings
nome_completo = f"{nome} da Silva"
pi_string = f"Os primeiros três valores de pi é {pi: .3f}"
f_operation = f"A operação {x} + {y} resulta em {x + y}"

#
# Estruturas de Dados
#

# Listas: listas são coleções ordenadas de valores. Podem conter valores de qualquer tipo. Mutáveis.
lista = [1, 2, 3, 4, 5]
lista.append(6)  # adiciona um valor ao final da lista
lista.insert(0, 0)  # insere o valor 0 na posição 0
lista.remove(3)  # remove o valor 3 da lista

# pop(x) remove o valor no índice x da lista e o retorna
# se x não for especificado, remove o último valor da lista
lista = [1, 2, 3, 4, 5, 6]
valor = lista.pop()  # 6
valor = lista.pop(0)  # 1

# operações com listas
lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
rs = lista + lista2  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.extend(lista2)  # lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# slicing: novamente, podemos pegar partes de uma lista usando índices
lista = [1, 2, 3, 4, 5]
primeiro = lista[0]
ultimos_tres = lista[-3:]
dois_ultimos = lista[-2:]
meio = lista[1:4]

# reverse: inverte a ordem dos valores na lista in-place (modifica a lista original)
lista = [1, 2, 3, 4, 5]
lista.reverse()  # [5, 4, 3, 2, 1]

# sort: ordena os valores da lista in-place (modifica a lista original)
lista = [5, 3, 1, 4, 2]
lista.sort()  # [1, 2, 3, 4, 5]
lista.sort(reverse=True)  # [5, 4, 3, 2, 1]

# novamente, len retorna o tamanho de uma lista ou objeto iterável (string, lista, set, etc)
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)  # 5

# unpacking: tecnica para atribuir valores de uma lista a variáveis
endereco = "Rua das Flores, 123, Bairro das Rosas"
# rua = "Rua das Flores", numero = "123", bairro = "Bairro das Rosas"
rua, numero, bairro = endereco.split(", ")

# Sets: são como listas, mas não podem conter valores duplicados. Não são ordenados. Mutáveis.
# Lembra da teoria dos conjuntos da matemática?

set1 = {1, 2, 3, 4, 5}
set1.add(6)  # adicionar um valor
set1.update({7, 8, 9})  # adicionar vários valores de uma vez
set1.remove(3)  # remove um valor. Erro se o valor não existir
set1.discard(10)  # remover um valor, sem erro se o valor não existir

# remove valores de um set que estão em outro set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
diferenca = set1 - set2  # {1, 2}
diferenca = set1.difference(set2)  # {1, 2}

# União: adiciona valores de um set que não estão em outro set
uniao = set1.union(set2)  # {1, 2, 3, 4, 5, 6, 7}
uniao = set1 | set2  # {1, 2, 3, 4, 5, 6, 7}

# Interseção: valores que estão em ambos os sets
intersecao = set1.intersection(set2)  # {3, 4, 5}
intersecao = set1 & set2  # {3, 4, 5}

# Tuplas: são como listas, mas imutáveis. Ou seja, não podem ser alteradas.
# Uteis em situações onde você não quer que os valores sejam alterados
tupla = ("maçã", "abobora", "uva")
tupla[0]  # "maçã"

# unpacking
valor1, valor2, valor3 = (1, 2, 3)
rs = valor1 + valor2 + valor3  # 6

# Dicionários
# Dicionários são como listas, mas os valores são acessados por chaves
# Cada chave é única, e pode ser de qualquer tipo imutável (string, número, etc)
# Utilize dicionários para armazenar valores que são relacionados entre si

pessoa = {"nome": "Marcos", "idade": 35}
pessoa["nome"]  # "Marcos"
pessoa["idade"]  # 35

# adicionar um novo par chave-valor ao dicionário
pessoa["profissão"] = "programador"

# alterar um valor no dicionário
pessoa["idade"] = pessoa["idade"] + 1

# remover um par chave-valor
del pessoa["profissão"]


def print_dicionario(dicionario: dict):
  # items() retorna uma lista de tuplas (chave, valor)
  for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")


print_dicionario(pessoa)

# List Comprehension (Compreensão de Listas)
# é uma forma concisa de criar listas a partir de outras listas
lista = [1, 2, 3, 4, 5]
lista_dobro = [numero * 2 for numero in lista]  # [2, 4, 6, 8, 10]

# pode ser usado para filtrar valores com base em uma condição
pares = [numero for numero in lista if numero % 2 == 0]  # [2, 4]

# set comprehension
set1 = {1, 2, 3, 4, 5}
set_dobro = {numero * 2 for numero in set1}  # {2, 4, 6, 8, 10}

# tuple comprehension
tupla1 = (1, 2, 3, 4, 5)
tupla_dobro = (numero * 2 for numero in tupla1)  # (2, 4, 6, 8, 10)

# dict comprehension
pesos = {"marcos": 70, "vinicius": 80, "maria": 60}
pesos_maiores_que_70 = {
    nome: peso
    for nome, peso in pesos.items() if peso > 70
}  # {"vinicius": 80}
