import numpy as np
import numpy.random as npr
from numpy import linalg as la

'''
===================================================================
1 - Crie uma função usando numpy que caso receba uma matriz 
bidimensional numpy retorna um vetor unidimensional. Se a entrada é
um vetor unidimensional retorne uma matriz diagonal com os 
elementos do vetor. Caso contrário levante uma exceção ValueError.
===================================================================
''' 
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 2, 3])

def special_diagonal(D):
	# confere se é 2D
	if len(D.shape) == 2:
		# rearranja para 1 x m+n
		D = np.reshape(D, (1, D.shape[0] * D.shape[1]))
		return D

	elif len(D.shape) == 1:
		# cria uma matriz nula e insere cada elemento de D na posição correspondente na diagonal de M
		M = np.zeros((D.shape[0], D.shape[0]))
	
		for i in range(D.shape[0]):
			M[i, i] = D[i]
		return M

	else:
		# não foi dito o que fazer caso a matriz seja de outras dimensões
		print('Invalid input!')

print(special_diagonal(A), special_diagonal(B), sep='\n')

'''
===================================================================
2 - Crie uma função para simular o jogo pedra papel tesoura usando 
números aleatórios do numpy.
- Suponha que tirar pedra, papel ou tesoura possui a mesma 
probabilidade de acontecer.
- A entrada corresponde ao número de vezes que o experimento deve
acontecer.
- A função deve retornar um dicionário com a quantidade de vezes
que cada evento aconteceu (ex: {'papel':1,'pedra':3,'tesoura':2})
===================================================================
'''

def jokenpo(n):
  pedra = 0
  papel = 0
  tesoura = 0

  for i in range(n):
		# cria inteiros entre 1 e 3
    sorteio = npr.randint(1, 4)
    
		# mapeia os inteiros aleatórios para os contadores
    if sorteio == 1:
      pedra += 1
    elif sorteio == 2:
      papel += 1
    else:
      tesoura += 1

  dic = {'papel': papel, 'pedra': pedra, 'tesoura': tesoura}
  return dic

print(jokenpo(9))

'''
===================================================================
3 - Crie uma função para expandir uma matriz numpy. Dada uma matriz
A de dimensão mxn, retorne A com dimensão kxk onde k = max(m,n).
Completando com zeros até que A possua a dimensão kxk. 
===================================================================
'''

A = np.array([[1, 2, 3], [4, 5, 6], [1, 1, 9]])

def expandir(A):
	# confere se há mais linhas que colunas ou vice-versa
  if A.shape[0] > A.shape[1]:
		# cria uma matriz nula de tamanho apropriado
    B = np.zeros((A.shape[0], A.shape[0] - A.shape[1]))
		# empilha as matrizes, formando uma matriz quadrada
    A = np.hstack((A, B))
    return A

  elif A.shape[0] < A.shape[1]:
    B = np.zeros((A.shape[1] - A.shape[0], A.shape[1]))
    A = np.vstack((A, B))
    return A

  else:
    return A

print(expandir(A))

'''
===================================================================
4 - Crie uma função numpy que dada uma matriz A de dimensão mxn. 
Retorne um vetor um vetor coluna mx1 onde cada entrada i 
corresponde ao menor valor da linha i.
===================================================================
'''

A = np.array([[1, 2, 3], [4, 5, 6], [1, 1, 9]])

def minimos(A):
	# calcula os mínimos de cada linha e forma um novo array com a lista desses valores 
  B = np.amin(A, axis = 1)
  return B

print(minimos(A), minimos(A).shape)

'''
===================================================================
5 - Sabemos que uma multiplicação de matrizes não é comutativa. 
Mas, em alguns casos é possível verificar que A*B = B*A. Crie uma 
função que dada duas matrizes ela retorna verdadeiro se A*B=B*A e
retorna falso caso contrário. Observe que quando A e B não são 
matrizes quadradas a função deve retornar falso, independente do 
tamanho de A e B.
===================================================================
'''

A = np.array([[1, 9, 2], [0, 1, 0], [0, 0, 1]])
B = np.array([[1, 0, 0], [0, 1, 1], [0, 0, 1]])

def AB_igual_BA(A,B):
	# se A possuir um número diferente de linhas e colunas ou for de um 
	# formato diferente de B, já sabemos que AB != BA (não é necessário 
	# conferir se B possui uma quantidade diferente de linhas e colunas, 
	# pois, se A é quadrada e A.shape = B.shape, então B é quadrada)
  if A.shape[0] != A.shape[1] or A.shape != B.shape:
    return False

	# calcula AB e BA, compara-as elemento a elemento e retorna True se 
	# todos os elementos forem True
  elif (np.matmul(A, B) == np.matmul(B, A)).all():
    return True
  
  else:
    return False
  
print(AB_igual_BA(A, B))

'''
===================================================================
6 - Crie uma função que recebe uma lista de vetores numpy, retorne 
o vetor que possuiu a menor norma vetorial. 
Desafio opcional: tente resolver essa questão com uma só linha de 
código, recomendo utilizar map e função lambda. Confira a seguir:
https://medium.com/horadecodar/express%C3%B5es-lambda-em-python-com-map-reduce-e-filter-a391368ae886
https://cs.stanford.edu/people/nick/py/python-map-lambda.html
===================================================================
'''

lista = [np.array([1, 0, 1]), np.array([1, 53, 3]), np.array([1, 1, 0]), np.array([1, 5, 3]), np.array([1, 1, 4])]

# Solução 1:
def menorNorma(l):
	vector = l[0]

	for i in l:
		# compara a norma de cada elemento da lista
		if la.norm(vector) > la.norm(i):
			vector = l[i]

	return vector

print(menorNorma(lista))

# Solução 2:
# mapeia a norma de cada elemento da lista de vetores para uma nova lista,
# cria um array, acha o índice do menor elemento do array e usa esse índice
# para acessar o vetor desejado na lista de vetores 
print(lista[np.argmin(np.array(list(map(lambda i: la.norm(i), lista))))])

'''
===================================================================
7 - Desafio, vamos estimar o valor de pi por meio do Método de 
Monte Carlo. Considere um círculo de raio r=1 centrado na origem 
que está inscrito num quadrado de lado l=2 (veja a figura pi.png).
Vamos estimar o valor de pi comparando a razão da quantidade de 
pontos P_c que "caíram" dentro do círculo (matematicamente P_c
representa o número de pontos em que a distância euclidiana deles
a origem é menor do que r) em relação ao total de pontos P com a
razão da área do círculo em relação ao quadrado, observe:
pi*r^2/l^2 ~= P_c/P
Isto é, utilizando os valores de r^2=1 e l^2=4 estime o valor de pi:
pi/4 ~= P_c/P 
A função que vocês devem implementar deve:
- Receber n como o número de pontos que serão gerados.
- Gerar com numpy n coordenadas x aleatórias.
- Gerar com numpy n coordenas y aleatórias.
- Calcular a quantidade P_c de pontos que caíram dentro do círculo, 
isto é, calcular a distância do ponto I=(x_i,y_i) à origem (0,0) e
contar quantos estão mais próximos da origem do que o raio do círculo
(r=1).
- Retornar o valor de Pi de acordo com a expressão pi = (4*P_c)/P.
Obs: para saber mais sobre o Método de Monte Carlo acesse:
https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Monte_Carlo
===================================================================
'''

def piMonteCarlo(n):
	p_c = 0

	for i in range(n):
		# por algum motivo, aumentar o número de casas decimais das coordenadas melhora a estimativa mais do que aumentar n
		# cria as coordenadas num intervalo entre 0 e 1_000_000 e multiplica por (-1) elevado a 1 ou 2 (aleatoriamente)
		x = npr.randint(0, 1_000_001)*((-1)**npr.randint(1, 3))
		y = npr.randint(0, 1_000_001)*((-1)**npr.randint(1, 3))

		# divide por 1_000_000 para fazer as coordenadas ficarem entre -1 e 1 com seis casas decimais
		array = np.array((x, y))/1_000_000

		# se a norma é menor que 1, aumenta p_c em 1
		if la.norm(array) <= 1:
			p_c += 1

	pi = 4*p_c/n

	return pi
	
print(piMonteCarlo(100000))
