import random
import sys
from usuario import IA, introducir_num


def desea_jugar():
    valor=0
    palabra=input("Si quiere jugar escriba si, sino quiere escriba cualquier cosa\n")
    palabra=palabra.lower()
    if palabra=='si':
        valor=1
    return valor

def fun_usuario ():
  try:
    valor = int (input("Escriba un 1 si quiere usar la IA, si quiere jugar usted escriba un 0\n"))
    while valor!=0 and valor!=1:
      valor = int (input("Escriba un 1 si quiere usar la IA, si quiere jugar usted escriba un 0\n"))

  except:
    pass
  else:
    return valor

def indicar_dificultad():
    limite_inferior=0
    try:
        dificultad = int (input("Indicar el nivel de dificultad\nNivel simple [0, 100] pulse 1\nNivel Intermedio[0, 1.000] pulse 2\nNivel avanzado[0, 1.000.000] pulse 3\nNivel experto[0, 1.000.000.000.000] pulse 4\n"))
        while dificultad<1 or dificultad>4:
            dificultad = int (input("Indicar el nivel de dificultad\nNivel simple [0, 100] pulse 1\nNivel Intermedio[0, 1.000] pulse 2\nNivel avanzado[0, 1.000.000] pulse 3\nNivel experto[0, 1.000.000.000.000] pulse 4\n"))
    except:
        pass
    if dificultad==1:
        limite_superior=100
    elif dificultad==2:
      limite_superior=1000
    elif dificultad==3:
      limite_superior=1000000
    else:
        limite_superior=1000000000000

    return limite_inferior, limite_superior, dificultad

def ayuda():
    try:
        valor_ayuda = int (input ("Indicar con un 1 si quiere ayuda de rangos, sino escriba un 0\n"))
        while (valor_ayuda!=0 and valor_ayuda!=1):
            valor_ayuda = int( input ("Error. Indicar con un 1 si quiere ayuda de rangos, sino escriba un 0\n"))
    except:
        pass
    else:
        return valor_ayuda

def numero_maximo_intentos(dificultad):
    #x son el numero de intentos permitidos
    if dificultad==1:
        intentos=10
    elif dificultad==2:
        intentos=50
    elif dificultad==3:
        intentos=100
    else:
        intentos=1000
    return intentos
    

def adivinar_numero(numero, l_inf, l_sup, valor_ayuda, intentos_permitidos, usuario):
    contador_intentos=0
    while True:
        contador_intentos+=1
        if usuario==1:
          intento = IA(l_inf, l_sup)
        else:
          intento=introducir_num(l_inf, l_sup)

        if intento==numero:
            return contador_intentos
        
        else:
            if intento>numero:
                print("\nEl numero es menor")
                l_sup=intento-1
            else:
                print ("\nEl numero es mayor")
                l_inf=intento+1
            
            if valor_ayuda==1:
                print("Rango de valores [{}, {}]\n".format(l_inf,l_sup))
                
        if contador_intentos==intentos_permitidos:
            return 0



def jugar():
    contador=0
    while True:
        valor = desea_jugar()
        if valor==0:
            break

        l_inf, l_sup, dificultad = indicar_dificultad()  
        numero=random.randint(l_inf, l_sup)
        valor_ayuda = ayuda()
        intentos_permitidos = numero_maximo_intentos(dificultad)
        usuario = fun_usuario()
        nºintentos = adivinar_numero (numero, l_inf, l_sup, valor_ayuda, intentos_permitidos, usuario)

        if nºintentos==0:
            print ("Ha utilizado el número máximo de oportunidades\n")
        else:
            print ("Ha acertado con {} intentos\n".format(nºintentos))
        contador+=1  
    if contador==1:
        print ("Ha jugado {} vez\n".format(contador))
    else:
        print ("Ha jugado {} veces\n".format(contador))

if __name__=='__main__':
    print ("Es este modulo\n")
    jugar()
else:
    print ("Se ha importado el modulo\n")
