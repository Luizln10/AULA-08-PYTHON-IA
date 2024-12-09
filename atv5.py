def produto_mais_vendido(vendas):
    max_vendas = 0
    produtos_mais_vendidos = []

    for produto, quantidade in vendas.items():
        if quantidade > max_vendas:
            max_vendas = quantidade
            produtos_mais_vendidos = [produto]  
        elif quantidade == max_vendas:
            produtos_mais_vendidos.append(produto) 

    return produtos_mais_vendidos, max_vendas

vendas = {
    'Produto A': 10,
    'Produto B': 15,
    'Produto C': 15,
    'Produto D': 5
}

produtos, quantidade = produto_mais_vendido(vendas)
print(f'Produto(s) mais vendido(s): {produtos} com {quantidade} vendas.')
