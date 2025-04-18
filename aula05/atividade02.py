# for n in range(10):
#     print(f'{n+1}')

# for n in range(5):
#     n+1
#     print('Estudando Python')

# for n in range(3):
#     n += 1
# nome = input('Informe o nome: ')
# print(f'nome: {nome}')

soma = 0.0
media = 0.0
for n in range(5):
    n += 1
    numero = int(input('Informe o número: '))
    soma += numero
if n == 5:
    media = soma/n

print(f' A soma total é: {soma:.2f} \n e a média é: {media:.2f} ')
# print(f'A média é: {media:.2f}')
