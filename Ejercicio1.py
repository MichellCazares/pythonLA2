#

def main():
    st = float(input("Ingrese su sueldo: "))
    if(st<1000):
        st = st*1.15
    elif(st>=1000):
        st = st*1.12

    print("Su sueldo nuevo es: ",st)

if __name__ == "__main__":
    main()

