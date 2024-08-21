temp = int(input("Insira a temperatura: "))

def c_para_f(temp):
    y = (temp*5/9+32)
    return(y)

result = c_para_f(temp)
print(result)