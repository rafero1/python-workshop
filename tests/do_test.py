class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def do_test(func, *assertions):
    func_name = func.__name__

    print(f"Testando {func_name}:")

    result = None

    for args, expected in assertions:
        try:
            result = func(args) if len(func.__code__.co_varnames) == 1 else func(
                *args)
            assert result == expected

        except NotImplementedError:
            print(f"{bcolors.WARNING}Não implementado.{bcolors.ENDC}\n")
            return

        except AssertionError:
            print(
                f"{func_name}{args} == {expected} {
                    bcolors.FAIL}Falha!{bcolors.ENDC}"
            )
            print(f"  {bcolors.FAIL}Esperado: {expected}{bcolors.ENDC}")
            print(f"  {bcolors.FAIL}Obtido: {result}{bcolors.ENDC}\n")
            return

        print(
            f"{func_name}{args} == {expected} {bcolors.OKGREEN}OK!{bcolors.ENDC}")

    print(f"{bcolors.OKGREEN}{func_name} OK!{bcolors.ENDC}\n")


def do_test_void(func, *assertions):
    func_name = func.__name__

    print(f"Testando {func_name}:")

    for args in assertions:
        try:
            func(args) if len(func.__code__.co_varnames) == 1 else func(*args)

        except NotImplementedError:
            print(f"{bcolors.WARNING}Não implementado.{bcolors.ENDC}\n")
            return

    print("\n")
