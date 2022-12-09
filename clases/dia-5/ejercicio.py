def contiene_una_letra(letra,palabra):
    condicion_que_contenga=letra in palabra
    if condicion_que_contenga:
        contiene="["+letra+"]"
        return contiene
    else:
        no_contiene=letra
        return no_contiene

print(contiene_una_letra("a","hola"))