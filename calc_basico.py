# calc_basico
# Módulo A — Operações Básicas

def somar(parcela_a, parcela_b):
    """
    Retorna a soma da parcela a pela parcela b.
    """
    return parcela_a + parcela_b


def subtrair(minuendo, subtraendo):
    """
    Retorna a diferença do minuendo pelo subtraendo.
    """
    return minuendo - subtraendo


def multiplicar(fator_a, fator_b):
    """
    Retorna o produto do fator a pelo fator b.
    """
    return fator_a * fator_b

def dividir(dividendo, divisor):
    """
    Retorna a divisão do dividendo pelo divisor.
    Lança ZeroDivisionError se b == 0.
    """
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        print("Impossível dividir por zero")