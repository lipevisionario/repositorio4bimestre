import random
def exibir(matriz):
    print("  1 2 3")
    for linha in range(3):
        print(linha + 1, end= ' ')
        for coluna in range (3):
            print(matriz[linha][coluna], end= ' ')
        print()

matriz = [['x' for _ in range(3)] for _ in range(3)]

exibir(matriz)

numero = random.randint(0, 100)
matriz2 = [[numero for _ in range(3)] for _ in range(3)]
exibir(matriz2)
