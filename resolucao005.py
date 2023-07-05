'''
 Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, 
 faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.
'''

ano = int(input('Qual ano você nasceu? '))
ano_atual = 2023

if ano_atual - ano >= 18:
    print('Você já fez 18 anos')
else:
    print('Você ainda fará 18 anos')


