matriz = [[1,2,3], [4,5,6,], [7,8,9]]
numero = matriz [1][1]
print("numero = {numero}")

def exibir(matriz):
    print("  1 2 3")
    for linha in range(3):
        print(linha + 1, end= ' ')
        for coluna in range (3):
            print(matriz[linha][coluna], end= ' ')
        print()

exibir(matriz)