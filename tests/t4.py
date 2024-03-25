from do_test import do_test, do_test_void

# complete as classes abaixo
# substitua "raise NotImplementedError" pelo seu código


class TPessoa:
    """
    Crie uma classe Pessoa com os atributos nome, sobrenome, idade

    Crie um método aniversario() que incrementa a idade da pessoa em 1
    Crie um método iniciais() que retorna as iniciais do nome e sobrenome da pessoa
    """

    def __init__(self):
        raise NotImplementedError

    def aniversario(self):
        raise NotImplementedError


class TDisciplina:
    """
    Crie uma classe Disciplina com os atributos nome, professor

    Crie um método __str__ que retorna o nome da disciplina
    """

    def __init__(self):
        raise NotImplementedError


class TAluno(TPessoa):
    """
    Crie uma classe Aluno que herda da classe Pessoa e tem um atributo matricula e uma lista de disciplinas

    Crie um método estudar() que imprime "{nome} está estudando {disciplinas}"
    Crie um método adicionar_disciplina(disciplina) que adiciona uma disciplina à lista de disciplinas
    Crie um método professores() que retorna uma lista com os professores das disciplinas do aluno, sem repetição
    """

    def __init__(self):
        raise NotImplementedError

    def estudar(self):
        raise NotImplementedError

    def adicionar_disciplina(self, disciplina):
        raise NotImplementedError

    def professores(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass
