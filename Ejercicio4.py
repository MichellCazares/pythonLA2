# -*- coding: utf-8 -*-
lista = []
n = 0
def capturarCal():
    global n
    ciclo = True
    while(ciclo == True):
        cal = float(input("Ingrese la calificacion del Alumno: "))
        lista.append(cal)
        n=n+1
        resp = input("Quiere capturar otra calificacion? s/n ")
        if( resp == "s" or resp == "S" ):
            ciclo = True
        else:
            ciclo = False
        

def promGen():
    suma = 0.0
    for i in lista:
        suma=suma+i
    promedio = suma/n
    print("El promedio es: ",promedio)

def numAprob():
    nAprob = 0
    for i in lista:
        if(i>=70):
            nAprob=nAprob+1
    return nAprob

def numReprob():
    nReprob = 0
    for i in lista:
        if(i<70):
            nReprob=nReprob+1
    return nReprob


def porcentajeAprob():
    nAprob = numAprob()
    porcentaje = (nAprob/n)*100
    return porcentaje
def porcentajeReprob():
    nReprob = numReprob()
    porcentaje = (nReprob/n)*100
    return porcentaje

def calMayorDe(cal):
    total = 0
    for i in lista:
        if(i>cal):
            total=total+1
    return total

def main():
    capturarCal()
    promGen()
    print("El numero de aprobados es: ",numAprob())
    print("El numero de reprobados es: ",numReprob())
    print("El porcentaje de aprobados es: ",porcentajeAprob())
    print("El porcentaje de reprobados es: ",porcentajeReprob())
    print("Total de calificaciones mayores a 80: ",calMayorDe(80))

if __name__ == "__main__":
    main()