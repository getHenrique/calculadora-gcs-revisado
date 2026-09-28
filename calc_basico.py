# calc_basico.py
# Módulo A — Operações Básicas
# Autor: <nome do aluno>
# Branch: feature/modulo-basico


def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença de a e b."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de a por b.
    Lança ValueError se b == 0."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Impossível dividir por zero")