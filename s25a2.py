matriz = [[1,2,3], [4,5,6,], [7,8,9]]
numero = matriz [1][1]
print("numero = {numero}")

cinema = [[0 for _ in range(8)]for _ in range(5) ]

def exibir(matriz):
    print("  1 2 3 4 5 6 7 8 ")
    for linha in range(5):
        print(linha + 1, end= ' ')
        for coluna in range (8):
            print(matriz[linha][coluna], end= ' ')
        print()

def reservar(linha, coluna, cinema):
    posicao_l = linha - 1
    posicao_c = coluna - 1
    if 0 < posicao_l < 5 and 0 < posicao_c <=8:
        if cinema[posicao_l][posicao_c] == 0:
            cinema[posicao_l][posicao_c] = 1
            print(f"O Assento [{posicao_l}{posicao_c}] foi reservado com sucesso")
        else:
            print(f"O Assento [{posicao_l}{posicao_c}] já foi reservado")

def cancelar(linha, coluna, cinema):
    posicao_l = linha - 1
    posicao_c = coluna - 1
    if 0 < posicao_l < 5 and 0 < posicao_c < 8:
        if cinema[posicao_c][posicao_l] == 0:
            cinema[posicao_l][posicao_c] = 1
            print(f"O Assento [{posicao_c}{posicao_l}] foi cancelado com sucesso")
        else:
            print(f"O Assento [{posicao_c}{posicao_l}] já foi cencelado")

exibir(cinema)
reservar(1,3, cinema)
reservar(2,5, cinema)
reservar(4,7, cinema)
#cancelar(2,5)
exibir(cinema)