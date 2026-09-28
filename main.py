# main.py — importa módulos conforme são mergeados na main
def menu():

    user_input = '0'

    print("=== Calculadora GCS ===\n")

    while user_input != 'x' :
        
        user_input = input(
            "a - Básico\n" \
            "b - Potência\n" \
            "c - Percentual\n" \
            "d - Estatística\n" \
            "e - Conversão\n" \
            "x - Sair\n"
            ">> "
        )

        match user_input :
            case 'a' :
                
                try:

                    from calc_basico import somar, subtrair, multiplicar, dividir
                    print("\nMódulo Básico carregado.\n")
                    
                    while user_input != '5' :

                        user_input = input(    
                            "1 - Somar\n" \
                            "2 - Subtrair\n" \
                            "3 - Multiplicar\n" \
                            "4 - Dividir\n"
                            "5 - Cancelar operação\n" \
                            ">> "
                        )

                        match user_input :
                            case '1' :
                                print("\nSomando A + B")
                                print(
                                    "A + B = ",
                                    somar(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '2' :
                                print("\nSubtraindo A - B")
                                print(
                                    "A - B = ",
                                    subtrair(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '3' :
                                print("\nMultiplicando A * B")
                                print(
                                    "A * B = ",
                                    multiplicar(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '4' :
                                print("\nDividindo A / B")
                                print(
                                    "A / B = ",
                                    dividir(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '5' :
                                print("Saindo do módulo...\n")
                            case _ :
                                print("Input inválido\n")
                    
                except ImportError:
                    
                    print("Módulo Básico ainda não disponível.\n")

            case 'b' :

                try:

                    from calc_potencia import potencia, raiz_quadrada, raiz_cubica
                    print("Módulo Potência carregado.\n")

                    while user_input != '4' :

                        user_input = input(    
                            "1 - Potência\n" \
                            "2 - Raiz Quadrada\n" \
                            "3 - Raiz Cúbica\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )

                        match user_input :
                            case '1' :
                                print("\nPotência de A^B")
                                print(
                                    "A^B = ",
                                    potencia(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '2' :
                                print("\nRaiz quadrada de X")
                                print(
                                    "√X = ",
                                    raiz_quadrada(float(input("X = "))),
                                    "\n"
                                )
                            case '3' :
                                print("\nRaiz cúbica de X")
                                print(
                                    "∛X = ",
                                    raiz_cubica(float(input("X = "))),
                                    "\n"
                                )
                            case '4' :
                                print("Saindo do módulo...\n")
                            case _ :
                                print("Input inválido\n")

                except ImportError:

                    print("Módulo Potência ainda não disponível.\n")
                    
            case 'c' :

                try:

                    from calc_percentual import percentual, acrescimo, desconto
                    print("Módulo Percentual carregado.\n")

                    while user_input != '4' :

                        user_input = input(    
                            "1 - Percentual\n" \
                            "2 - Acréscimo\n" \
                            "3 - Desconto\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )

                        match user_input :
                            case '1' :
                                print("\nPercentual Y de X")
                                print(
                                    "Y% de X = ",
                                    percentual(
                                        float(input("X = ")),
                                        float(input("Y% = "))
                                    ),
                                    "\n"
                                )
                            case '2' :
                                print("\nAcrescentar percentual Y à X")
                                print(
                                    "X + (X de Y%) = ",
                                    acrescimo(
                                        float(input("X = ")),
                                        float(input("Y% = "))
                                    ),
                                    "\n"
                                )
                            case '3' :
                                print("\nDescontar percentual Y de X")
                                print(
                                    "X - (X de Y%) = ",
                                    desconto(
                                        float(input("X = ")),
                                        float(input("Y% = "))
                                    ),
                                    "\n"
                                )
                            case '4' :
                                print("Saindo do módulo...\n")
                            case _ :
                                print("Input inválido\n")

                except ImportError:

                    print("Módulo Percentual ainda não disponível.\n")

            case 'd' :

                try:

                    from calc_estatistica import media, mediana, desvio_padrao
                    print("Módulo Estatística carregado.\n")

                    while user_input != '4' :

                        user_input = input(    
                            "1 - Média\n" \
                            "2 - Mediana\n" \
                            "3 - Desvio Padrão\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )

                        match user_input :
                            case '1' :
                                print("\nMédia de um conjunto de números")
                                conjunto_estatistica = input("Insira os números da conjunto separados por espaço:\n").split()
                                conjunto_estatistica = [float(x) for x in conjunto_estatistica]
                                print("Média de ", conjunto_estatistica, " = ", media(conjunto_estatistica), "\n")
                            case '2' :
                                print("\nMediana de uma conjunto de números")
                                conjunto_estatistica = input("Insira os números da conjunto separados por espaço:\n").split()
                                conjunto_estatistica = [float(x) for x in conjunto_estatistica]
                                print("Mediana de ", conjunto_estatistica, " = ", mediana(conjunto_estatistica), "\n")
                            case '3' :
                                print("\nDesvio padrão populacional de uma conjunto de números")
                                conjunto_estatistica = input("Insira os números da conjunto separados por espaço:\n").split()
                                conjunto_estatistica = [float(x) for x in conjunto_estatistica]
                                print("Desvio Padrão populacional de ", conjunto_estatistica, " = ", desvio_padrao(conjunto_estatistica), "\n")
                            case '4' :
                                print("Saindo do módulo...\n")
                            case _ :
                                print("Input inválido\n")
                        
                except ImportError:

                    print("Módulo Estatística ainda não disponível.\n")

            case 'e' :

                try:

                    from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
                    print("Módulo Conversão carregado.\n")

                    while user_input != '4' :

                        user_input = input(    
                            "1 - Celsisus para Fahrenheit\n" \
                            "2 - km para milhas\n" \
                            "3 - kg para libras\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )

                        match user_input :
                            case '1' :
                                print("\nXºC para XºF")
                                print(
                                    "XºF = ",
                                    celsius_para_fahrenheit(
                                        float(input("XºC = ")),
                                    ),
                                    "\n"
                                )
                            case '2' :
                                print("\nXkm para X milhas")
                                print(
                                    "X milhas = ",
                                    km_para_milhas(
                                        float(input("Xkm = ")),
                                    ),
                                    "\n"
                                )
                            case '3' :
                                print("\nXkg para X libras")
                                print(
                                    "X libras = ",
                                    kg_para_libras(
                                        float(input("Xkg = ")),
                                    ),
                                    "\n"
                                )
                            case '4' :
                                print("Saindo do módulo...\n")
                            case _ :
                                print("Input inválido\n")

                except ImportError:

                    print("Módulo Percentual ainda não disponível.\n")

            case 'x' :
                print("Tenha um ótimo dia! :)")
                break
            case _ :
                print("Input inválido\n")

if __name__ == "__main__":
    menu()

