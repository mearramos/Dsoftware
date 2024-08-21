def clovis(x):
    y = ((3 * x ** 3) - (2 * x ** 2) + (4 * x) + 8)
    return y

x = int(input("Insira um número: "))
y = clovis(x)
print(y)