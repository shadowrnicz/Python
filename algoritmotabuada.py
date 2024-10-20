# Algoritmo que exibe a tabuada de um número fornecido pelo usuário
numero = int(input("Digite um número: "))  # Lê um número inteiro do usuário
for i in range(1, 11):  # Inicializa i em 1, vai até 10
    print(f"{numero} x {i} = {numero * i}")  # Imprime a tabuada
