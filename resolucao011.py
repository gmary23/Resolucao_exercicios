'''
Faça um programa que solicite o nome completo do usuário e exiba somente o seu segundo nome/primeiro sobrenome
'''
nome = input('Digite seu nome completo: ')
nome_dividido = nome.split(" ")
print(nome_dividido[1])
print(nome_dividido[3])