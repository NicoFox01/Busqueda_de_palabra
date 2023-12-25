def encuentra_palabra():
    oracion_macro = input("Escriba el texto sobre el cual vamos a trabajar:")
    palabra_buscada = input("¿Qué palabra deseas buscar?")
    
    if oracion_macro.find(palabra_buscada) != -1:
        print("La palabra se encuentra")
    else:
        print("La palabra no se encuentra")

encuentra_palabra()
