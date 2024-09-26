# 09-rent-car.py = Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o
# carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# variaveis
dias_locados = int(input("Dias alugados: "))
km_percorridos = float(input("Quantos km foram percorridos? "))

# calculo do preco total
total = (dias_locados*60)+(km_percorridos*0.15)
print(f"O valor total a pagar é R${total:.2f}")