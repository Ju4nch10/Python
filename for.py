contador = {
    "o":"4", 
    "h":"2"
    }


for caracter, cantidad in contador.items():
    print(caracter, ":", cantidad)

num = int(input('Ingrese un número: '))
resultado = 0

for i in range(1, 11):
    resultado = num * i
    print(num, ' x ', i, ' = ', resultado)

# test