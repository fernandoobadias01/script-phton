# fala sobre o dobro o triplo e a raiz quadrada do numero digitado
numero = int(input('Digite um numero'))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O dobro de {} é igual á {}!'.format(numero, dobro))
print('O triplo de {} é igual á {}!'.format(numero, triplo))
print('A raiz quadrada de {} é igual á {:.2}!'.format(numero, raiz))