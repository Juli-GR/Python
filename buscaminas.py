from random import randrange
from turtle import Screen, Turtle
from time import sleep

cerrado = 0
bandera = 1
abierto = 2

bomba = -1

bomba_abierta = False

def crea_matriz(w, l): #Crea matriz de ceros
  matriz = []
  for i in range(w):
    matriz.append([0]*l)
  return matriz

#Pone bombas(-1) y sus respectivos numeros(1 to 8)
#Casillas vacias == 0
def rellena_matriz(matriz, w, l): 
  bombas = cant_bombas
  for i in range(bombas):
    [a, b] = [randrange(w), randrange(l)]
    while matriz[a][b] == bomba:
      [a, b] = [randrange(w), randrange(l)]
    matriz[a][b] = bomba
  
  for i in range(w):
    for j in range(l):
      if matriz[i][j] == bomba:
        if i-1 in range(w) and j-1 in range(l):
          if matriz[i-1][j-1] != bomba:
            matriz[i-1][j-1] += 1
        if i-1 in range(w):
          if matriz[i-1][j] != bomba:
            matriz[i-1][j] += 1
        if i-1 in range(w) and j+1 in range(l):
          if matriz[i-1][j+1] != bomba:
            matriz[i-1][j+1] += 1
        if j-1 in range(l):
          if matriz[i][j-1] != bomba:
            matriz[i][j-1] += 1
        if j+1 in range(l):
          if matriz[i][j+1] != bomba:
            matriz[i][j+1] += 1
        if i+1 in range(w) and j-1 in range(l):
          if matriz[i+1][j-1] != bomba:
            matriz[i+1][j-1] += 1
        if i+1 in range(w):
          if matriz[i+1][j] != bomba:
            matriz[i+1][j] += 1
        if i+1 in range(w) and j+1 in range(l):
          if matriz[i+1][j+1] != bomba:
            matriz[i+1][j+1] += 1

def dibuja_tablero(tablero, bomb_num, w, l):
  for i in range(w):
    for j in range(l):
      dibuja_casilla(tablero, bomb_num, i, j)

def dibuja_casilla(tablero, bomb_num, i, j):
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
      dibuja_casilla(tablero, bomb_num, i-1, j-1)
  if i-1 in range(w):
    if tablero[i-1][j] == cerrado:
      tablero[i-1][j] = abierto
      dibuja_casilla(tablero, bomb_num, i-1, j)
  if i-1 in range(w) and j+1 in range(l):
    if tablero[i-1][j+1] == cerrado:
      tablero[i-1][j+1] = abierto
      dibuja_casilla(tablero, bomb_num, i-1, j+1)
  if j-1 in range(l):
    if tablero[i][j-1] == cerrado:
      tablero[i][j-1] = abierto
      dibuja_casilla(tablero, bomb_num, i, j-1)
  if j+1 in range(l):
    if tablero[i][j+1] == cerrado:
      tablero[i][j+1] = abierto
      dibuja_casilla(tablero, bomb_num, i, j+1)
  if i+1 in range(w) and j-1 in range(l):
    if tablero[i+1][j-1] == cerrado:
      tablero[i+1][j-1] = abierto
      dibuja_casilla(tablero, bomb_num, i+1, j-1)
  if i+1 in range(w):
    if tablero[i+1][j] == cerrado:
      tablero[i+1][j] = abierto
      dibuja_casilla(tablero, bomb_num, i+1, j)
  if i+1 in range(w) and j+1 in range(l):
    if tablero[i+1][j+1] == cerrado:
      tablero[i+1][j+1] = abierto
      dibuja_casilla(tablero, bomb_num, i+1, j+1)

def clicL (x, y):
  global pantalla, tablero, bomb_num, w, l, bomba_abierta
  [j, i] = [int(x), int(y)]
  if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
    if tablero[i][j] == cerrado:
      tablero[i][j] = abierto
      dibuja_casilla(tablero, bomb_num, i, j)
    elif tablero[i][j] == abierto:                                 #Se fija si se pueden abrir casillas
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
            
        if bomb_num[i][j] == contador:                          #Abre 8 casillas y las dibuja
          if i-1 in range(w) and j-1 in range(l):
            if tablero[i-1][j-1] == cerrado:
              tablero[i-1][j-1] = abierto
              dibuja_casilla(tablero, bomb_num, i-1, j-1)
          if i-1 in range(w):
            if tablero[i-1][j] == cerrado:
              tablero[i-1][j] = abierto
              dibuja_casilla(tablero, bomb_num, i-1, j)
          if i-1 in range(w) and j+1 in range(l):
            if tablero[i-1][j+1] == cerrado:
              tablero[i-1][j+1] = abierto
              dibuja_casilla(tablero, bomb_num, i-1, j+1)
          if j-1 in range(l):
            if tablero[i][j-1] == cerrado:
              tablero[i][j-1] = abierto
              dibuja_casilla(tablero, bomb_num, i, j-1)
          if j+1 in range(l):
            if tablero[i][j+1] == cerrado:
              tablero[i][j+1] = abierto
              dibuja_casilla(tablero, bomb_num, i, j+1)
          if i+1 in range(w) and j-1 in range(l):
            if tablero[i+1][j-1] == cerrado:
              tablero[i+1][j-1] = abierto
              dibuja_casilla(tablero, bomb_num, i+1, j-1)
          if i+1 in range(w):
            if tablero[i+1][j] == cerrado:
              tablero[i+1][j] = abierto
              dibuja_casilla(tablero, bomb_num, i+1, j)
          if i+1 in range(w) and j+1 in range(l):
            if tablero[i+1][j+1] == cerrado:
              tablero[i+1][j+1] = abierto
              dibuja_casilla(tablero, bomb_num, i+1, j+1)
              
  if bomba_abierta:
    sleep(2)
    t.clear()
    t.goto(w/2, l/2)
    t.color('black')
    t.write('Game over :(')
    sleep(2)
    pantalla.bye()
  elif win():
    t.clear()
    t.goto(w/2, l/2)
    t.color('black')
    t.write("Ganaste!!!! Vamo' loco!!!")
    print('\a')
    sleep(0.3)
    print('\a')
    sleep(0.2)
    print('\a')
    sleep(0.1)
    print('\a')
    sleep(0.05)
    print('\a')
    sleep(0.05)
    print('\a')
    sleep(0.05)
    print('\a')
    sleep(2)
    pantalla.bye()
  
def win():
  global w, l
  ganaste = True
  for i in range(w):
    for j in range(l):
      if tablero[i][j] == cerrado:
        ganaste = False
        return ganaste
  return ganaste

def clicR (x, y):
  global tablero, bomb_num
  [j, i] = [int(x), int(y)]
  if 0 <= i < len(tablero) and 0 <= j < len(tablero[0]):
    if tablero[i][j] == cerrado:
      tablero[i][j] = bandera
      dibuja_casilla(tablero, bomb_num, i, j)
    elif tablero[i][j] == bandera:
      tablero[i][j] = cerrado
      dibuja_casilla(tablero, bomb_num, i, j)

#Programa principal
l = int(input('largo: '))
w = int(input('ancho: '))
cant_bombas = int(input('cantidad de bombas: '))

pantalla = Screen()
pantalla.setup(l*50, w*50)
pantalla.screensize(l*50, w*50)
pantalla.setworldcoordinates(-.5, -.5, l+.5, w+.5)
pantalla.delay(0)
t = Turtle()
t.hideturtle()

bomb_num = crea_matriz(w, l)
tablero = crea_matriz(w, l)

rellena_matriz(bomb_num, w, l)
t.penup()
dibuja_tablero(tablero, bomb_num, w, l)

pantalla.onclick(clicL, btn=1)
pantalla.onclick(clicR, btn=3)

pantalla.mainloop()

