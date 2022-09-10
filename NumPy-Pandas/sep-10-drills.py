import numpy as np
import numpy.random as npr

'''
===================================================================
1 - Usando apenas o conceito de "máscaras" (usar uma array de boo-
leanas para selecionar elementos de outra array), crie uma função
que receba um argumento m e n e retorne uma array mxn com valores
gerados aleatoriamente.
Você deve gerar uma array com uma distribuição normal de média 7 
e desvio padrão 2, e após disso, você deve implementar um limite
de valores: os elementos da array devem ser, no máximo, 10, e no mí-
nimo, 0. 
===================================================================
''' 

def normalComLimite(m,n):
	# cria o array de média 7, std 2 e tamanho especificado
	array = npr.normal(7, 2, (m, n))
	# transforma os elementos menores que 0 em 0
	array[array < 0] = 0
	# transforma os elementos maiores que 10 em 10
	array[array > 10] = 10
	return array

print(normalComLimite(3, 6), '\n\n')

'''
===================================================================
2 - Novamente usando o conceito de máscaras, crie uma função que 
irá receber uma array mxn que representa notas de alunos em uma 
disciplina, onde cada linha representa um aluno e cada coluna a
nota de uma prova, que vale 10. A função deverá retornar uma array 
mx1 de booleanas, cujo valor de cada linha deverá indicar True se o 
aluno daquele índice tirou acima de 7 em ao menos metade das provas,
e False caso contrário.
===================================================================
'''

def alunosAprovados(notas):
	# cria o array m x 1 que será o output
	alunosAprovados = np.zeros((notas.shape[0], 1))
	for aluno in range(notas.shape[0]):
		aprovacoes = 0
		# para cada aluno(a), avalia e enumera em quantas provas ele(a) foi aprovado(a)
		for prova in range(len(notas[aluno, ])):
			if notas[aluno, prova] >= 7:
				aprovacoes += 1
		# se o(a) aluno(a) foi aprovado em pelo menos metade das provas,
		# o elemento correspondente no array output é transformado em 1
		if aprovacoes >= notas.shape[1]/2:
			alunosAprovados[aluno] = 1

	# arrays só aceitam um tipo de dado e, como usei np.zeros para criar o array,
	# não é possível mudar os elementos para booleanos um a um
	# dessa forma, todos são transformados ao mesmo tempo
	alunosAprovados = alunosAprovados.astype(bool)
	
	return alunosAprovados

notas = np.array([[7, 8, 9, 10, 2], [2, 3, 7, 8, 7], [4, 5, 3, 6, 5]])
print(alunosAprovados(notas), '\n\n')

'''
===================================================================
3 - Usando apenas o conceito de broadcasting numpy (ou seja, sem 
usar outras bibliotecas), crie uma função que receba uma array 1xn 
e retorne uma array 1xn que é a "normalização Z-score" dela.  
===================================================================
'''

def normalizarZScore(array):
	media = array.mean()
	std = array.std()
	# fórmula da normalização
	array = (array - media)/std
	return array

print(normalizarZScore(np.array((1, 2, 3, 4, 5))), '\n\n')

'''
===================================================================
4 - Crie uma função que receberá uma array mxn que representa notas 
de alunos da mesma forma que na questão 2, e retorne uma array mx1 
de booleanas, cujo valor de cada linha deverá indicar True se o a-
luno daquele índice deverá ficar de recuperação, ou False caso não.
Um aluno deverá ficar de recuperação se a média das notas dele for
menor que 7 mas maior que 5.
===================================================================
'''

def recuperacao(array):
	recuperacao = np.zeros((notas.shape[0], 1))
	for aluno in range(array.shape[0]):
		# se a média do subarray correspondente à linha de cada aluno estiver entre
		# 5 e 7, a linha correspondente do array output é transformada
		if array[aluno, ].mean() < 7 and array[aluno, ].mean() > 5:
			recuperacao[aluno] = 1

	recuperacao = recuperacao.astype(bool)
	
	return recuperacao

notas = np.array([[7, 8, 9, 10, 2], [2, 3, 7, 8, 7], [4, 5, 3, 6, 5]])
print(recuperacao(notas), '\n\n')

'''
===================================================================
5 - Crie uma função que receberá uma array mxn de inteiros e que 
retornará uma array mxn cujos elementos são o fatorial dos elemen-
tos da array de entrada.
Para aplicar o fatorial em cada elemento, não será permitido usar
loops. Tente pesquisar sobre a função "vectorize" do numpy.  
===================================================================
'''

def fatorial(num):
	fatorial = 1
	for i in range(1, num + 1):
		fatorial = fatorial * i
	return fatorial

# aplicando vectorize à função
fatorialArray = np.vectorize(fatorial)

print(fatorialArray(np.array([[0, 1, 2, 3, 4, 5, 9], [0, 3, 5, 2, 3, 1, 3]])))
