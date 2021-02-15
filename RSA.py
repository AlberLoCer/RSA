#Aldair Maldonado Honores y Alberto López Cervantes

import numpy
import math


alphabetSwitcher = {        #Diccionario para traducir un valor numérico a 
    0:" ",                  #alfabético
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h",
    9:"i",
    10:"j",
    11:"k",
    12:"l",
    13:"m",
    14:"n",
    15:"o",
    16:"p",
    17:"q",
    18:"r",
    19:"s",
    20:"t",
    21:"u",
    22:"v",
    23:"x",
    24:"y",
    25:"z"
}

# Nota: La función estándar de Python para la exponenciación, puede tomar 3 argumentos.
# Si los toma, hace una exponenciación modular, pasando de 
# tener una complejidad linal (Funcion de exponenciación estándar)
# a tener una complejidad logarítmica
# Sintaxis: pow(a,b,n) = a^b mod n

def inversaModular(a,b):    
    return pow(a, -1, b)        #Usando la función de exponenciación modular, ejecutamos:
                                # a^-1 mod b


class RSA(): 

    def cifrado(self, x, e, n): #(Texto plano ^ e) mod n
        res = pow(x, e, n) 
        return res

    def descifrado(self, c, d, n): #(Texto cifrado ^ d) mod n
        res = pow(c, d, n) 
        return res


    def generaClaves(self):
        #Generacion de claves para el primer locutor------------------------------------
        self.p1 = input("Introduce el primo p para el primer interlocutor: ")
        self.q1 = input("Introduce el primo q para el primer interlocutor:")
        self.n1 = int(self.p1)*int(self.q1)     #Generación de la clave pública n
        self.eulerN1 = (int(self.p1)-1)*(int(self.q1)-1)    #Cálculo de la función de Euler
        self.e1 = input("Introduce un número e para el primer interlocutor:")   #Clave pública e
        while(math.gcd(int(self.e1), self.eulerN1) != 1):   #Comprobación para que sea primo con phi(n)
            self.e1 = input("e debe ser primo con phi(n). Introduce un nuevo valor:")   

        self.d1 = inversaModular(int(self.e1),self.eulerN1)    #Calculo de la clave privada d
        print("Las claves del interlocutor A son: ")
        print("Clave pública p: ", self.p1)
        print("Clave pública q: ", self.q1)
        print("phi(n): ", self.eulerN1)
        print("Clave pública e: ", self.e1)
        print("Clave privada d: ", self.d1)
        

        #Generacion de claves para el segundo locutor----------------------------------
        self.p2 = input("Introduce el primo p para el segundo interlocutor:")
        self.q2 = input("Introduce el primo q para el segundo interlocutor:")
        self.n2 = int(self.p2)*int(self.q2)
        self.eulerN2 = (int(self.p2)-1)*(int(self.q2)-1)
        self.e2 = input("Introduce un número e:")
        while(math.gcd(int(self.e2),self.eulerN2) != 1):
            self.e2 = input("e debe ser primo con phi(n). Introduce un nuevo valor:")

        self.d2 = inversaModular(int(self.e2),self.eulerN2)
        print("Las claves del interlocutor B son: ")
        print("Clave pública p: ", self.p2)
        print("Clave pública q: ", self.q2)
        print("phi(n) : ", self.eulerN2)
        print("Clave pública e: ", self.e2)
        print("Clave privada d: ", self.d2)


                 

algoritmo = RSA()
algoritmo.generaClaves()
textoPlano = input("Introduce un texto a cifrar ")
textocifrado = ""
textoDescifrado = ""
for x in (textoPlano):
    cifrado = algoritmo.cifrado(ord(x)-96,int(algoritmo.e2),int(algoritmo.n2))          #Coversión de cada caracter en el texto plano a número
    textocifrado += alphabetSwitcher.get(cifrado % 26)                                  #Coversión del caracter cifrado de número a texto
    descifrado = algoritmo.descifrado(cifrado,int(algoritmo.d2),int(algoritmo.n2))      #Descifrado del caracter cifrado
    textoDescifrado+= alphabetSwitcher.get(descifrado)                                  #Conversión de vuelta a texto
    
print("Cifrado: ", textocifrado)
print("Descifrado: ", textoDescifrado)