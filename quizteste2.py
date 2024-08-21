valor = int(input("Insira o valor: "))
idade = input("Idade maior que 25? ")
guincho = input("Precisará de guincho? ")
pernoite = input("Rua ou garagem? ")
sinistro = input("S/N?")
qnd = int(input("Quantos?"))

if valor <= 4000:
    valores = valor*0.04
elif valor >= 4001 and valor < 9000:
    valores = valor*0.05
else: 
    valores = valor*0.075

if idade == "S":
    valoridade = valor
if idade == "N":
    valoridade = valor*0.20

if guincho == "S":
    valorguincho = valor+110
if guincho == "N":
    valorguincho = 0

if pernoite == "rua":
    valorpernoite = valor*0.12
if pernoite == "garagem":
    valorpernoite = 0

valorsemitotal = valoridade+valores+valorguincho+valorpernoite
acrescimosinistro = qnd*0.3

if sinistro == "S":
    valorsinistro = valorsemitotal*acrescimosinistro
if sinistro == "N":
    valorsinistro = 0

valortotal = valorsemitotal+valorsinistro

if idade == "S":
    valortotal = valortotal - valortotal*0.12

print("{:.2f}".format(valortotal))