def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    letra=int(caracter)
    if(letra>=48 and letra<=57):
        salida= "Es número"
    elif (letra>=65 and letra<=90):
        salida= "Es letra mayúscula"
    elif(letra>=97 and letra<=122):
        salida= "Es letra minúscula"
    else:
        salida= "No es letra ni número"
    print(letra)
    return salida

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
