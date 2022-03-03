# Programa de Juliana García Rosset
  # Versión 2: Se corrigieron los errores y se mejoró el programa :)
  # Nota: No se utilizan matrices sino listas de listas


from random import randrange
from turtle import Screen, Turtle
from time import sleep


# Crea matriz de ceros
def crea_matriz(w, l):
  matriz = []
  for i in range(w):
    matriz.append([0]*l)
  return matriz


def pone_bombas():
  bombas = cant_bombas
  for i in range(bombas):
    a, b = randrange(w), randrange(l)
    while bomb_num[a][b] == bomba:
      a, b = randrange(w), randrange(l)
    bomb_num[a][b] = bomba


def pone_numeros():	# Los números del 0 al 8 indican la cantidad de bombas cercanas
  for i in range(w):
    for j in range(l):
      if bomb_num[i][j] == bomba:
        if i-1 in range(w) and j-1 in range(l):
          if bomb_num[i-1][j-1] != bomba:
            bomb_num[i-1][j-1] += 1
        if i-1 in range(w):
          if bomb_num[i-1][j] != bomba:
            bomb_num[i-1][j] += 1
        if i-1 in range(w) and j+1 in range(l):
          if bomb_num[i-1][j+1] != bomba:
            bomb_num[i-1][j+1] += 1
        if j-1 in range(l):
          if bomb_num[i][j-1] != bomba:
            bomb_num[i][j-1] += 1
        if j+1 in range(l):
          if bomb_num[i][j+1] != bomba:
            bomb_num[i][j+1] += 1
        if i+1 in range(w) and j-1 in range(l):
          if bomb_num[i+1][j-1] != bomba:
            bomb_num[i+1][j-1] += 1
        if i+1 in range(w):
          if bomb_num[i+1][j] != bomba:
            bomb_num[i+1][j] += 1
        if i+1 in range(w) and j+1 in range(l):
          if bomb_num[i+1][j+1] != bomba:
            bomb_num[i+1][j+1] += 1


def dibuja_tablero():
  t.penup()
  for i in range(w):
    for j in range(l):
      dibuja_casilla(i, j)

def dibuja_casilla(i, j):
  global t, bomba_abierta
  t.goto(j+.5, i)
  t.begin_fill()
  if tablero[i][j] == cerrado:
    t.fillcolor('grey')
    t.circle(.5)
  elif tablero[i][j] == bandera:
    t.fillcolor('red')
    t.circle(.5)
  else:
    if bomb_num[i][j] == bomba:
      t.fillcolor('white')
      t.circle(.5)
      t.end_fill()
      t.begin_fill()
      t.fillcolor('black')
      t.circle(.2)
      bomba_abierta = True
    elif bomb_num[i][j] != 0:
      t.fillcolor('white')
      t.circle(.5)
      t.goto(j+.5, i+.25)
      t.write(bomb_num[i][j])
    else:
      t.fillcolor('white')
      t.circle(.5)
      t.end_fill()
      abrir_vacias(tablero, bomb_num, i, j)
  t.end_fill()

def abrir_vacias (tablero, bomb_num, i, j):
  if i-1 in range(w) and j-1 in range(l):
    if tablero[i-1][j-1] == cerrado:
      tablero[i-1][j-1] = abierto
      dibuja_casilla(i-1, j-1)
  if i-1 in range(w):
    if tablero[i-1][j] == cerrado:
      tablero[i-1][j] = abierto
      dibuja_casilla(i-1, j)
  if i-1 in range(w) and j+1 in range(l):
    if tablero[i-1][j+1] == cerrado:
      tablero[i-1][j+1] = abierto
      dibuja_casilla(i-1, j+1)
  if j-1 in range(l):
    if tablero[i][j-1] == cerrado:
      tablero[i][j-1] = abierto
      dibuja_casilla(i, j-1)
  if j+1 in range(l):
    if tablero[i][j+1] == cerrado:
      tablero[i][j+1] = abierto
      dibuja_casilla(i, j+1)
  if i+1 in range(w) and j-1 in range(l):
    if tablero[i+1][j-1] == cerrado:
      tablero[i+1][j-1] = abierto
      dibuja_casilla(i+1, j-1)
  if i+1 in range(w):
    if tablero[i+1][j] == cerrado:
      tablero[i+1][j] = abierto
      dibuja_casilla(i+1, j)
  if i+1 in range(w) and j+1 in range(l):
    if tablero[i+1][j+1] == cerrado:
      tablero[i+1][j+1] = abierto
      dibuja_casilla(i+1, j+1)

def clicL (x, y):
  global p, bomba_abierta
  [j, i] = [int(x), int(y)]
  if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
  
    if tablero[i][j] == cerrado:
      tablero[i][j] = abierto
      dibuja_casilla(i, j)
      if bomba_abierta:		#Perdiste o ganaste?
        sleep(2)
        t.clear()
        t.goto(w/2, l/2)
        t.color('black')
        t.write('Game over :(')
        sleep(2)
        p.bye()
      else: win()
      
    elif tablero[i][j] == abierto:			#Se fija si se pueden abrir casillas
      if bomb_num[i][j] > 0:
        contador = 0
        if i-1 in range(w) and j-1 in range(l):
          if tablero[i-1][j-1] == bandera:
            contador += 1
        if i-1 in range(w):
          if tablero[i-1][j] == bandera:
            contador += 1
        if i-1 in range(w) and j+1 in range(l):
          if tablero[i-1][j+1] == bandera:
            contador += 1
        if j-1 in range(l):
          if tablero[i][j-1] == bandera:
            contador += 1
        if j+1 in range(l):
          if tablero[i][j+1] == bandera:
            contador += 1
        if i+1 in range(w) and j-1 in range(l):
          if tablero[i+1][j-1] == bandera:
            contador += 1
        if i+1 in range(w):
          if tablero[i+1][j] == bandera:
            contador += 1
        if i+1 in range(w) and j+1 in range(l):
          if tablero[i+1][j+1] == bandera:
            contador += 1
            
        if bomb_num[i][j] == contador:			#Abre 8 casillas y las dibuja
          if i-1 in range(w) and j-1 in range(l):
            if tablero[i-1][j-1] == cerrado:
              tablero[i-1][j-1] = abierto
              dibuja_casilla(i-1, j-1)
          if i-1 in range(w):
            if tablero[i-1][j] == cerrado:
              tablero[i-1][j] = abierto
              dibuja_casilla(i-1, j)
          if i-1 in range(w) and j+1 in range(l):
            if tablero[i-1][j+1] == cerrado:
              tablero[i-1][j+1] = abierto
              dibuja_casilla(i-1, j+1)
          if j-1 in range(l):
            if tablero[i][j-1] == cerrado:
              tablero[i][j-1] = abierto
              dibuja_casilla(i, j-1)
          if j+1 in range(l):
            if tablero[i][j+1] == cerrado:
              tablero[i][j+1] = abierto
              dibuja_casilla(i, j+1)
          if i+1 in range(w) and j-1 in range(l):
            if tablero[i+1][j-1] == cerrado:
              tablero[i+1][j-1] = abierto
              dibuja_casilla(i+1, j-1)
          if i+1 in range(w):
            if tablero[i+1][j] == cerrado:
              tablero[i+1][j] = abierto
              dibuja_casilla(i+1, j)
          if i+1 in range(w) and j+1 in range(l):
            if tablero[i+1][j+1] == cerrado:
              tablero[i+1][j+1] = abierto
              dibuja_casilla(i+1, j+1)
              
      win()	#Ganaste?
      

def clicR (x, y):
  global tablero, bomb_num
  [j, i] = [int(x), int(y)]
  if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
    if tablero[i][j] == cerrado:
      tablero[i][j] = bandera
      dibuja_casilla(i, j)
      win()	#Ganaste?
    elif tablero[i][j] == bandera:
      tablero[i][j] = cerrado
      dibuja_casilla(i, j)


def win():
  for i in range(w):
    for j in range(l):
      if tablero[i][j] == cerrado:
        return False
  t.clear()
  t.goto(w/2, l/2)
  t.color('black')
  t.write("¡¡Ganaste!!")
  sleep(2)
  p.bye()


#-----PROGRAMA PRINCIPAL----------

#VARIABLES
cerrado, bandera, abierto  =  0, 1, 2	# tablero: Estados de las casillas
bomba = -1				# bomb_num
bomba_abierta = False			# Para verificar si perdiste

l = int(input('Largo: '))
w = int(input('Ancho: '))
cant_bombas = int(input('cantidad de bombas: '))


# Se inicializa la tortuga
p = Screen()
p.setup(l*50, w*50)
p.screensize(l*50, w*50)
p.setworldcoordinates(-.5, -.5, l+.5, w+.5)
p.delay(0)
t = Turtle()
t.hideturtle()


bomb_num = crea_matriz(w, l)
tablero = crea_matriz(w, l)

pone_bombas()
pone_numeros()
dibuja_tablero()

p.onclick(clicL, btn=1)
p.onclick(clicR, btn=3)

p.mainloop()

