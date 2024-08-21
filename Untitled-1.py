
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
    cupcake = troco//2

    if troco == 2 and qtd > 4:
        if cupcake 

    # if cupcake == 0 and qtd > 4:
    #     print("cupcake")
    # if troco == 2 and qtd < 4 and cupcake == 0:
    #     print("cheesecake")

    # if troco == 1 and qtd> 4 and cupcake == 0:
    #     print("banofee")
    # if troco == 1 and qtd < 4 and cupcake == 0:
    #     print("brownie")

    # if troco > 2 and qtd > 4 and cupcake >= 1:
    #     print
    # if troco == 0:
    #     print("sem acompanhamento")


