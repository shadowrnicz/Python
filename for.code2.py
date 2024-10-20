# Algoritmo que calcula a soma dos números pares entre 1 e 50
soma = 0  # Inicializa a soma em 0
for i in range(1, 51):  # Inicializa i em 1, vai até 50
    if i % 2 == 0:  # Verifica se i é par
        soma += i  # Adiciona i à soma
print(f"Soma dos números pares entre 1 e 50: {soma}")  # Imprime o resultado
