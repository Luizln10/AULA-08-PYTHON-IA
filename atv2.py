produtos = {}

def adicionarProduto(nome, preço, quantidade):
    if nome in produtos:
        print(f"O {nome} já existe! Tente novamente")
    else:
        produtos[nome] = {'preço' : preço, 'quantidade' : quantidade}
        print(f"O {nome} foi adicionado")
