from Funciones_de_entrada import *
import random


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
        valor_si_no = desea_jugar()
        if valor_si_no==0:
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
    


