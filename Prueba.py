import random
import sys

def indicar_lim_inf():
  limite_inferior= int (input("Escriba el limite inferior\n"))
  return limite_inferior

def indicar_lim_sup():
  limite_superior= int (input("Escriba el limite superior\n"))
  return limite_superior
  
def comparacion_limites(x,y):
  val=0
  if x<y:
    val=1
  return val

def introducir_num(a,b):
  try:
    intento = int(input("Escriba un numero\n"))
    while intento<a or intento>b:
      intento = int(input("Escriba otro numero\n"))
  except:
    pass
  else:
    return intento
  sys.exit()

def adivinar_numero():
  l_sup = indicar_lim_sup()
  l_inf = indicar_lim_inf()
  try:
    z=comparacion_limites(l_inf,l_sup)
    while z==0:
      l_sup = indicar_lim_sup()
      l_inf = indicar_lim_inf()
      z=comparacion_limites(l_inf,l_sup)

  except:
    pass
  numero=random.randint(l_inf,l_sup)

  numero_intentos=0
  while True:
    numero_intentos+=1
    x=introducir_num(l_inf,l_sup)
    if x==numero:
      print("Ha acertado el numero con {} intentos\n".format(numero_intentos))
      break
    elif x>numero:
      l_sup=x
      print("Rango de valores ({}, {})\n".format(l_inf,l_sup))
    else:
      l_inf=x
      print("Rango de valores ({}, {})\n".format(l_inf, l_sup))
adivinar_numero()