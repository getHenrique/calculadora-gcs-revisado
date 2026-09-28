def percentual(numero, percentual):
    return numero * percentual / 100;

def acrescimo(numero, acrescimo):
    return numero + percentual(numero, acrescimo);

def desconto(numero, desconto):
    return numero - percentual(numero, desconto);