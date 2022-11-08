'''
-Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
que calcule el mínimo común múltiplo (mcm) de dos números enteros.
-No se pueden utilizar operaciones del lenguaje que 
lo resuelvan directamente.
 '''

 #El mínimo común múltiplo de dos números es el número más pequeño común a los dos entre los que se pueden dividir
 #El máximo común divisor de dos números es el número más grande común a los dos 

def MCD(a,b):
    temporal = 0
    if b != 0:
        temporal = b
        b = a % b 
        a = temporal

    return a

def mcm(a,b):



    return 
 