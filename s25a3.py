vendas_mensais=[120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

def calcular_total_vendas(vendas_mensais):
    resultado=0
    for venda in vendas_mensais: 
        resultado = resultado + venda
    return resultado

print(f"total de vendas:{calcular_total_vendas(vendas_mensais)}")

def media_mensal(vendas_mensais):
  total_vendas = calcular_total_vendas(vendas_mensais)
  tamanho= len(vendas_mensais)
  media= total_vendas/tamanho
  return media

print (media_mensal(vendas_mensais):)