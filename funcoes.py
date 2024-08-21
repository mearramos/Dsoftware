import math

def altura_do_predio(comprimento, ângulo):
    resposta = math.tan(math.radians(ângulo))
    altura = (resposta*comprimento)
    return altura