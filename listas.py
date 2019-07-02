# -*- coding: utf-8 -*-
# Nombre: listas.py
# Objetivo: muestra el funcionamiento de las listas en python
# math
# Autor: Michell Cázares
# Fecha: 02 de Julio de 2019

lista = []

def agregarItem(dato):
    lista.append(dato)

def imprimirList():
    j=0
    for i in lista:
        print("Item: ",j,",",i)
        j+=1

def eliminardato(dato):
    if(dato in lista):
        lista.remove(dato)
        print("Item eliminado.")
    else:
        print("El item no se ha encontrado.")

def main():
    ciclo = True
    while(ciclo == True):
        print("-- Script para Trabajar con Listas --")
        print("1. Agregar elementos a la lista.")
        print("2. Buscar un elemento en la lista.")
        print("3. Modificar un elemento en la lista.")
        print("4. Eliminar un elemento de la lista.")
        print("5. Imprimir los elementos de la lista.")
        print("0. Salir.")
        opc = int(input("\nSeleccione una opción: "))

        if(opc == 1):
            item = input("Introduce valor del elemento: ")
            agregarItem(item)
        elif(opc == 2):
            print("2")
        elif(opc == 3 ):
            print("3")
        elif(opc==4):
            eliminardato(input("Ingrese el dato a eliminar: "))
        elif(opc==5):
            imprimirList()
        elif(opc==0):
            SystemExit
            ciclo=False
        else:
            print("Favor de elegir una opción válida.")
        resp = input("Desea hacer otra acción: s/n \n")
        if( resp == "s" or resp == "S" ):
            ciclo = True
        else:
            ciclo = False


if __name__ == "__main__":
    main()