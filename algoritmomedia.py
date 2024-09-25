# Algoritmo média: criar um algoritmo que leia 4 notas
# e apresente uma média final

print("Algoritmo do cálculo da média")

nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
nota4 = float(input("Digite a nota4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média final é {media:.2f}")  # .2f é usado
# para mostrar apenas 2 casas decimais