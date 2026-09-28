def potencia(base, expoente):
    total = 1
    while(expoente!=0):
        total = (total) * (base)
        expoente -= 1
    return total


def raiz_quadrada(numero):
    return numero ** 0.5


def raiz_cubica(num):
    return num ** (1 / 3)