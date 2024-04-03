import os

#
# Tratamento de erros
#

# Exceções são erros que ocorrem durante a execução do programa.
# Elas podem ser capturadas e tratadas, para que o programa não pare de funcionar.

lista = [1, 2, 3]
try:
  # tenta acessar um índice que não existe vai gerar um IndexError
  print(lista[6])
except IndexError:
  print("Erro: esse índice não existe")

try:
  print(lista[6])
except IndexError:
  print("Erro: esse índice não existe")
else:  # podemos usar um bloco else para executar um código caso não ocorra nenhuma exceção
  print("Nenhuma exceção ocorreu")

# Se uma exceção não for tratada com try-except, o programa vai parar de funcionar e exibir uma mensagem de erro

# Podemos usar um bloco finally para executar um código após o bloco try-except, independente de ter ocorrido uma exceção ou não
try:
  print(lista[6])
except IndexError:
  print("Erro: esse índice não existe")
finally:
  # o bloco finally é executado sempre, independente de ter ocorrido uma exceção ou não
  # é executado mesmo se houver um return dentro do bloco try, ou se a exceção não for tratada, ou se houver um break
  # ou seja, é garantido que o código dentro do bloco finally será executado antes de sair do bloco try-except
  # é útil para liberar recursos, como fechar um arquivo ou uma conexão com um banco de dados
  print("O código foi executado até o final")

# Podemos criar nossas próprias exceções, herdando da classe Exception
# util para facilitar a identificação de erros específicos


class MaiorQueSeisError(Exception):
  pass


try:
  if 7 > 6:
    # raise é usado para lançar uma exceção manualmente
    raise MaiorQueSeisError("7 é maior que 6")
except MaiorQueSeisError as e:
  print(e)

#
# Arquivos
#

# Podemos abrir arquivos com with open(arquivo, modo)

with open("arquivo.txt", "r") as file:
  # o arquivo é aberto no modo leitura (r)
  # o arquivo é fechado automaticamente ao sair do bloco with
  # definimos um alias para o arquivo com as file.
  # podemos usar esse alias para chamar métodos do arquivo, como read, readline, readlines, write, etc

  # read: lê o arquivo inteiro
  print(file.read())

  # readline: lê uma linha do arquivo
  print(file.readline())

  # readlines: lê todas as linhas do arquivo e retorna uma lista com as linhas
  lines = file.readlines()
  for line in lines:
    print(line)

# podemos abrir arquivos em outros modos, como escrita (w), adição (a), binário (b), leiura e escrita (r+), etc
# especificamos o modo como o segundo argumento de open
# use encoding="utf-8" para manipular arquivos de texto com caracteres especiais, como acentos
with open("arquivo.txt", "w", encoding="utf-8") as file:
  # o arquivo é aberto no modo escrita (w)
  # o arquivo é fechado automaticamente ao sair do bloco with

  # write: escreve no arquivo
  file.write("Escrevendo no arquivo\n")

  # writelines: escreve uma lista de strings no arquivo
  file.writelines(["linha1", "linha2"])

# podemos usar o método seek para mover o cursor do arquivo para uma posição específica
# use o método tell para saber a posição atual do cursor
with open("arquivo.txt", "r", encoding="utf-8") as file:
  print(file.read(5))  # lê os primeiros 5 caracteres
  print(file.tell())  # 5
  file.seek(0)  # move o cursor para o início do arquivo
  print(file.read(5))  # lê os primeiros 5 caracteres

# podemos abrir arquivos sem o bloco with, mas é necessário fechá-los manualmente
file = open("arquivo.txt", "r", encoding="utf-8")
print(file.read())
file.close()  # é necessário fechar o arquivo manualmente

# sempre use o bloco with para abrir arquivos, pois ele garante que o arquivo será fechado corretamente, mesmo se ocorrer uma exceção

# os é um módulo que fornece funções para interagir com o sistema operacional

# __file__ é uma variável mágica do python que contém o caminho do arquivo atual
print(__file__)  # caminho completo do arquivo atual (p5_files_errors.py)

# use os.path.dirname para obter o diretório do arquivo
# se usar em conjunto com __file__, é possível obter o diretório do arquivo atual
# isso é útil para abrir arquivos de modo relativo ao arquivo atual, por exemplo
print(os.path.dirname(__file__))

# use os.path.join para juntar caminhos de arquivos
# isso é útil para garantir que o caminho seja correto, independente do sistema operacional
os.path.join(os.path.dirname(__file__), "arquivo.txt")

# use os.path.exists para verificar se um arquivo ou diretório existe
print(os.path.exists("arquivo.txt"))  # True

# use os.path.isfile para verificar se um caminho é um arquivo
print(os.path.isfile("arquivo.txt"))  # True

# use os.path.isdir para verificar se um caminho é um diretório
print(os.path.isdir(os.path.dirname(__file__)))  # True
