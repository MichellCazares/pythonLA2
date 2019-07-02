# -*- coding: utf-8 -*-
# Nombre: circunferencia.py
# Objetivo: calcula el area y el diametro de una circunferencia e import
# math
# Autor: Michell Cázares
# Fecha: 01 de Julio de 2019
import math as mat
#------------------------------
# Función para calcular área
#------------------------------
def calcularArea(radio):
    area = mat.pi(pow(radio,2))
    return area

#------------------------------
# Función para calcular el diámetro
#------------------------------
def calcularDiametro(radio):
    diam=radio*2
    return diam


def main():
    ciclo = true
    while(ciclo == true)
        print("-- Script para calcular Área de Circunferencia --")
        print("Introduce el valor del radio: ")
        radio = float (input("Introduce el valor del radio: "))
        #Invocar un método
        print("El área es: " + calculaArea(radio))
        print("El diámetro es: " + calcularDiametro())
        resp = input("¿Desea hacer otro cálculo? s/n")
        if(resp=="S" or resp == "s"):
            ciclo = true
        else:
            ciclo = false
    else:
        print("Fin de programa.")

if __name__: == "__main__":
    main()