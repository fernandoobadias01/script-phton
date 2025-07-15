# mostra a nota media que o aluno tirou
aluno = input('nome do aluno: ')
nota1 = float(input('Qual foi a primeira nota do aluno?: '))
nota2 = float(input('Qual foi a segunda nota dele?: '))
soma = (nota1 + nota2) / 2
print('A nota media do aluno {} é {}!' .format(aluno, soma))