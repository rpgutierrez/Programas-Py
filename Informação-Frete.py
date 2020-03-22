print("Seja bem vindo ao programa de informção de fretes...")

print("")

print("Rio Grande do Sul, Santa Catarina e Paraná = 1")
print("São Paulo, Rio de Janeiro, Espirito Santo e Minas Gerais = 2")
print("Acre, Amapá, Amazonas, Pará, Rondônia, Roraima e Tocantins = 3")
print("Alagoas, Bahia, Ceará, Maranhão, Paraíba, Pernambuco, Piauí, Rio Grande do Norte e Sergipe = 4")
print("Goiás, Mato Grosso, Mato Grosso do Sul e o Distrito Federa = 5")

print("")

print("Digite o código correspondente ao seu estado:")
codestado = int(input())

while(codestado > 5 or codestado < 1):
    print("Estado inválido, tente novamente")
    codestado = int(input())

valproduto = float(input("Digite o valor do produto:"))
valfrete = 0
if codestado == 1:
    valfrete = 0
else:
    if codestado == 2:
        valfrete = (valproduto * 0.12)
    else:
        if codestado == 3:
            valfrete = (valproduto * 0.34)
        else:
            if codestado == 4:
                valfrete = (valproduto * 0.28)
            else:
                if codestado == 5:
                    valfrete = (valproduto * 0.19)

print("O valor do frete é", valfrete)

valtotal = (valproduto + valfrete)
print("O valor total do produto é", valtotal)


