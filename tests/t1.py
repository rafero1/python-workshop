from do_test import do_test

# complete as funções abaixo
# substitua "raise NotImplementedError" pelo seu código


# exemplo já pronto
def t_somar(x, y):
    """ Deve retornar a soma de x e y """
    return x + y


# função usada para testar vários casos
do_test(t_somar, ((1, 2), 3), ((5, 5), 10), ((-99, 1), -98))


def t_subtrair(x, y):
    """ Deve retornar a subtração de x e y """
    raise NotImplementedError


do_test(t_subtrair, ((2, 1), 1), ((5, 5), 0), ((-99, 1), -100))


def t_maior_que(x, y):
    """ Deve retornar True se o valor de x for maior que y, False caso contrário """
    raise NotImplementedError


do_test(t_maior_que, ((5, 1), True), ((5, 5), False), ((0.5, 1), False))


def t_esta_entre(z, x, y):
    """ Deve retornar True se o valor de z estiver entre x e y, False caso contrário """
    raise NotImplementedError


do_test(t_esta_entre, ((3, 1, 5), True), ((3, 5, 1), False),
        ((3, 3, 3), False), ((5, 5, 50), False), ((10, 1, 10), False))


def t_par(x):
    """ Deve retornar True se o valor de x for par, False caso contrário """
    raise NotImplementedError


do_test(t_par, (2, True), (1, False), (-7, False))


def t_adicionar_titulo(nome, titulo):
    """ Deve retornar um nome completo no formato "titulo nome" """
    raise NotImplementedError


do_test(t_adicionar_titulo, (("Marcos", "Sr."), "Sr. Marcos"),
        (("Anilda", "Sra."), "Sra. Anilda"))
