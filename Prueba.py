import random
numero=random.randint(0,100)
import sys

def introducir_num():
  try:
    intento = int(input("Escriba un numero\n"))
  except:
    pass
  else:
    return intento
  sys.exit()

def adivinar_numero():
  l_sup=100
  l_inf=0
  i=0
  while True:
    i+=1
    x=introducir_num()
    if x==numero:
      print("Ha acertado el numero con {} intentos\n".format(i))
      break
    elif x>numero:
      l_sup=x
      print("Rango de valores ({}, {})\n".format(l_inf,l_sup))
    else:
      l_inf=x
      print("Rango de valores ({}, {})\n".format(l_inf, l_sup))
adivinar_numero()


  
  