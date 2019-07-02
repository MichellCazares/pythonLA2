# -*- coding: utf-8 -*-
# Nombre: circunferencia.py
# Objetivo: calcula el area y el diametro de una circunferencia e import
# math
# Autor: Michell Cázares
# Fecha: 01 de Julio de 2019

def calculaPerimetro(l1,l2,l3):
    return l1+l2+l3

def identificar(l1,l2,l3):
    if l1 == l2 and l1 == l3:
        print("El triangulo es equilatero.")
    elif ((l1==l2 and l1!=l3) or (l1==l3 and l1!=l2) or (l2==l3 and l2!=l1)):
        print("El triangulo es isosceles.")
    elif(l1!=l2 and l1!=l3 and l2!=l3):
        print("El triangulo es escaleno.")


def main():
    l1 = float(input("Lado 1: "))
    l2 = float(input("Lado 2: "))
    l3 = float(input ("Lado 3: "))
    identificar(l1,l2,l3)
    print("El perimetro es: " ,calculaPerimetro(l1,l2,l3))


if __name__ == "__main__":
    main()