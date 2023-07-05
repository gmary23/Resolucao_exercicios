'''
Faça um programa que inicialize uma lista com vários números diferentes, depois disso, solicite ao usuário um número, 
verifique se o número está ou não na lista e exiba uma mensagem notificando o usuário do resultado.

'''
lista = [1, 3, 5, 7, 9]
numero = int(input('Informe um número: '))

if numero in lista:
    print(f'O numero {numero} está na lista')
    print(lista)
else: 
    print('O número não está na lista.')
    print(lista)

