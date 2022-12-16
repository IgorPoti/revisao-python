#Exercício 001 referente a Listas (array) - Revisão João Igor

listaCarrinho = []
listaPrecos = []
contProdutos = 0
valorTotal = 0
produto = ''

while contProdutos < 5:
    produto = input('Produto: ')
    listaCarrinho.append(produto)
    preco = float(input('Preço: '))
    listaPrecos.append(preco)
    contProdutos += 1

for id in range(0, 5):
    valorTotal += listaPrecos[id]

print(f'Produtos: {listaCarrinho}')
print(f'Valor total: {valorTotal}')
