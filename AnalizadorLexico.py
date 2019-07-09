# Script para analizar lexicamente la sentencia printf en ansi c
# Autor: Michell Cazares
# Fecha:

def lexico(inst):
    f=inst[0:6]
    print("La palabra reservada: ",f)
    d=inst[6]
    print("El parentesis de apertura: ",d)
    e=inst.find(")")
    a=inst[e]
    t=inst[7:e]
    print("La cadena de caracteres: ",t)
    print("El parentesis de cierre: ",a)
    i=inst.find(";")
    j=inst[i]
    print("El simbolo de fin de sentencia: ",j)

def main():
    print("Analisis lexico de sentencia printf.")
    sentencia = "printf('Hola');"
    lexico(sentencia)

if __name__ == "__main__":
    main()