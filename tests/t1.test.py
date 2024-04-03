from do_test import do_test
from t1 import t_somar, t_adicionar_titulo, t_esta_entre, t_maior_que, t_par, t_subtrair

# função usada para testar vários casos
do_test(t_somar, ((1, 2), 3), ((5, 5), 10), ((-99, 1), -98))

do_test(t_subtrair, ((2, 1), 1), ((5, 5), 0), ((-99, 1), -100))

do_test(t_maior_que, ((5, 1), True), ((5, 5), False), ((0.5, 1), False))

do_test(t_esta_entre, ((3, 1, 5), True), ((3, 5, 1), False),
        ((3, 3, 3), False), ((5, 5, 50), False), ((10, 1, 10), False))

do_test(t_par, (2, True), (1, False), (-7, False))

do_test(t_adicionar_titulo, (("Marcos", "Sr."), "Sr. Marcos"),
        (("Anilda", "Sra."), "Sra. Anilda"))
