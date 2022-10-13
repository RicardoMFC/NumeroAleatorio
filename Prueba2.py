import random
import sys

def indicarLimites():
  while True:
    limite_inferior= int (input("Escriba el limite inferior\n"))
    limite_superior= int (input("Escriba el limite superior\n"))
    if limite_inferior<limite_superior:
      return limite_inferior, limite_superior

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

def adivinar_numero(t, numero, l_inf, l_sup):
  val=0
  if t==numero:
    val=1
  elif t>numero:
    l_sup=t-1
    print("Rango de valores [{}, {}]\n".format(l_inf,l_sup))
  else:
    l_inf=t+1
    print("Rango de valores [{}, {}]\n".format(l_inf, l_sup))
    
  return val, l_inf, l_sup
    
def main():
  l_inf, l_sup = indicarLimites()
  numero=random.randint(l_inf,l_sup)
  contador=0
  while True:
    contador+=1
    x=introducir_num(l_inf, l_sup)
    y, l_inf, l_sup = adivinar_numero(x, numero, l_inf, l_sup)
    if y==1:
      print("Ha acertado con {} intentos\n".format(contador))
      break
main()