# calc_percentual
# Módulo C — Operações de porcentagem

PORCENTO = 100


def porcentagem(valor_referente, percentual_referencia):


    return (valor_referente * percentual_referencia) / PORCENTO


def acrescer(valor_referente, percentual_acrescimo):


    return valor_referente + porcentagem(valor_referente, percentual_acrescimo)


def descontar(valor_referente, percentual_desconto):

    
    return valor_referente - porcentagem(valor_referente, percentual_desconto)