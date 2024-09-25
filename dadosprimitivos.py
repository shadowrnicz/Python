# Tipos de Dados Primitivos:
# - Inteiro (int): números inteiros
# - Float (float): números reais, decimais
# - String (str): cadeia de caracteres, utilizando aspas
# - Boolean (bool): tipo lógico True ou False
# - Complex (complex): números complexos, com parte real e imaginária
# - List (list): lista de elementos, ordenados e indexados
# - Tuple (tuple): tupla de elementos, ordenados e imutáveis
# - Dictionary (dict): dicionário de elementos, não ordenados e indexados

# Atribuição de variável por captura
nome = input("Digite o seu nome: ")
print(type(nome))
idade = input("Digite a sua idade: ")
print(type(idade))
altura = input("Digite a sua altura: ")
print(type(altura))

# Exibir na tela
print(f"nome: {nome} idade: {idade} altura: {altura}")

# Exemplo de conversão de string para inteiro
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
resultado = valorA + valorB
print(f"A soma = {resultado}")
# Exemplo de conversão de string para float
valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
resultado = valorA + valorB
print(f"A soma = {resultado}")