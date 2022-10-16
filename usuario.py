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
  sys.exit()
