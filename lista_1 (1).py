# Questão 1
def altura_media():
  lista_alturas = []
  altura = 0

  while altura != 99:
    try:
    # tenta converter o input em float
      altura = float(input('Insira a altura ou insira 99 para finalizar: '))
      if altura != 99:
      # insere o valor na lista caso não seja o comando de saída
       lista_alturas.append(altura)
    except ValueError:
      # retorna uma mensagem de erro e reinicia o loop
      print('Valor inválido! Lembraste de usar ponto para separar as casas decimais?')
      pass
  soma = 0
  for i in range(len(lista_alturas)):
    # soma as alturas da lista e divide pelo número de elementos
    soma += lista_alturas[i]
  try:
    media = soma/len(lista_alturas)
  except ZeroDivisionError:
    media = 0
  return media

print('A média das alturas é ' + str(round(altura_media(), 2)))

# Questão 2
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

# Questão 3
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

# Questão 4
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

# Questão 5
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
