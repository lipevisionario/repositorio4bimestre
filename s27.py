import random

def criar_matriz(dim_linha, dim_coluna):
    matriz = [[0 for _ in range(dim_coluna)] for _ in range(dim_linha)]
    return matriz

def matriz_aleatoria(dim_linha, dim_coluna):
    matriz = criar_matriz(dim_linha, dim_coluna)
    for linha in range(dim_linha):
        for coluna in range(dim_coluna):
            matriz[linha][coluna] : random.randint(0,100)
    return matriz

def imprimir(matriz):
    dim_linha = len(matriz)
    dim_coluna = len(matriz)
    print(f"matriz gerada com dimensões: {dim_linha}x {dim_coluna}")
    for linha in range (dim_linha)
        print(matriz[linha][coluna], end= "")


matriz = matriz_aleatoria(10,10)
imprimir(matriz)