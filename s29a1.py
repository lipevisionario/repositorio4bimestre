quantidade = int(input("Digite a quantidade de peças: "))
preco = float(input("Digite o preço unitario: "))

if quantidade >= 1 and quantidade <= 5:
    desconto = 0
    preco = preco - (preco * desconto)
    print(f"desconto: {desconto}")
    print(f"preço: {preco}")
elif  quantidade > 5 and quantidade <= 10:
    desconto = 0.10
    preco = preco - (preco * desconto)
    print(f"desconto: {desconto}")
    print(f"preço: {preco}")
elif  quantidade > 10:
    desconto = 0.20
    preco = preco - (preco * desconto)
    print(f"desconto: {desconto}")
    print(f"preço: {preco}")
else:
    print("quantidade invalida")