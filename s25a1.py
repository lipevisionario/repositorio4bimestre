estoque = [20 , 15 , 10 , 30 , 5 ]
def atualizar(elemento, quantidade):
    posição = elemento -1
    if 0 <= posição < len(estoque):
            estoque[posição]-= quantidade
    else:
        print("elemento invalido!")  
 
def exibir (estoque):
    print(f"Estoque atual :{estoque}")
 
def adicionar(elemento,quantidade):
     posição = elemento - 1
     if 0<= posição < len (estoque):
          estoque [posição] += quantidade
     else:
          print("Elemento invalido")
def exibir (Estoque):
     print (f"estoque atual : {estoque}")
 
exibir(estoque)
atualizar(1,3 )        
print("estoque atualizado")
exibir(estoque)
 