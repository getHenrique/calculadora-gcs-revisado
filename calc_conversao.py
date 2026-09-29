# calc_conversao
# Módulo E — Operações de Conversão

FATOR_ESCALAR_CELSIUS_FAHRENHEIT = 9 / 5
DESLOCAMENTO_CELSIUS_FAHRENHEIT = 32
QUILOMETROS_EM_MILHAS = 0.621371
QUILOGRAMAS_EM_LIBRAS = 2.20462


def converter_celsius_fahrenheit(temperatura_celsius):
    return (temperatura_celsius * FATOR_ESCALAR_CELSIUS_FAHRENHEIT) + DESLOCAMENTO_CELSIUS_FAHRENHEIT

def converter_quilometros_milhas(distancia_quilometros):
    return distancia_quilometros / QUILOMETROS_EM_MILHAS

def converter_quilogramas_libras(peso_quilogramas):
    return peso_quilogramas * QUILOGRAMAS_EM_LIBRAS