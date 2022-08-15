def primo(m):
    i = 1
    cont = 0
    while i <= m:
        if m % i == 0:
            cont += 1
        i += 1
    if cont > 2:
        return False
    else:
        return True

num = 1000

li = 2
LPrimos = []
while li <= num:
    if primo(li):
        LPrimos.append(li)
    li += 1

print(LPrimos)

num = int(input('digite o número, digite "0" para parar o programa'))

while num != 0:
    if num in LPrimos:
        print('É primo')
    else:
        print('Não é primo')
