print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Desenvolva um programa que leia quatro números e depois eleve eles ao quadrado,
calcule a soma e mostre o resultado da Soma''')

print()
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
soma = 0
n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terceiro Número: '))
n4 = int(input('Digite o Quarto Número: '))
Soma = (n1 * n1) + (n2 ** 2) + (n3 ** 2) + (n4 ** 2)
print(f'A soma dos números após elevá-los ao quadrado é {Soma}')
print(f'{"FIM":=^40}')
