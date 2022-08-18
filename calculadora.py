

Soma = 1
Subtracao = 2
Divisao = 3
Multiplicacao = 4


def start():
    print('[+ = 1] \n[- = 2] \n[/ = 3] \n[* = 4]')
    operacao = int(input('Digite a operação: '))
    x = float(input('Entre com o número: '))
    y = float(input('Entre com o número: '))


if operacao == 1:
    soma = x + y
    print(f'Resultado: {x} + {y} = {soma}')
    start()

elif operacao == 2:
    sub = x - y
    print(f'Resultado: {x} - {y} = {sub}')
    start()

elif operacao == 3:
    div = x / y
    print(f'Resultado: {x} / {y} = {div}')
    start()

elif operacao == 4:
    mult = x * y
    print(f'Resultado: {x} * {y} = {mult}')
    start()
else:
    print('Operação inexistente.')
    print('Fim da operação.')
