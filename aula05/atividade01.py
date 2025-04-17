# ate 15° TEMPLIMITE - PASSOU DISSO = MANUTENÇÃO

temp = float(input('Informe a temperatura: '))

TEMPLIMITE = 15.0

match temp:
    case t if t <= TEMPLIMITE:
        print('Temperatura dentro do limite')
    case _:
        print('O equipamento de refrigeração precisa de manutenção')
