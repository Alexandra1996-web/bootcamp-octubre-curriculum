palabra_correcta = "animo"

palabra_ingresada = input("Ingrese una palabra de 5 letras:  ")

lista_de_letras_de_palabra_correcta = list(palabra_correcta)
lista_de_letras_de_palabra_ingresada = list(palabra_ingresada)
print(lista_de_letras_de_palabra_correcta)
print(lista_de_letras_de_palabra_ingresada)

cantidad_de_letras = 5

for posicion_de_letra in range(cantidad_de_letras):
  

  las_letras_son_iguales = palabra_ingresada[posicion_de_letra] == palabra_correcta[posicion_de_letra]

  las_letras_existen = lista_de_letras_de_palabra_ingresada[posicion_de_letra] in lista_de_letras_de_palabra_correcta

  if (las_letras_son_iguales):
    print( f"[ {palabra_ingresada[posicion_de_letra]} ]" )
  elif (las_letras_existen):
    print( f"( {palabra_ingresada[posicion_de_letra]} )" )
  else:
    print( f" {palabra_ingresada} " )



