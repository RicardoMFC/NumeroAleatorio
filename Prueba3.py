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

def adivinar_numero(numero, l_inf, l_sup):
    contador=0
    while True:
        contador+=1
        x=introducir_num(l_inf, l_sup)
        if x==numero:
            return contador
        elif x>numero:
            l_sup=x-1
            print("Rango de valores [{}, {}]\n".format(l_inf,l_sup))
        else:
            l_inf=x+1
            print("Rango de valores [{}, {}]\n".format(l_inf, l_sup))
    
def main():
    l_inf, l_sup = indicarLimites()
    numero=random.randint(l_inf,l_sup)
    nºintentos = adivinar_numero(numero, l_inf, l_sup)
    print("Ha acertado con {} intentos\n".format(nºintentos))
main()
