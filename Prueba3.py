import random
import sys

def indicar_dificultad():
    limite_inferior=0
    try:
        w = int (input("Indicar el nivel de dificultad\nNivel simple [0, 100] pulse 1\nNivel Intermedio[0, 1.000] pulse 2\nNivel avanzado[0, 1.000.000] pulse 3\nNivel experto[0, 1.000.000.000.000] pulse 4\n"))
        while w<1 or w>4:
            w = int (input("Indicar el nivel de dificultad\nNivel simple [0, 100] pulse 1\nNivel Intermedio[0, 1.000] pulse 2\nNivel avanzado[0, 1.000.000] pulse 3\nNivel experto[0, 1.000.000.000.000] pulse 4\n"))
    except:
        pass
    if w=1:
        limite_superior=100
    elif w=4:
        limite_superior=1000000000000
    else:
        limite_superior=1000^(w-1)
    return limite_inferior, limite_superior

def ayuda():
    c = input ("Indicar con un 1 si quiere ayuda de rangos, sino escriba un 0\n")
    while (c!=0 or c!=1):
        c = input ("Error. Indicar con un 1 si quiere ayuda de rangos, sino escriba un 0\n")
    return c

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

def adivinar_numero_con_ayuda(numero, l_inf, l_sup):
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

def adivinar_numero_sin_ayuda ():
    
def main():
    l_inf, l_sup = indicar_dificultad()  
    numero=random.randint(l_inf,l_sup)
    u = ayuda()
    if ayuda == 1:
        adivinar_numero_con_ayuda(numero, )
 
    nºintentos = adivinar_numero(numero, l_inf, l_sup)
    print("Ha acertado con {} intentos\n".format(nºintentos))
main()
