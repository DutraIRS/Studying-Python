'''
===================================================================
1 - Create a function that will receive heights from inputs (by 
some kind of loop) and return their average. Must be protected from
invalid entry values.
===================================================================
'''
def avg_height():
  list_heights = []
  height = 0

  while height != 99:
    try:
    # tries to convert the input to float
      height = float(input('Type a height or type 99 to exit: '))
      if height != 99:
      # unless it is the exit command, appends the given value to the list
       list_heights.append(height)
    except ValueError:
      # returns an error message and restarts the loop
      print('Invalid value! Have you used a comma as decimal separator?')
      pass
  sum = 0
  for i in range(len(list_heights)):
    # sums the given values and divides by the number of values
    sum += list_heights[i]
  try:
    avg = sum/len(list_heights)
  except ZeroDivisionError:
    avg = 0
  return avg

print('The average height is ' + str(round(avg_height(), 2)))

'''
===================================================================
2 - Crie uma função que receberá um path para um arquivo .txt, irá
abrí-o em modo read, e caso o arquivo não exista, irá criá-lo.
===================================================================
'''
import os

def abre_te_sesamo(path):
  if path[-4:] != '.txt':
    raise Exception('Não é um arquivo .txt!')
  # path deve ser o caminho relativo ao script python
  script_dir = os.path.dirname('__file__')
  file_path = os.path.join(script_dir, path)
  try:
    # o parâmetro x tenta criar o arquivo e retorna erro caso já exista
    # ou seja, a função tenta criar o arquivo e, caso não consiga, abre-o
    open(file_path, 'x').read()
  except:
    open(file_path).read()

def fecha_te_sesamo(path):
  script_dir = os.path.dirname('__file__')
  file_path = os.path.join(script_dir, path)
  open(file_path).close()

path = 'o_barradas_eh_o_melhor.txt'

abre_te_sesamo(path)
fecha_te_sesamo(path)

'''
===================================================================
3 - Crie uma função que receberá duas listas de números e retornará
uma nova lista que é uma soma das duas listas. 
Ela deve ser protegida contra entrada de valores inválidos e, caso
as listas sejam de tamanhos diferentes, deve ser retornado uma men-
sagem ao usuário.
Exemplo 1:
[1, 3, 4, 6]
[2, 8, 11, 1]
Output:
[3, 11, 15, 7]
Exemplo 2:
[1, 5]
[4, 2, 8]
Output:
"Tamanhos não compatíveis!"
===================================================================
'''
def soma_listas():
  lista_1 = []
  lista_2 = []
  item = 0

  while item != 'next':
      try:
        # recebe o valor dado pelo usuário e tenta converter em float
        item = input('Digite um item a inserir na lista 1 ou insira next para prosseguir à lista 2: ')
        lista_1.append(float(item))
      except ValueError:
        # confere se o valor inválido não é o comando para ir para o próximo passo
        if item != 'next':
          print('Valor inválido!')
          pass
        else:
          # se for o comando, segue o loop, que será interrompido na seguinte iteração
          pass

  while item != 'end':
      try:
        item = input('Digite um item a inserir na lista 2 ou insira end para prosseguir ao cálculo: ')
        lista_2.append(float(item))
      except ValueError:
        # mesma estrutura do loop anterior, exceto que agora o comando é end
        if item != 'end':
          print('Valor inválido!')
          pass
        else:
          pass

  if len(lista_1) == len(lista_2):
    # confere se as listas são do mesmo tamanho
    nova_lista = []
    for i in range(len(lista_1)):
      # insere a soma dos elementos de mesma posição na nova lista
      novo_elemento = lista_1[i] + lista_2[i]
      nova_lista.append(novo_elemento)
    return nova_lista
  else:
    return 'Tamanhos não compatíveis!'

print(soma_listas())

'''
===================================================================
4 - Crie uma função que receberá uma lista de nomes e irá lançar
uma exceção caso algum nome seja inválido.
Um nome é inválido quando:
- Não for uma string
- Tiver números
- Tiver um dos seguintes caracteres: "!@#$%¨&*()_+=-{}[]|:;<>,.?/
O tipo de exceção lançada deve ser diferente para cada um dos três
tipos de nomes inválidos. (Use raise Exception())
===================================================================
'''
def confere_nomes(lista_nomes):
  for nome in lista_nomes:
    # confere se são strings
    if type(nome) != str:
      raise Exception('Não é uma string!')
    else:
      for letra in range((len(nome))):
        try:
          # tenta converter cada letra em int (retorna erro a menos que seja um número)
          int(nome[letra])
        except ValueError:
          # não é número, mas é um símbolo especial?
          if nome[letra] in '"!@#$%¨&*()_+=-{}[]|:;<>,.?/':
            raise Exception('Possui símbolo especial!')
          else:
            # os nomes escritos corretamente caem aqui
            pass
        else:
          # se não retornou erro, é um número
          raise Exception('Possui número!')
  return lista_nomes

lista_nomes = ['João', 'Carlota']

print(confere_nomes(lista_nomes))

'''
===================================================================
5 - Crie uma função fatorial para os números inteiros não negativos
retorne o fatorial do número (exemplo 4!=24, 1!=1). Para criar essa 
função não é permitido utilizar bibliotecas, apenas o python 
padrão. Proteja a função para qualquer tipo de dados que seja
diferente dos números inteiros não negativos (-5! = exceção).
===================================================================
'''
def fatorial():
  num = 0.5

  while (num % 1 != 0) or (num < 0):
    # pede um novo input enquanto não atender ao definido pelo enunciado
    try:
      # testa se é um número (strings causam erro)
      num = float(input('Digite um número: '))
      try:
        # se for número, confere se atende aos requisitos
        if (num % 1 != 0) or (num < 0):
          raise ValueError
          # este raise e o abaixo servem apenas para pular para o bloco que adereça valores inválidos (ainda estamos dentro do try inicial)
      except TypeError:
        raise ValueError
    except ValueError:
      # se não for int ou float, reseta a variável num, informa o erro e recomeça o loop
      num = 0.5
      print('Valor inválido!')
      pass
  fatorial = 1
  for i in range(1, (int(num) + 1)):
    # calcula o fatorial
    fatorial = fatorial*i
  return fatorial

print(fatorial())
