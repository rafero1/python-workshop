# Isso é um comentário. No Python, inicie comentários usando #
# Use comentários quando necessário, porém evite o uso excessívo
# Almeje escrever código legível, funcional, eficiêntel, com funções e variáveis auto-explicativas e de fácil entendimento

#
# Variáveis
#

# Declaração de variável
# Formato:
# nome: tipo (opcional) = valor
nome = "valor"
nome2: str = "valor"

# No Python, nomes de variáveis ou funções devem começar com letras ou _
_nome = "valor"

# Declaração de variável sem atribuíção de valor: Use tipagem ou inicie com valor None
nome3: str
nome4 = None

# É possível reatribuir uma variável já declarada.
nome = "valor"
nome = "outro valor"
nome = "mais um valor"

# Isso é possível pois as variáveis são apenas referências para valores guardados em memória

# Também podemos fazer atribuição usando outras variáveis
nome1 = "valor1"
nome2 = nome1  # nome2 é atribuído o mesmo valor de nome1

# Se nome1 for reatribuido, um novo objeto será criado em memória para ele.
# Dessa forma, nome2 ainda será = "valor1"
nome1 = "outro valor"

# Exceções: Objetos mutáveis, como listas.

# No Python, busque seguir a nomenclatura snake_case

#
# Tipos Básicos
#

# int (Inteiro): Números inteiros, positivos ou negativos.
x = 10
y = 5

# float (Ponto flutuante): Números decimais, positivos ou negativos
pi = 3.1415926535

# bool (Booleano): Valores lógicos, verdadeiro ou falso
ativo = True
off = False

# str (String): Texto, sequência de caracteres
nome = "Marcos"
email = "oqibz@example.com"
endereco = "Rua da Paz, 123"

# None (Nenhum): Valor nulo, sem valor
nulo = None

# Reatribuição de variável com mudança de tipo
# Isso é possível pois Python é uma linguagem com tipagem dinâmica
# Tente evitar, pois pode gerar erros e confusão
nome1 = "valor"
nome1 = 10
nome1 = True

# Operações básicas
z = 10 + 5
z = 10 - 5
z = 20 * 2  # multiplicação
z = 9 / 3  # divisão
z = 9 % 3  # resto da divisão
z = 2**6  # potência


# Operações com variáveis
x = 10
y = 20
z = x + y  # z = 10 + 20

# Operações com strings
batman = "bat" + "man"
nome_pessoal = "Marcos"
nome_familia = "da Silva"
nome_completo = nome_pessoal + " " + nome_familia

# Syntactic sugar de operações com redefinição
# x += y é um atalho equivalente a x = x + y
x += y
x -= y
x *= y
x /= y
x %= y
x **= y

# Operações de comparação. Atribui a variável uma booleana (True ou False) que representa o resultado da comparação.
z = 20 == 20
z = x != y
z = 15 > 20
z = 15 < 20
z = x >= y
z = x <= y

# Operações lógicas (and, or, not)
z = 20 > 20 and 20 > 15
z = 20 > 20 or 20 > 15
z = not True

# Operações de identidade
# Checa se os objetos referênciados pelas variáveis são os mesmos
z = x is y
z = x is not y
