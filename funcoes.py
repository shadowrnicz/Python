def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!\n")
def somar(a,b):
    return a+b
def calcAcirculo(raio):
    area = 3.1415 * raio**2
    return area

# Início do algoritmo
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
exibirMensagem(nome, idade) 
# Exibe a mensagem com o nome do usuário

# Chamando função com retorno
valorA = int(input("Digite o primeiro número: "))
valorB = int(input("Digite o segundo número: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma é igual a = {resultado}\n")

# Calcular a área do círculo
print("Área do círculo\n")
raio = float(input("Digite o valor do raio: "))
area = calcAcirculo(raio)
print(f"A área do círculo é igual a = {area:.2f}")
