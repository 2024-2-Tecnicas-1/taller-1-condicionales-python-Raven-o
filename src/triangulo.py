def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if a+b>c and b+c>a and a+c>b:
        if a==b and b==c:
            return "El triángulo es equilátero"
        elif a==b or b==c or a==c:
            return "El triángulo es isósceles"
        else:
            return "El triángulo es escaleno"
    else: return "No es un triángulo válido"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
