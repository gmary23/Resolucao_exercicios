'''
Faça um programa que solicite a idade do usuário, verifique se o texto informado só contém números. 
Caso contenha somente números exiba a mensagem: "Você tem {idade digitada} anos.", 
caso contrário exiba a mensagem: "Você digitou uma idade inválida".
'''
idade = input('Qual sua idade? ')
if idade.isdigit(): # verifica se digitou número
    print(f'Você tem {idade} anos')
else:
    print(f'Você digitou a idade inválida')