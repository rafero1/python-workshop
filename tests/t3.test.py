from do_test import do_test, do_test_void
from t3 import t_add_sufix_lista, t_busca_linear, t_contagem_char, t_dict_invertido, t_fatorial, t_peso_medio, t_print_fatorial, t_print_impares_entre, t_print_lista, t_set_diferenca, t_verificar_senha

do_test_void(t_print_impares_entre, (0, 10), (11, 111))
do_test_void(t_print_lista, ["a", "b", "c"], [1, 2, 3])

do_test(t_add_sufix_lista, ((["a", "b", "c"], "!"), ["a!", "b!", "c!"]),
        (([1, 2, 3], "x"), ["1x", "2x", "3x"]))

do_test(t_busca_linear, (("molho", ["carne", "macarrão", "molho"]), 2),
        (("frango", ["carne", "macarrão", "molho"]), -1))

do_test(t_contagem_char, ((["a", "ba", "c"], "a"), 2),
        ((["aranha", "banana", "cachorro"], "a"), 7))

do_test(t_fatorial, (5, 120), (10, 3628800), (4, 24))

do_test_void(t_print_fatorial, 5, 7)

do_test(t_dict_invertido, ({
    "a": 1,
    "b": 2
}, {
    1: "a",
    2: "b"
}), ({
    "a": "x",
    "b": "y"
}, {
    "x": "a",
    "y": "b"
}))

do_test(t_set_diferenca, ({1, 2, 3}, {3, 4}, {1, 2}),
        ({1, 2, 3}, {1, 2, 3}, set()), ({1, 2, 3}, {4, 5}, {1, 2, 3}))

do_test(t_peso_medio, ([70, 80, 60], 70), ([100, 200, 300], 200),
        ([1, 2, 3], 2))

do_test(t_verificar_senha, ("Abc123!@", True), ("abc123", False),
        ("Abc123", False), ("Abc123@", False), ("Abc123!@a", False))
