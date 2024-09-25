# Desenvolver um algoritmo que leia o peso e a altura
# do usuário, calcule o IMC.
# Cálculo de IMC = peso / (altura**2)
# Exiba o resultado do IMC com a classificação correspondente:
# Abaixo do peso – IMC < 18,5
# Peso normal – IMC entre 18,5 a 24,9
# Sobrepeso – IMC entre 25 e 34,9
# Obesidade – IMC a partir de 35

print("Programa para Cálculo de IMC")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura**2)

print(f"Seu IMC é {imc:.2f}")  # .2f é usado
# para mostrar apenas duas casas decimais

if (imc < 18.5):
    print("Abaixo do peso")
elif (18.5 <= imc < 25):
    print("Peso normal.")
elif (25 <= imc < 35):
    print("Sobrepeso.")
else:
    print("Obesidade.")