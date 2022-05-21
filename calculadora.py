from gettext import find
import os
from rich import print

   
while True:
    print('###### DIGITE SAIR PARA DEIXAR O PROGRAMA ######')
    numero = input('Digite sua operação entre dois números aqui: ')
    os.system('cls')

    if numero.lower() == 'sair':
        print('Saindo...')
        break

 
    elif numero.find('+') > 0:    
        trocar = numero.replace('+', ' ')   

        novos_numeros = trocar.split()              

        result = float(novos_numeros[0]) + float(novos_numeros[1])

        print(result)


    elif numero.find('-') > 0:
        trocar = numero.replace('-', ' ')

        novos_numeros = trocar.split()

        result = float(novos_numeros[0]) - float(novos_numeros[1])

        print(result)

    elif numero.find('*') > 0:
        trocar = numero.replace('*', ' ')

        novos_numeros = trocar.split()

        result = float(novos_numeros[0]) * float(novos_numeros[1])

        print(result)


    elif numero.find('/') > 0:
        trocar = numero.replace('/', ' ')

        novos_numeros = trocar.split()

        result = float(novos_numeros[0]) / float(novos_numeros[1])

        print(result)
    
    
    else:
        print('Operação inválida')
    
    