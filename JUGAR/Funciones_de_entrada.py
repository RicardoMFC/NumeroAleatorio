def desea_jugar():
    valor=0 #Supongo que no va a introducir si, si introduce si cambio el valor a 1.
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

def IA(l_inf,l_sup):
    intento = int ((l_sup+l_inf)/2)
    print(intento)
    return intento

def introducir_num(l_inf,l_sup):
  try:
    intento = int(input("Escriba un numero\n"))
    while intento<l_inf or intento>l_sup:
      intento = int(input("Escriba otro numero\n"))
  except:
    pass
  else:
    return intento

