# -*- coding: utf-8 -*-
# Nombre: factorial.py
# Objetivo: calcula el factorial
# math
# Autor: Michell Cázares
# Fecha: 01 de Julio de 2019


def fact(n):
    if(n<1):
        return 1
    else:
        return n * fact(n-1)

    
def main():
    print("Cálculo de Factorial")
    n = int(input("Número: "))
    print(str(fact(n)))

if __name__=="__main__":
    main()