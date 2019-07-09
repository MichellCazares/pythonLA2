
# Nombre: punto.py
# Autor: Michell Cázares 
import math  
class punto(object):
        #contructor de la clase
        def __init__(self, valorx, valory):
            self.x=valorx
            self.y=valory
            
        def getx(self):
            return self.x
        def gety(self):
            return self.y
        #metodos set
        def setx(self, valorx):
            self.x=valorx
        def sety(self, valory):
            self.y=valory
        def toString(self):
            return "el punto tiene las siguientes coordenadas", self.x,",", self.y
class circuferencia(punto):
        def __init__(self, valorRadio):
            self.radio=valorRadio
        def getRadio(self):
            return self.radio
        def serRadio(self, valorRadio):
            self.radios=valorRadio
        def getArea(self):
            return math.pi * math.pow(self.getRadio(), 2)
        def toString(self):
            return "la circuferncia tiene como centro : ", self.getx(), ",", self.gety(), ", ", self.getRadio(), "el area es: ",self.getArea()
            
def main():
    p1=punto(2,3)
    print(p1.toString())
    #crear el objeto 2
    p2=punto(0,0)
    print(p2.toString())
    # invocar al metodo set 
    p2.setx(-2)
    p2.sety(-4)
    print(p2.toString())
    
    p3=circuferencia(12.34)
    p3.setx(10)
    p3.sety(12)
    print(p3.toString())
    

    
    
    
if __name__ == "__main__":
    main()
    
    
            
        
        
        
        
        
        
        
        
        