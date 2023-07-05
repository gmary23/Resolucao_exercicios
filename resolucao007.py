'''
Faça um programa que solicite ao usuário 2 valores, utilize uma condição
ternária para escrever qual o maior valor: o primeiro ou o segundo 
(caso os valores sejam iguais, considere o segundo).
'''
valor1 = int(input('Digite um valor? '))
valor2 = int(input('Digite outro valor? '))
print('O primeiro é maior' if valor1 > valor2 else 'O segundo é maior') # operacão ternária