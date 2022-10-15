import random
import sys

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
    
def IA(l_inf,l_sup):
    intento = int ((l_sup+l_inf)/2)
    print(intento)
    return intento

def adivinar_numero(numero, l_inf, l_sup, valor_ayuda, intentos_permitidos):
    contador_intentos=0
    while True:
        contador_intentos+=1
        intento=IA(l_inf, l_sup)

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

    l_inf, l_sup, dificultad = indicar_dificultad()  
    numero=random.randint(l_inf, l_sup)
    valor_ayuda = ayuda()
    intentos_permitidos = numero_maximo_intentos(dificultad)
    nºintentos = adivinar_numero (numero, l_inf, l_sup, valor_ayuda, intentos_permitidos)

    if nºintentos==0:
        print ("Ha utilizado el número máximo de oportunidades\n")
    else:
        print("Ha acertado con {} intentos\n".format(nºintentos))  
jugar()
