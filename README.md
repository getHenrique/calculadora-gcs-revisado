# REFATORAÇÃO PARA CÓDIGO LIMPO  
# CALCULADORA GCS - LABORATÓRIO COLABORATIVO  
---
## ~~Gerência de Configuração de Software com Git Flow~~
## Avaliação 1 - Manutenção de Software
### ~~Prof. Dr. Márcio Silva  ~~
### Prof. Rodrigo Funabashi Jorge
---
Mantenedor: Henrique Dias Albernaz  
Desenvolvedores:  
- Grazyelly Wenz  
- Henrique Dias  
- José Roland  
- Kauã Rios  
Revisão: Henrique Dias Albernaz  
  
Link para o repositório original: [https://github.com/getHenrique/calculadora-gcs](https://github.com/getHenrique/calculadora-gcs)  
Link para o repositório revisado:   

## Guia de Estilo  
O guia de estilo utilizado para revisar e refatorar este projeto é o ***PEP 8 – Style Guide for Python Code***. O guia pode ser encontrado [aqui]([PEP 8 – Style Guide for Python Code | peps.python.org](https://peps.python.org/pep-0008/)).
## Glossário  

| Termo                                          | Definição                                                                                                                                                  |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operando                                       | Qualquer valor, constante ou variável fornecida como dado de entrada para o processamento de um cálculo.                                                   |
| Operação                                       | A regra de cálculo ou função matemática/computacional executada sobre um ou mais operandos para gerar um resultado.                                        |
| Parcela                                        | Cada um dos operandos numéricos fornecidos em uma operação de adição.                                                                                      |
| Adição                                         | A operação matemática fundamental que combina duas ou mais parcelas para obter um valor total.                                                             |
| Soma (Somar)                                   | O resultado final da operação de adição, ou a ação de executar a adição de duas ou mais parcelas.                                                          |
| Minuendo                                       | O valor inicial do qual um montante será subtraído (o primeiro operando da subtração).                                                                     |
| Subtraendo                                     | O valor que será deduzido do minuendo (o segundo operando da subtração).                                                                                   |
| Subtração (Subtrair)                           | A operação de deduzir o subtraendo do minuendo.                                                                                                            |
| Fator                                          | Cada um dos operandos numéricos em uma operação de multiplicação.                                                                                          |
| Multiplicação (Multiplicar)                    | A operação de calcular o produto de dois ou mais fatores, equivalente a adições repetidas.                                                                 |
| Dividendo                                      | O valor numérico base que será dividido em partes iguais.                                                                                                  |
| Divisor                                        | O valor pelo qual o dividendo será dividido. Deve, necessariamente, ser diferente de zero.                                                                 |
| Divisão (Dividir)                              | A operação que determina quantas vezes o divisor está contido no dividendo, resultando no quociente.                                                       |
| Base                                           | O número que será multiplicado por si mesmo repetidamente em uma operação de potenciação.                                                                  |
| Expoente                                       | O número que indica a quantidade de vezes que a base será usada como fator (multiplicada por si mesma).                                                    |
| Potenciação (Exponenciar)                      | A operação matemática de elevar uma base à potência indicada por um expoente.                                                                              |
| Radicando                                      | O número do qual se deseja extrair a raiz.                                                                                                                 |
| Expoente de Raiz Quadrada                      | O valor constante ($0{,}5$ ou $1/2$) utilizado como expoente na potenciação para equivaler à extração da raiz quadrada de um radicando.                    |
| Raiz quadrada                                  | A operação que encontra o valor que, quando elevado a 2 (quadrado), resulta no radicando.                                                                  |
| Expoente de Raiz Cúbica                        | O valor constante ($1/3$ ou aproximadamente $0{,}333...$) utilizado como expoente na potenciação para equivaler à extração da raiz cúbica de um radicando. |
| Raiz Cúbica                                    | A operação que encontra o valor que, quando elevado a 3 (cubo), resulta no radicando.                                                                      |
| Razão                                          | A relação de divisão entre dois valores, expressando a proporção de um em relação ao outro (ex: frações, taxas).                                           |
| Valor referente                                | O valor principal sobre o qual os cálculos de porcentagem serão aplicados.                                                                                 |
| Taxa                                           | A proporção a ser aplicada sobre um valor referente para calcular variações ou fatias.                                                                     |
| Porcento                                       | A constante numérica fixa (100) utilizada como denominador ou razão base na conversão de taxas para calculo proporcional.                                  |
| Percentual (de referência)                     | A taxa (fração de 100) aplicada ao valor referente para extrair uma fatia desse total.                                                                     |
| Porcentagem                                    | A operação que aplica um porcentual a um valor referente.                                                                                                  |
| Acréscimo (Acrescer)                           | A ação de adicionar um valor adicional (derivado de um percentual) ao valor referente.                                                                     |
| Percentual (de acréscimo)                      | A taxa utilizada para calcular o valor extra que será somado ao valor referente (ex: juros, taxas).                                                        |
| Desconto (Descontar)                           | A ação de subtrair um valor dedutível (derivado de um percentual) do valor referente.                                                                      |
| Percentual (de desconto)                       | A taxa utilizada para calcular o valor que será abatido/subtraído do valor referente.                                                                      |
| Conjunto                                       | Uma coleção de valores numéricos de entrada usados para cálculos estatísticos.                                                                             |
| Média                                          | O valor central (média aritmética) obtido pela soma de todos os itens do conjunto, dividida pela quantidade de itens.                                      |
| Mediana                                        | O valor que ocupa a posição central do conjunto quando seus elementos estão ordenados; divide os dados ao meio.                                            |
| Desvio Padrão                                  | A medida de dispersão estatística que indica o quanto os valores do conjunto variam em relação à média.                                                    |
| Temperatura (Celsius)                          | Unidade de medida de temperatura métrica fornecida como *input* para o serviço de conversão térmica.                                                       |
| Fator escalar Celsius e Fahrenheit (constante) | O fator multiplicativo constante (1,8 ou 9/5) que representa a diferença na escala entre os dois sistemas de temperatura.                                  |
| Deslocamento (constante)                       | O valor de compensação constante (32) usado para alinhar os pontos de congelamento/zero dos dois sistemas térmicos.                                        |
| Converter Celsius para Fahrenheit              | A operação que transforma a temperatura métrica (Celsius) em seu equivalente imperial (Fahrenheit).                                                        |
| Distância (quilômetros)                        | Unidade de medida de distância do sistema métrico, usada como entrada para conversão espacial.                                                             |
| Quilômetros em milhas (constante)              | O fator de conversão de distância constante (aprox. 0,621371) aplicado no cálculo de conversão de quilômetros para milhas.                                 |
| Converter quilômetros em milhas                | A operação de dividir o valor em quilômetros pela constante de milhas para obter a distância imperial equivalente.                                         |
| Peso (quilogramas)                             | Unidade de medida de massa usada como entrada para conversão de peso.                                                                                      |
| Quilogramas em libras (constante)              | O fator de conversão de massa constante (aprox. 2,20462) aplicado no cálculo de conversão de quilogramas para libras.                                      |
| Converter quilogramas em libras                | A operação de multiplicar a massa em quilogramas pela constante de libras para obter o peso imperial equivalente.                                          |
| Módulo (sistema)                               | Um componente isolado do sistema que agrupa um domínio específico (ex: Módulo de Potência, de Estatística).                                                |
| Entrada de usuário                             | Qualquer dado de entrada (operandos, constantes providas, arrays) inserido pelo usuário no sistema para processamento.                                     |
  
## Descrição do sistema

| Módulo          | Arquivo             | Funções a implementar                                         | Autor     |
| --------------- | ------------------- | ------------------------------------------------------------- | --------- |
| A — Básico      | calc_basico.py      | somar(), subtrair(), multiplicar(), dividir()                 | Henrique  |
| B — Potência    | calc_potencia.py    | potencia(), raiz_quadrada(), raiz_cubica()                    | Grazyelly |
| C — Percentual  | calc_percentual.py  | percentual(), acrescimo(), desconto()                         | José      |
| D — Estatística | calc_estatistica.py | media(), mediana(), desvio_padrao()                           | Kauã      |
| E — Conversão   | calc_conversao.py   | celsius_para_fahrenheit(), km_para_milhas(), kg_para_libras() | Grazyelly |
| Menu            | main.py             | Menu inicial para acessar aos demais módulos                  | Henrique  |


