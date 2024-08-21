
# dicio = dict(XP=5, P=7, M=20, G=31, XG=50) #basicamente, aqui estou criando um dicionário. as chaves estão guardando os valores. 
# print(type(dicio)) #TESTE DICIONÁRIO

tamanho = input("Escolha 'XP', 'P', 'M', 'G', ou 'XG': ").strip().upper()
XP = 5
P = 7
M = 20
G = 31
XG = 50

# if tamanho in dicio:
#     print(f"O valor de {tamanho} é {dicio[tamanho]}")

orcamento = int(input("Insira seu orçamento: "))

calculo = (orcamento + tamanho)

print(calculo)