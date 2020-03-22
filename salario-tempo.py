print("Digite o salário base do funcionário:")
salbase = float(input())
print("Digite o tempo prestado pelo funcionário em anos:")
tempo = float(input())

#imposto
if salbase < 200:
    imposto = 0
else:
    if salbase >= 200 and salbase <= 450:
        imposto = (salbase * 3)/100
    else:
        if salbase > 450 and salbase < 700:
            imposto = (salbase * 8)/100
        else:
            if salbase >= 700:
                imposto = (salbase * 12)/100
print("O valor do imposto é", imposto)

#gratificação
if salbase > 500 and tempo < 3:
    gtrf = 20
else:
    if salbase > 500 and tempo > 3:
        gtrf = 30
    else:
        if salbase < 500 and tempo < 3:
            gtrf = 23
        else:
            if salbase < 500 and tempo > 3 or tempo < 6:
                gtrf = 35
            else:
                if salbase < 500 and tempo > 6:
                    gtrf = 33
print("O valor da gratificação em reais é de", gtrf)

#salário líquido
salliq = (salbase - imposto) + gtrf
print("O salário líquido do funcionário será", salliq)

#categoria
if salliq < 350:
    categ = "A"
else:
    if salliq > 350 and salliq <= 600:
        categ = "B"
    else:
        if salliq > 650:
            categ = "C"
print("A categoria do funcionário é", categ)






