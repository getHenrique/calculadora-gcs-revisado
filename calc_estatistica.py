# calc_estatistica
# Módulo D — Operações Estatísticas

from calc_potencia import raiz_quadrada


def media(conjunto):


    """ Retorna a média de um conjunto de números.
    """

    if not conjunto:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return sum(conjunto) / len(conjunto)


def mediana(conjunto):


    """ Retorna a mediana de um conjunto de números.
    """

    if not conjunto:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        conjunto_ordenado = sorted(conjunto)
        tamanho_conjunto = len(conjunto_ordenado)
        if (tamanho_conjunto % 2) == 0:
            return (conjunto_ordenado[(tamanho_conjunto // 2) - 1] + conjunto_ordenado[tamanho_conjunto // 2]) / 2
        else:
            return conjunto_ordenado[tamanho_conjunto // 2]


def desvio_padrao(conjunto):

    
    """ Retorna o desvio padrão de um conjunto de números.
    """

    if not conjunto:
        raise ValueError("O conjunto não pode estar vazio.")
    else:
        return raiz_quadrada(
            sum(
                ((valor - media(conjunto)) ** 2) for valor in conjunto
            ) / len(conjunto)
        )
