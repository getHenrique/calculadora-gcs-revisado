# main menu

def menu():


    user_input = '0'

    print("\n=== Calculadora GCS ===\n")

    while user_input != 'x':
        user_input = input(
            "a - Básico\n" \
            "b - Potência\n" \
            "c - Percentual\n" \
            "d - Estatística\n" \
            "e - Conversão\n" \
            "x - Sair\n" \
            ">> "
        )

        match user_input:
            case 'a':
                try:
                    from calc_basics import add, subtract, multiply, divide
                    print("\nMódulo Básico carregado.\n")
                    
                    while user_input != '5':
                        user_input = input(    
                            "1 - Somar\n" \
                            "2 - Subtrair\n" \
                            "3 - Multiplicar\n" \
                            "4 - Dividir\n"
                            "5 - Cancelar operação\n" \
                            ">> "
                        )
                        match user_input:
                            case '1':
                                print("\nSomando A + B")
                                print(
                                    "A + B = ",
                                    add(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '2':
                                print("\nSubtraindo A - B")
                                print(
                                    "A - B = ",
                                    subtract(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '3':
                                print("\nMultiplicando A * B")
                                print(
                                    "A * B = ",
                                    multiply(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '4':
                                print("\nDividindo A / B")
                                print(
                                    "A / B = ",
                                    divide(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '5':
                                print("Saindo do módulo...\n")
                            case _:
                                print("Input inválido\n")
                
                except ImportError: 
                    print("Módulo Básico não foi encontrado...\n")

            case 'b':
                try:
                    from calc_exponenciation import to_power_of, square_root_of, cube_root_of
                    print("Módulo Potência carregado.\n")

                    while user_input != '4':
                        user_input = input(    
                            "1 - Potência\n" \
                            "2 - Raiz Quadrada\n" \
                            "3 - Raiz Cúbica\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )
                        match user_input:
                            case '1':
                                print("\nPotência de A^B")
                                print(
                                    "A^B = ",
                                    to_power_of(
                                        float(input("A = ")),
                                        float(input("B = "))
                                    ),
                                    "\n"
                                )
                            case '2':
                                print("\nRaiz quadrada de X")
                                print(
                                    "√X = ",
                                    square_root_of(float(input("X = "))),
                                    "\n"
                                )
                            case '3':
                                print("\nRaiz cúbica de X")
                                print(
                                    "∛X = ",
                                    cube_root_of(float(input("X = "))),
                                    "\n"
                                )
                            case '4':
                                print("Saindo do módulo...\n")
                            case _:
                                print("Input inválido\n")

                except ImportError:
                    print("Módulo Potência não foi encontrado...\n")
                    
            case 'c':
                try:
                    from calc_percentage import percentage_of, increase, discount
                    print("Módulo Percentual carregado.\n")

                    while user_input != '4':
                        user_input = input(    
                            "1 - Percentual\n" \
                            "2 - Acréscimo\n" \
                            "3 - Desconto\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )
                        match user_input:
                            case '1':
                                print("\nPercentual Y de X")
                                print(
                                    "Y% de X = ",
                                    percentage_of(
                                        float(input("X = ")),
                                        float(input("Y% = "))
                                    ),
                                    "\n"
                                )
                            case '2':
                                print("\nAcrescentar percentual Y à X")
                                print(
                                    "X + (X de Y%) = ",
                                    increase(
                                        float(input("X = ")),
                                        float(input("Y% = "))
                                    ),
                                    "\n"
                                )
                            case '3':
                                print("\nDescontar percentual Y de X")
                                print(
                                    "X - (X de Y%) = ",
                                    discount(
                                        float(input("X = ")),
                                        float(input("Y% = "))
                                    ),
                                    "\n"
                                )
                            case '4':
                                print("Saindo do módulo...\n")
                            case _:
                                print("Input inválido\n")

                except ImportError:
                    print("Módulo Percentual não foi encontrado...\n")

            case 'd':
                try:
                    from calc_statistics import average, median, standard_deviation
                    print("Módulo Estatística carregado.\n")

                    while user_input != '4':
                        user_input = input(    
                            "1 - Média\n" \
                            "2 - Mediana\n" \
                            "3 - Desvio Padrão\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )
                        match user_input:
                            case '1':
                                print("\nMédia de um conjunto de números")
                                set = input(
                                    "Insira os números do conjunto separados por espaço:\n"
                                ).split()
                                set = [float(value) for value in set]
                                print(
                                    "Média de ",
                                    set,
                                    " = ",
                                    average(set),
                                    "\n"
                                )
                            case '2':
                                print("\nMediana de um conjunto de números")
                                set = input(
                                    "Insira os números do conjunto separados por espaço:\n"
                                ).split()
                                set = [float(value) for value in set]
                                print(
                                    "Mediana de ",
                                    set,
                                    " = ",
                                    median(set),
                                    "\n"
                                )
                            case '3':
                                print("\nDesvio padrão populacional de um conjunto de números")
                                set = input(
                                    "Insira os números do conjunto separados por espaço:\n"
                                ).split()
                                set = [float(value) for value in set]
                                print(
                                    "Desvio Padrão populacional de ",
                                    set,
                                    " = ",
                                    standard_deviation(set),
                                    "\n"
                                )
                            case '4':
                                print("Saindo do módulo...\n")
                            case _:
                                print("Input inválido\n")
                        
                except ImportError:
                    print("Módulo Estatística não foi encontrado...\n")

            case 'e':
                try:
                    from calc_conversion import convert_celsius_fahrenheit, convert_kilometers_miles, convert_kilograms_pounds
                    print("Módulo Conversão carregado.\n")

                    while user_input != '4':
                        user_input = input(    
                            "1 - Celsisus para Fahrenheit\n" \
                            "2 - km para milhas\n" \
                            "3 - kg para libras\n" \
                            "4 - Cancelar operação\n" \
                            ">> "
                        )
                        match user_input:
                            case '1':
                                print("\nXºC para XºF")
                                print(
                                    "XºF = ",
                                    convert_celsius_fahrenheit(
                                        float(input("XºC = ")),
                                    ),
                                    "\n"
                                )
                            case '2':
                                print("\nXkm para X milhas")
                                print(
                                    "X milhas = ",
                                    convert_kilometers_miles(
                                        float(input("Xkm = ")),
                                    ),
                                    "\n"
                                )
                            case '3':
                                print("\nXkg para X libras")
                                print(
                                    "X libras = ",
                                    convert_kilograms_pounds(
                                        float(input("Xkg = ")),
                                    ),
                                    "\n"
                                )
                            case '4':
                                print("Saindo do módulo...\n")
                            case _:
                                print("Input inválido\n")

                except ImportError:
                    print("Módulo Percentual não foi encontrado...\n")

            case 'x':
                print("Tenha um ótimo dia! :)")
                break
            
            case _:
                print("Input inválido\n")

if __name__ == "__main__":
    menu()

