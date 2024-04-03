#
# Classes e Objetos
#


# Classes são modelos para criar objetos. Objetos são instâncias de classes.
class Pessoa:
  # O método __init__ é o construtor da classe. Ele é chamado quando um objeto é criado.
  # self é uma referência ao objeto que está sendo criado.
  def __init__(self, nome, idade):
    # Atributos são variáveis que pertencem a um objeto.
    # Toda instância de Pessoa terá um atributo nome e um atributo idade próprios.
    self.nome = nome
    self.idade = idade

  # Métodos são funções que pertencem a um objeto.
  def aniversario(self):
    self.idade += 1


# Para criar um objeto, chamamos a classe como se fosse uma função.
marcos = Pessoa("Marcos", 35)

# Acessamos os atributos e métodos do objeto usando ponto.
print(marcos.nome)  # Marcos

marcos.aniversario()
print(marcos.idade)  # 36

#
# Herança
#

# A herança permite que uma classe herde atributos e métodos de outra classe.


class Aluno(Pessoa):

  def __init__(self, nome, idade, matricula):
    # super() é uma referência à classe pai.
    super().__init__(nome, idade)  # Chama o construtor da classe pai.
    self.matricula = matricula

  def estudar(self):
    print(f"{self.nome} está estudando")


# Um objeto da classe Aluno tem acesso aos atributos e métodos da classe Pessoa, pois Aluno herda de Pessoa.
joao = Aluno("João", 20, "1234")
print(joao.nome)  # João
print(joao.idade)  # 20
joao.aniversario()  # 21

joao.matricula  # 1234
joao.estudar()  # João está estudando

#
# Polimorfismo em POO
#

# Perceba que o método aniversario() da classe Pessoa é chamado a partir de um objeto da classe Aluno.
# Isso é uma característica do polimorfismo, que permite que objetos de diferentes classes sejam tratados como objetos da mesma classe pai.

# Podemos sobrescrever métodos da classe pai em uma subclasse.


class Animal:

  def __init__(self, nome):
    self.nome = nome

  def falar(self):
    raise NotImplementedError("Subclasse precisa implementar este método")


class Cachorro(Animal):
  # sobrescrevendo o método falar da classe pai
  def falar(self):
    return f"{self.nome} diz Woof!"


class Gato(Animal):
  # sobrescrevendo o método falar da classe pai
  def falar(self):
    return f"{self.nome} diz Meow!"


dog = Cachorro("Manuel")
print(dog.falar())  # Manuel diz Woof!

cat = Gato("Mingau")
print(cat.falar())  # Mingau diz Meow!

# isinstance: verificar se um objeto é uma instância de uma classe
print(isinstance(dog, Cachorro))  # True
print(isinstance(dog, Animal))  # True, pois Cachorro herda de Animal

# duck typing: "se parece com um pato, nada como um pato, então é um pato"
# em Python, não é necessário herdar de uma classe específica para que um objeto seja tratado como um tipo específico
# basta que o objeto tenha os métodos e atributos necessários para ser tratado como o tipo desejado
# isso é chamado de duck typing


class Pato:

  def nadar(self):
    return "Pato nadando"


class Galinha:

  def nadar(self):
    return "Galinha nadando"


def fazer_nadar(objeto):
  print(objeto.nadar())


# Pato e Galinha não herdam de uma mesma classe, mas ambos têm um método nadar
# portanto, ambos podem ser tratados da mesma forma
fazer_nadar(Pato())  # Pato nadando
fazer_nadar(Galinha())  # Galinha nadando


# se usar tipagem, podemos impedir que um objeto seja tratado como um tipo que ele não é
def fazer_nadar_pato(objeto: Pato):
  print(objeto.nadar())


fazer_nadar_pato(Pato())  # Pato nadando
# fazer_nadar_pato(Galinha()) # TypeError: fazer_nadar_pato() esperava um Pato, mas recebeu uma Galinha

#
# Encapsulamento
#

# proteger os atributos e métodos de uma classe para que eles não sejam acessados diretamente
# atributos e métodos privados são acessados apenas de dentro da classe
# atributos e métodos públicos são acessados de qualquer lugar

# Em Python, não existem atributos e métodos privados de fato. Tudo é público.

# No entanto, podemos usar decorators para criar getters e setters para simular o encapsulamento


class Funcionario:

  def __init__(self):
    self.__salario = 0  # no Python, por convenção, atributos privados começam com __

  # decorators são uma característica da linguagem que permitem modificar a função ou método que o segue
  # property é um decorator que cria um getter
  # getter é um método que retorna o valor de um atributo privado
  @property
  def salario(self):
    return self.__salario

  # decorator para criar um setter
  @salario.setter
  def salario(self, valor):
    raise ValueError(
        "Salário não pode ser alterado diretamente. Use o método aumentar_salario()"
    )

  # método para modificar o salário
  def aumentar_salario(self, aumento):
    if aumento < 0:
      raise ValueError("Aumento não pode ser negativo")
    self.__salario += aumento


joao = Funcionario()
joao.salario  # 0

joao.aumentar_salario(1000)
joao.salario  # 1000

# perceba que o atributo __salario não pode ser acessado ou alterado diretamente, devido aos decorators
try:
  joao.__salario  # AttributeError: 'Funcionario' object has no attribute '__salario'
except AttributeError as e:
  print(e)

try:
  # ValueError: Salário não pode ser alterado diretamente. Use o método aumentar_salario()
  joao.salario = 2000
except ValueError as e:
  print(e)

#
# atributos estáticos
#


class Conta:
  # atributos estáticos pertencem à classe, não aos objetos
  # eles são compartilhados por todos os objetos da classe
  # para acessar um atributo estático, usamos o nome da classe
  saldo_total = 0

  def __init__(self, saldo):
    self.saldo = saldo
    Conta.saldo_total += saldo

  def depositar(self, valor):
    self.saldo += valor
    Conta.saldo_total += valor

  def sacar(self, valor):
    if valor > self.saldo:
      raise ValueError("Saldo insuficiente")
    self.saldo -= valor
    Conta.saldo_total -= valor


print(Conta.saldo_total)  # 0

nova_conta = Conta(1000)
print(Conta.saldo_total)  # 1000

outra_conta = Conta(500)
print(Conta.saldo_total)  # 1500
