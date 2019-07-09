# -*- coding: utf-8 -*-
def main():
    cat = input("Ingrese su categoría 1-5: " )
    saldo = float(input("Ingrese su sueldo: "))

    if(cat == 1):
        saldo = saldo*1.15
        print("El nuevo saldo es: ",saldo)
    elif(cat==2):
        saldo = saldo*1.10
        print("El nuevo saldo es: ",saldo)
    elif(cat==3):
        saldo = saldo*1.08
        print("El nuevo saldo es: ",saldo)
    elif(cat==4):
        saldo = saldo*1.07
        print("El nuevo saldo es: ",saldo)
    else:
        print("No existe la categoría dada.")

if __name__ == "__main__":
    main()