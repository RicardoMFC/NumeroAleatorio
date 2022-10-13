import random
numero=random.randint(0,100)
import sys

def introducir_num():
  try:
    intento = int(input("Escriba un numero\n"))
    while intento<0 or intento>100:
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
    l_sup = indicar_lim_sup()
    l_inf = indicar_lim_inf()
    z=comparacion_limites(l_inf,l_sup)

    while z!=1:
      l_sup = indicar_lim_sup()
      l_inf = indicar_lim_inf()
      z=comparacion_limites(l_inf,l_sup)
  except:
    pass
    
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

def indicar_lim_inf():
  try:
    limite_inferior= int (innput("Escriba el limite inferior\n"))
  except:
    pass
  else:
    return limite_inferior

def indicar_lim_sup():
    try:
    limite_superior= int (innput("Escriba el limite inferior\n"))
  except:
    pass
  else:
    return limite_superior
  
def comparacion_limites(x,y):
  val=0
  if x<y:
    val=1
  return val
