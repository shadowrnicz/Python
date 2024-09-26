# Desenvolva um programa que calcula as raízes de uma equação quadrática
# utilizando a fórmula de Bhaskara.
# Requisitos
# Solicite ao usuário para inserir os valores dos coeficientes a, b e c.
# Calcule o discriminante:
# Verifique o valor do discriminante:
# Se delta for negativo, imprima "A equação não possui raízes reais."
# Se delta for igual a zero, calcule e imprima a única raiz real.
# Se delta for positivo, calcule e imprima as duas raízes reais.

a = float(input("Informe o coeficiente a: "))
b = float(input("Informe o coeficiente b: "))
c = float(input("Informe o coeficiente c: "))

while a == 0:
    print("O coeficiente a não pode ser igual a zero.")
    a = float(input("Informe o coeficiente a: "))

# cálculo do delta
delta = b**2 - 4*a*c

# Verificando o delta
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A única raiz real é {x:.3f}")
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"As raízes reais são {x1:.3f} e {x2:.3f}")