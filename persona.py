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
