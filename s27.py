import random

def criar_matriz(dim_linha, dim_coluna):
    matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    return matriz

def matriz_aleatoria(dim_linha, dim_coluna):
    matriz = criar_matriz(dim_linha, dim_coluna)
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            matriz[linha][coluna] = random.randint(0,9)
    return matriz

def imprimir(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz[0])
    print(f"\nMatriz gerada com dimensões: {dim_linha} x {dim_coluna}")
    for linha in range (dim_linha):
        for coluna in range(dim_coluna):
            print(matriz[linha][coluna], end= "  ")
        print()

def main():
    while True:
        dim_linha = int(input("Digite a dimensão da linha: "))
        dim_coluna = int(input("Digite a dimensão da coluna: "))
        matriz = matriz_aleatoria(dim_linha, dim_coluna)
        imprimir(matriz)
        continuar = input("\nDeseja continuar?[s, n]: ").lower()
        if continuar == "n":
            break

main()