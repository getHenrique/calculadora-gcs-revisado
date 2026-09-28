# calc_estatistica.py
# Módulo B — Operações Estatísticas
# Autor: <nome do aluno>
# Branch: feature/modulo-estatistica
def media(valores):
    """Retorna a média de uma sequência de números."""
    if not valores:
        raise ValueError("O vetor não pode estar vazio.")
    return sum(valores) / len(valores)

def mediana(valores):
    """Retorna a mediana de uma sequência de números."""
    if not valores:
        raise ValueError("O vetor não pode estar vazio.")
    sorted_valores = sorted(valores)
    n = len(sorted_valores)
    if n % 2 == 0:
        return (sorted_valores[n // 2 - 1] + sorted_valores[n // 2]) / 2
    else:
        return sorted_valores[n // 2]

def desvio_padrao(valores):
    """Retorna o desvio padrão de uma sequência de números."""
    if not valores:
        raise ValueError("O vetor não pode estar vazio.")
    media_val = media(valores)
    return (sum((x - media_val) ** 2 for x in valores) / len(valores)) ** 0.5
