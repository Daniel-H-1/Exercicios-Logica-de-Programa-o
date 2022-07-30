print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Faça um programa que leia um Peso em Quilogramas, e se o Peso ultrapassar 50 Quilos, calcule 4 reais de multa
por quilo em excesso, e assim calcular a multa.''')

print()
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
PesoP = Excesso = Multa = 0
PesoP = float(input('Digite o seu Peso: '))
if PesoP > 50:
    Excesso = PesoP - 50
    Multa = Excesso * 4
print(f'O peso total é {PesoP}')
if Excesso > 0:
    print(f'O Excesso total é {Excesso}')
else:
    print(f'Não existe excesso de Peso.')
if Multa > 0:
    print(f'A Multa é de R${Multa}')
else:
    print('Não existe multa, pois não houve excesso de Peso.')
print(f'{"FIM":=^40}')
