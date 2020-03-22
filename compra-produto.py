print("Digite o código do produto comprado entre 1 e 10:")
codproduto = float(input())
print("Digite o peso do produto em quilos:")
pesoquilos = float(input())
print("Digite o código do país de origem de 1 a 3:")
codorigem = float(input())

#peso em gramas
pesogramas = (pesoquilos * 1000)
print("O peso do produto em gramas é", pesogramas)

#preço do produto
if codproduto >= 1 and codproduto <= 4:
    precototal = (pesogramas * 10)
else:
    if codproduto >= 5 and codproduto <= 7:
        precototal = (pesogramas * 25)
    else:
        if codproduto >= 8 and codproduto <= 10:
            precototal = (pesogramas * 35)

print("O preço do produto será", precototal)

#preço imposto
if codorigem == 1:
    precoimp = 0
else:
    if codorigem == 2:
        precoimp = (precototal * 15)/100
    else:
        if codorigem == 3:
            precoimp = (precototal * 25)/100

print("O valor do imposto cobrado será de", precoimp)

#valor total
valtotal = (precototal + precoimp)
print("O valor final do produto será", valtotal)


