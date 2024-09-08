from time import localtime
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    t=localtime()
    diaact=t.tm_mday
    mesact=t.tm_mon
    annoact=t.tm_year

    if mesact<mes:
        if diaact<dia:
            edad=abs(anno-annoact)-1
    else:
        edad=abs(anno-annoact)    
    return "Usted tiene "+str(edad)+" años" 

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
