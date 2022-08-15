

Soma = 1
Subtracao = 2
Divisao = 3
Multiplicacao = 4

print('[+ = 1] \n[- = 2] \n[/ = 3] \n[* = 4]')

operacao = int(input('Digite a operação: '))


x = float(input('Entre com o número: '))
y = float(input('Entre com o número: '))

while operacao == 1:
    if operacao == 1:
        soma = x + y
        print(f'Resultado: {x} + {y} = {soma}')
        operacao = int(input('Digite a operação: '))
        x = float(input('Entre com o número: '))
        y = float(input('Entre com o número: '))
while operacao == 2:
    if operacao == 2:
        sub = x - y
        print(f'Resultado: {x} - {y} = {sub}')
        operacao = int(input('Digite a operação: '))
        x = float(input('Entre com o número: '))
        y = float(input('Entre com o número: '))
while operacao == 3:
    if operacao == 3:
        div = x / y
        print(f'Resultado: {x} / {y} = {div}')
        operacao = int(input('Digite a operação: '))
        x = float(input('Entre com o número: '))
        y = float(input('Entre com o número: '))
while operacao == 4:
    if operacao == 4:
        mult = x * y
        print(f'Resultado: {x} * {y} = {mult}')
        operacao = int(input('Digite a operação: '))
        x = float(input('Entre com o número: '))
        y = float(input('Entre com o número: '))
else:
    print('Operação inexistente.')
    print('Fim da operação.')
