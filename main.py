import random
numero=random.randint(0,100)

def introducir_num():
  intento = int(input("Escriba un numero\n"))
  while intento<0 or intento>100:
    intento = int(input("Escriba un numero\n"))
  return intento
  
def adivinar_numero(intento):
  while True:
    introducir_num()
    if intento==numero:
      print("Ha acertado el numero\n")
      break
    elif intento>numero:
      print("El numero es menor\n")
    else:
      print("El numero es mayor\n")




  


  
