# Bucle For
# Ejemplo 1: Sumar los valores de una lista

num = [8, 4, 7, 9, 2, 5, 4, 9]
sum = 0
for i in num:
    sum = sum + i
print('La suma total es: ' + str(sum))

# ejemplo 2: Validar mail
contador = 0
mail = input('Ingrese su correo electrónico: ')
for i in mail:
    if i == '@' or i == '.':
        contador = contador + 1
if contador >= 2:
    print('El mail ingresado es correcto')
else:
    print('El mail ingresado es incorrecto')

print('El valor de "i" es: ' + str(contador))

# Ejemplo 3: crear una variable del del 1 al 100 que muestre solo los números impares

num = range(1, 16, 2)
for i in num:
    print(i)

# Ejemplo 4: solicitar contraseña que sea mayor de 8 carácteres y que no tenga espacio

clave = str(input('Ingrese la contraseña'))
validarLargoClave = len(clave)
validarClave = True

for i in clave:
    if i == ' ':
        validarClave = False

while validarClave == False or validarLargoClave < 8:
    print('La clave ingresada no cumple con los parámetros de seguridad')
    clave = str(input('Ingrese la contraseña'))
    validarLargoClave = len(clave)
    for i in clave:
        if i == ' ':
            validarClave = False
        else:
            validarClave = True

print('La contraseña ingresada es correcta.')

#Ejercicio 4: 
# Suma de números: Escribe un programa que calcule la suma de todos los números enteros desde 1 hasta un número ingresado por el usuario.

solicitarNum = int(input('Ingrese el número entero: '))
valores = range(1, num + 1)
sumaTotal = 0

for i in valores:
    sumaTotal = i + sumaTotal
print('La suma total es: ' + str(sumaTotal))

#Ejercicio 5
#Contador de vocales: Escribe un programa que cuente el número de vocales (a, e, i, o, u) en una cadena de texto ingresada por el usuario.

solicitarVocal = input('Ingrese una paralabra u oración: ')
valores = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
cantidad = 0

for i in solicitarVocal:
    if i in valores:
        cantidad = cantidad + 1
print('La cantidad de vocales escritas es de:', cantidad)

#Ejercicio 6
#Números primos: Escribe un programa que verifique si un número ingresado por el
# usuario es primo o no. Un número primo es aquel que solo es divisible por 1 y
# por sí mismo.

num = int(input("Ingrese un número: "))
esPrimo = True

for i in range(2, num):
    if num % i == 0:
        esPrimo = False
        break

if esPrimo:
    print("El número es primo")
else:
    print("El número no es primo")

#Ejercicio 7:
#Tabla de multiplicar: Escribe un programa que genere la tabla de multiplicar de un número ingresado por el usuario. 
# La tabla debe mostrar los resultados desde el 1 hasta el 10.

num = int(input('Ingrese un número: '))
resultado = 0

for i in range(1, 11):
    resultado = num * i
    print(num, ' x ', i, ' = ', resultado)

#Ejercicio 8:
#Números pares e impares: Escribe un programa que recorra una lista de números e
#imprima los números pares y los números impares por separado.

num = int(input('Ingrese un número: '))

print('Los números impares del N° ingresado son:')
for i in range(1, num + 1, 2):
    print(i)

print('Los números pares del N° ingresado son:')
for i in range(0, num + 1, 2):
    print(i)

#Solución 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números impares:", impares)

#Ejercicio 9
#Contador de caracteres: Escribe un programa que cuente la cantidad de veces que aparece cada carácter en una cadena de texto ingresada por el usuario.

cadena = input("Ingrese una cadena de texto: ")
contador = {}

for caracter in cadena:
    if caracter in contador:
        contador[caracter] += 1
    else:
        contador[caracter] = 1

for caracter, cantidad in contador.items():
    print(caracter, ":", cantidad)

#Ejercicio 10
#Suma de elementos en una lista: Escribe un programa que sume todos los elementos de una lista de números ingresada por el usuario.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
lista = [num1, num2, num3]
sum = 0

for i in lista:
    sum = sum + i
print('La suma de los números que ingresaste es: ', sum )

#Ejercicio 11
#Contador de palabras: Escribe un programa que cuente la cantidad de palabras en una oración ingresada por el usuario. Puedes asumir que las palabras están separadas por espacios.

cadena = input("Ingrese una cadena de texto: ")
lista = cadena.split()
contador = 0

for i in lista:
    contador += 1

print('Usted ha ingresado: ', contador, ' palabras.')



import array

mi_array = array.array('i', [1, 2, 3, 4, 5])

for i in mi_array:
    print(i)

#Arrays
import array

mi_array = array.array('i', [1, 2, 3, 4, 5])

#Ejemplos de arrays

import array

mi_array = array.array('i', [1, 2, 3, 4, 5])

# Acceder a un elemento
print(mi_array[3])  # Imprime: 4

# Modificar un elemento
mi_array[2] = 10

# Agregar un elemento al final
mi_array.append(6)

# Eliminar un elemento
del mi_array[1]

# Obtener la longitud del array
print(len(mi_array))  # Imprime: 5



#lista = ['cinco','seis','siete']
lista =  range(1, 11)
for i in lista:
    agregar = 'El número ' + str(i)
    print(agregar)

salirChat = True

while salirChat == True:
    texto = input('>')
        
    if texto == 'Exit' or texto == 'exit':
        salirChat = False
    print(texto)



















#for
num = range(1, 11)
for i in num:
    print(i)

estadoChat = True
while estadoChat == True:
    texto = input('>')
    if texto == 'exit':
        estadoChat = False
    texto = texto.replace(':)', '😀')
    texto = texto.replace(';)', '😉')
    texto = texto.replace(':p', '😋')
    texto = texto.replace(':P', '😋')
    texto = texto.replace(':()', '🙁')
    print(texto)

'''
#While
num = 0
while num < 3:
    num += 1
    if num == 2:
        continue
    print('El valor de la variable num es de: ' + str(num)) 
print('Fin del programa')

#while 2
n = 5
sum = 0
i = 1
while i <= n:
    sum = sum + i
    print('El valor de la suma para esta secuencia es de: '+ str(sum))
    i += 1
print('Fin del programa')

#Debugging

print('Esto es una prueba de debug')

def debug():
    a = 20
    print('Hola')
    print('Chau')
    a = 25
    return a

valorFinal = debug()
print(debug())

print('Hola mundo!')

5 > 4

15 < 10

#Ejemplo de AND
EDAD = 25
EDAD >= 18 and EDAD <= 70

#Ejemplo de NOT
EDAD = 25
if not ((EDAD < 18) or (EDAD >=70)):
    print('El resultado será verdadero. El operador NOT dará el resultado opuesto de la operación')

#Ejemplo de función
def montaniaRusa(edad):
    #edad=int(input('Ingrese su edad: '))
    if edad < 12:
        print('Permiso denegado')
    if edad > 12:
        print('Permiso aceptado')
montaniaRusa(10)

#descuento
def mostrarPrecioFinal(producto, precio, descuento):
    precioFinal = precio - descuento * precio / 100
    print('El precio sobre ' + producto + ' es: $ ' + str(precioFinal))
mostrarPrecioFinal('Remera', 40, 10)
mostrarPrecioFinal('Campera', 120, 30)

#IMC: Calcular el índice de masa corporal

def imc(peso, alturaCm):
    alturaMetros = alturaCm / 100
    resultadoIMC = peso / (alturaMetros * alturaMetros)
    print('El resultado del IMC es: ' + str(resultadoIMC))

    if resultadoIMC < 20:
        print('Estado de delgadez.')
    if resultadoIMC >= 20 and resultadoIMC < 26:
        print('Estado normal.')
    if resultadoIMC >= 26 and resultadoIMC < 30:
        print('Estado de sobrepeso.')
    if resultadoIMC >= 30:
        print('Estado de obesidad.')
imc(60, 162)

#IMC: Calcular el índice de masa corporal
def calcularIMC(peso, alturaCm):
    alturaMetros = alturaCm / 100
    resultadoIMC = peso / (alturaMetros * alturaMetros)
    print('El resultado del IMC es: ' + str(resultadoIMC))

    if resultadoIMC < 20:
        print('Estado de delgadez.')
    if resultadoIMC >= 20 and resultadoIMC < 26:
        print('Estado normal.')
    if resultadoIMC >= 26 and resultadoIMC < 30:
        print('Estado de sobrepeso.')
    if resultadoIMC >= 30:
        print('Estado de obesidad.')

#Solicitar datos para calcular IMC
def pedirIMC():
    peso = float(input('Ingrese su peso corporal en kg: '))
    alturaCm = int(input('Ingrese su altura en CM: '))
    calcularIMC(peso, alturaCm)

pedirIMC()



#Debugging

print('Esto es una prueba de debug')

def debug():
    a = 20
    print('Hola')
    print('Chau')
    a = 25
    return a

valorFinal = debug()
print(debug())

'''
