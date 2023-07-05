'''
Faça um programa que inicialize uma lista vazia
e a preencha com 5 nomes diferentes digitados pelo usuário, 
depois disso solicite um número de 0 até 4 e remova o elemento desta posição.
'''
lista = []

lista.append(input('Digite o primeiro nome: '))
lista.append(input('Digite o segundo nome: '))
lista.append(input('Digite o terceiro nome: '))
lista.append(input('Digite o quarto nome: '))
lista.append(input('Digite o quinto nome: '))
print(lista)

numero = int(input('Digite um número de 0 a 4.'))
del lista[numero]
print(lista)