# value_inputs


def get_single_float(prompt = "X = "):
    """
    Solicita um número ao usuário até que uma entrada válida seja fornecida.
    """

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números reais.")


def get_two_floats(prompt_a = "A = ", prompt_b = "B = "):
    """
    Solicita dois números ao usuário até que entradas válidas sejam fornecidas.
    """

    while True:
        try:
            value_a = float(input(prompt_a))
            value_b = float(input(prompt_b))
            return value_a, value_b
        except ValueError:
            print("Entrada inválida! Por favor, insira apenas números reais.")


def get_number_set(prompt = "Insira os números do conjunto separados por espaço:\n"):
    """
    Solicita uma lista de números separados por espaço e garante a conversão correta.
    """

    while True:
        user_input = input(prompt).split()
        if not user_input:
            print("O conjunto não pode estar vazio. Tente novamente.")
            continue
        try:
            number_set = [float(value) for value in user_input]
            return number_set
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir apenas números reais separados por espaço.")