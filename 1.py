
altura = float(input('informe a Altura = ' ))
peso = float(input('informe o peso =  '))
IMC = peso/(altura*altura)

print(IMC)

if IMC<18.5:
    print('abaixo do peso')
elif IMC<18.5 and IMC<25:
    print('peso normal')
if IMC>25 and IMC<30:
    print('acima do peso')
elif IMC>30:
    print('obeso')
