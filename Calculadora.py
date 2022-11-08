'''
   -Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
  resultado e imprímelo.
   -El .txt se corresponde con las entradas de una calculadora.
   -Cada línea tendrá un número o una operación representada por un
   símbolo (alternando ambos).
   -Soporta números enteros y decimales.
   -Soporta las operaciones suma "+", resta "-", multiplicación "*"
   y división "/".
   -El resultado se muestra al finalizar la lectura de la última
   línea (si el .txt es correcto).
   -Si el formato del .txt no es correcto, se indicará que no se han
   podido resolver las operaciones.
'''
#Defino funciones para hacer las operaciones.
def suma (x,y):
    return x + y

def resta (x,y):
    return x-y

def mult (x,y):
    return x*y

def resta (x,y):
    return x-y

#Leer fichero
#f = open('Operacion.txt', mode = 'r')
#lines = f.readlines()
file = 'Operacion.txt'
with open(file, mode = 'r') as f:
    lines = f.readlines()

print('Selecciona operacion: ')
print('1.Add')
print('2.Substract')
print('3.Divide')
print('4.Product')

while True: 
    #Pedimos input al usuario
    n1 = input('Dime el primer numero: ')
    n2 = input('Dime el segundo numero: ')  
    operacion = input('Dime el tipo de operacion dentro de las opciones anteriores: ')
    
    #Mirar que sea correcta la opcion
    if operacion in ('1', '2', '3', '4'):
        if operacion == '1':
            print(n1, "+", n2, "=", int(n1)+int(n2))
        if operacion == '2':
            print(n1, "+", n2, "=", int(n1)-int(n2))
        if operacion == '3':
            print(n1, "/", n2, "=", int(n1)/int(n2))
        if operacion == '4':
            print(n1, "*", n2, "=", int(n1)*int(n2))       
    
        siguiente_calculo = input('¿Quieres hacer otro cálculo?(yes/no): ')
        if siguiente_calculo in ('no', 'n'):
            break

    else:
        print('Invalid Input')

