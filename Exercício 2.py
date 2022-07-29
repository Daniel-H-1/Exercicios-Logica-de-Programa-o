print(f'{"INSTRUÇÕES DO PROGRAMA":=^40}')
print('''Calcular a média ponderada dadas as notas de 3 provas, e o peso de cada uma delas, 
mostrar o resultado da média e a situação do aluno de acordo com o seguinte critério:

- Média >= 7 Aprovado;
- Média >= 5 e <= 7 Recuperação;
- Média < 5 Reprovado;''')

print()
print(f'{"RESOLUÇÃO DO PROGRAMA":=^40}')
nota1 = nota2 = nota3 = 0
peso1 = peso2 = peso3 = 0
mediaponderada = 0

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
peso1 = int(input('Peso da 1 prova: '))
peso2 = int(input('Peso da 2 prova: '))
peso3 = int(input('Peso da 3 prova: '))
mediaponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
if mediaponderada >= 7:
    print('Aprovado')
elif mediaponderada > 5:
    print('Recuperação')
else:
    print('Reprovado')
print(mediaponderada)
print(f'{"FIM":=^40}')
