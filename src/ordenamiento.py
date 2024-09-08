def evaluar(numero1, numero2, numero3, numero4):
    # TODO: Coloca aquí el código del ejercicio 5: Ordenamiento
    lista=[]
    lista.append(numero1)
    lista.append(numero2)
    lista.append(numero3)
    lista.append(numero4)
    lista.sort()

    lis= str(lista[0])+" "+str(lista[1])+" "+str(lista[2])+" "+str(lista[3])
    return lis

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
