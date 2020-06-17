# -*- coding: utf-8 -*-
'''estrela'''
import statistics
import math
pi = 3.1415
'''
funções seguem abaixo
'''
'''verificar se primo'''
def primo(a):
  while True:
    if a >= 3:
      if a % 2 != 0:
        if a % 3 != 0:
          if a % 5 != 0:
            return True
            break
          else:
            return False  
        else:
          return False
      else:
        return False      
    else:
      return False       

'''verifica se é primo'''		
def mmc(num1, num2):
  a = num1
  b = num2
  c = None
  while c != 0:
      c = a % b
      a  = b
      b  = c
  return a
'''função de mmc'''
def euler(a):
  a = a
  lista =[]
  teste = 0
  c = a
  contador = 0
  for i in range(a):
    lista.append(a-1)
    a-=1
  for j in range(len(lista)):
    teste = lista[j]
    if teste != 0:
      if mmc(c,teste)==1:
        contador +=1
  return int(contador/2)
'''conta os não multiplos'''

def chamada(entrada):
  valor = entrada
  if primo(valor) == False:
    return euler(valor)
  else:
    return int((valor - 1)/2)

'''ler mais sobre função totiente/euler'''

'''calculando seno/cos'''
def coseno(a):
  valor = a
  pi = 3.1415
  circ=360
  grau = valor*(pi/circ)
  raio = 10
  return raio * math.cos(grau)

def seno(a):
  valor = a
  pi = 3.1415
  circ=360
  grau = valor*(pi/circ)
  raio = 10
  return raio*math.sin(grau)

def coord(a):
  xy = a
  return print('x :',coseno(xy),'y :',seno(xy))

'''organizar as coordenadas'''
def org(a):
  pontos = a
  lista=[]
  razao = 360/pontos
  param = 0
  for i in range(pontos):
    lista.append(razao+param)
    param += razao
  return lista

'''org retorna uma lista com os graus para cada ponto'''

'''convertendo para cartesiano'''

def grauToCartX(a):
  grauList = a
  coslist =[]
  grau =0
  for i in range(len(grauList)):
    grau = grauList[i]
    coslist.append(coseno(grau))
  return coslist

def grauToCartY(a):
  grauList = a
  senlist=[]
  grau =0
  for i in range(len(grauList)):
    grau = grauList[i]
    senlist.append(seno(grau))
  return senlist

'''tratando as coordenadas cartesianas para X
  função tratamento retornando uma matriz
  tratamento retorna metade da quantidade de coordenadas para tratar
'''
def tratamentoPositivoX(a):
  eiX = a
  j = 1
  lxPositivo = []
  contador = 0
  while True:
    lxPositivo.append(eiX[j])
    j +=2
    contador +=1
    if contador == round(len(eiX)/2):
      return lxPositivo
      break

'''recebe lista com valores de x e multiplica por -1'''
def finalCoordX(lxPositivo):
  lstX = lxPositivo
  lstNegativo = []
  for i in range(len(lstX)):
    lstNegativo.append(lstX[i]*-1)
  return lstNegativo

###############################

'''inicio tratamento para valores de Y'''
def tratamentoPositivoY(a):
  eiY = a
  j = 1
  lyPositivo = []
  contador = 0
  while True:
    lyPositivo.append(eiY[j])
    j +=2
    contador +=1
    if contador == round(len(eiY)/2):
      return lyPositivo
      break

'''recebe lista com valores de Y e multiplica por -1'''
def finalCoordY(lyPositivo):
  lstY = lyPositivo
  lstNegativo = []
  for i in range(len(lstY)):
    lstNegativo.append(lstY[i]*-1)
  return lstNegativo

'''chamadas
entrada = numero de pontos '''
entrada = 150
if entrada%2 !=0:
  entrada +=1

ordenada = org(entrada)
ordenadoX = grauToCartX(ordenada)
ordenadoY = grauToCartY(ordenada)
'''tradando coordenadas para x'''
lxPositivo = tratamentoPositivoX(ordenadoX)
lxNegativo = finalCoordX(lxPositivo)

''' tratando coordenadas para y'''
lyPositivo = tratamentoPositivoY(ordenadoY)
lyNegativo = finalCoordY(lyPositivo)

'''finalizando tratamento das coordenadas'''
xfinal =[]
yfinal=[]
'''obs: usar função lambda para simplificar'''
for x in range(len(lxPositivo)):
  xfinal.append(lxPositivo[x])

for y in range(len(lyPositivo)):
  yfinal.append(lyPositivo[y])

for nx in range(len(lxNegativo)):
  xfinal.append(lxNegativo[nx])

for ny in range(len(lyNegativo)):
  yfinal.append(lyNegativo[ny])

#tratar numeros impares
'''se o numero for impar 
posso somar a entrada + 1 e no final retirar 1 coordenada'''
'''
for d in range(len(xfinal)):
  print('(',xfinal[d],',',yfinal[d],')')'''



'''criar função para tratar numeros impares'''
statistics.median(xfinal)