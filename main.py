import random
numero=random.randint(0,100)
def introducir_num(x)
i=0 #def 
intento = int(input("Escriba un numero\n"))

while True:    
  while intento<0 or intento>100:
    intento = int(input("Escriba un numero\n"))

  if intento==numero:
    print("Ha acertado el numero\n")
    break
  elif intento>numero:
    print("El numero es menor\n")
  else:
    print("El numero es mayor\n")
  intento=-1
  i=i+1

print(i)
#if name==

  
  


  
