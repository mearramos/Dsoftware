tipo = int(input("1(C) or 2(F): "))
temp = int(input("Insira a temperatura: "))

def c_para_f(temp):
    resultc = (temp*5/9+32)
    return(resultc)

def f_para_c(temp):
    resultf = ((temp-32)*5/9)
    return(resultf)

if tipo == 1:
    resultcc = c_para_f(temp)
    print(resultcc)

if tipo == 2:
     resultff = f_para_c(temp)
     print(resultff)