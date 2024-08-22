valores = {
    "XP": 5,
    "P": 7,
    "M": 20,
    "G": 31,
    "XG": 50
}

tamanho = input("Escolha 'XP', 'P', 'M', 'G', ou 'XG': ").strip().upper()

if tamanho in valores:
    valor_tamanho = valores[tamanho]

    orcamento = int(input("Insira seu orçamento: "))
    qtd = orcamento // valor_tamanho
    troco = orcamento - qtd*valor_tamanho
    novoorc = troco//2
    maissobre = troco%2

if qtd<=4 and novoorc>0 and maissobre==0:
    print(novoorc,"cheesecake")
if qtd<=4 and novoorc==0 and maissobre>0:
    print(maissobre,"brownie")
if qtd<=4 and novoorc>0 and maissobre>0:
    print(novoorc,"cheesecake")
    print(maissobre,"brownie")
if qtd>4 and novoorc==0 and maissobre>0:
    print(maissobre,"banofee")    
if qtd>4 and novoorc>0 and maissobre>0:
    print(novoorc,"cupcake")
if qtd>4 and novoorc>0 and maissobre==0:
    print(novoorc,"cupcake")
    print(maissobre,"banoffee")
if qtd>4 and novoorc==0 and maissobre==0:
    print("sem acompanhamento")
if qtd<=4 and novoorc==0 and maissobre==0:
    print("sem acompanhamento")
