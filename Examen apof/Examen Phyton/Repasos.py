#Repaso1 ) ejecutar y entender el siguiente programa:

numero1 = int(input('Dime un numero del 1 al 10'))
numero2 = int(input('Dime otro numero del 1 al 10'))

calcula = numero1 * numero2

cadenaCalcula = str (calcula)

print('El resulado es ')
print (cadenaCalcula)

#Repaso2 ) Realizar el siguiente programa:

dolares = int(input('Conversor de dolares a euros '))
euros = 0.9
calcula = dolares * euros

cadenaCalcula = str (calcula)

print('El resultado es ')
print (cadenaCalcula)

#Repaso 3) DEBUG, depurar y reparar paso a paso el siguiente programa :

numero1 = int(input('Dime un numero del 1 al 10 '))
numero2 = int(input('Dime otro numero del 1 al 10 '))

if numero1
**"<"** numero2:
resultado = 'el segundo'
else:
    resultado = 'el primero'

print ('El mayor es ' +str(resultado))

#Repaso 4) Depurar (con puntos de interrupción) para corregir y ejecutar :

nota1 = float(input('Escribe la primera nota '))
nota2 = float(input('Escribe la segunda nota '))
nota3 = float(input('Escribe la tercera nota '))

media = (nota1 + nota2 + nota3)/3

if media **"<"** 5:
    resultat = "Suspendido"
else:
    resultat = "Aprobado"

print ('La nota final es ' + str(resultat))

#Repaso 5) Realizar el siguiente programa:

print("COMPARADOR DE NÚMEROS")
numero1 = int(input("Escriba un número: "))
numero2 = int(input("Escriba otro número: "))

if numero1 > numero2:
    print('El mayor es el primero: ' + str(numero1))
elif **numero1** < **numero2**:
    print('El mayor es el segundo: ' + str(numero2))
else:
    print("Los dos números son iguales")

#Repaso 6) Ejecuta el siguiente programa

Programa condicion multiple
marca = input ("Escribe la marca del coche")
modelo = input ("Escribe modelo del coche")

precio = 10000

if marca == "ford" or marca =="Ford" or marca == "FORD":
    descuento = 10;

if marca == "opel" or marca =="Opel" or marca == "OPEL":
    descuento = 20;

precio = precio - (precio * (descuento/100))
print (' El precio final es ' + str(precio) + '€')

#Repaso 7) ¿Qué función tiene el siguiente programa?.

Hace que si elegimos el 1 y el 4 volvera a preguntar, por lo cual hace un bucle, pero si pones el 2 o el 3 no se repite

#Repaso 8) Realizar un programa para una tienda de informática

#El usuario introduce la marca y el modelo de la tarjeta gráfica y el programa saca el descuento correspondiente por pantalla
marca = input ("Escribe el nombre de la marca")
modelo = input ("Â¿Es GTX?")
IT = input ("Â¿Es IT?")
descuento= 0

if marca == "MSI" or marca =="msi" or marca == "Msi":
    descuento = 5;

if modelo == "SI" or modelo =="si" or modelo == "Si":
    descuento = descuento + 5;

if IT == "Si" or IT =="si" or IT == "SI":
    descuento = descuento + 10;
print (' El descuento es ' + str(descuento))

#Repaso 9) Ejecutar el siguiente programa

#Programa condicion multiple
marca = input ("Escribe la marca del coche")
modelo = input ("Escribe modelo del coche")

precio = 10000

if marca == "ford" or marca =="Ford" or marca == "FORD":    if modelo == "fiesta":
        descuento = 8;
    elif modelo == "focus":
        descuento = 15;
    else:
        descuento = 0;


if marca == "opel" or marca =="Opel" or marca == "OPEL":
    if modelo == "corsa":
        descuento = 50;
    elif modelo == "astra":
        descuento = 15;
    else:
        descuento = 0

precio = precio - (precio * (descuento/100))

print (' El precio final es ' + str(precio) + '€')

#Repaso 10) Ejecutar el siguiente programa y hacer seguimiento con puntos de interrupción:

print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")

#Repaso 11) En base al siguiente código, realizar programa que pide al usuario cuantas veces quiere que aparezca el saludo y también su nombre. El programa saca en pantalla el saludo "Hola nombre" ese número de veces.

numero = int(input('Dime cuantas veces quieres que ser repita'))
print("Comienzo")
for i in range(numero):
    print("Hola ", end="")

#Repaso 12) Modificar siguiente programa para que cuente números impares menores que 50.

cuenta = 0
for i in range(1, 50):
    if i % 2 == 1:
        cuenta = cuenta + 1

print("Hay " + str(cuenta) +" numeros impares")

#Repaso 13) Ejecutar y hacer seguimiento variables con punto interrupción para entender como funciona:

suma = 0
for i in [1, 2, 3, 4]:
    suma = suma + i
print("La suma de los números de 1 a 4 es " + str (suma))

#Repaso 14) Realizar programa que da como resultado la SUMA,de todos los números pares del 1 al 20.

cuenta = 0
suma = 0
for i in range(1, 10):
    if (i % 2) == 1:
        cuenta = cuenta + 1
        suma = suma + i

print ("Hay" + str(cuenta) +"numeros impares")
print("la suma es " + str(suma))

#Repaso 15) En base al siguiente programa, realizar programa que muestre tabla de multiplicar del 5:

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
   print(5 * (i))

#Repaso 16) En base al siguiente código: realizar programa donde usuario introduce una palabra y el ordenador cuenta cuantas vocales "a" hay en dicha palabra.

palabra = input("Escribe una palabra")
contador = 0

for letter in palabra:
    if letter == "a" or letter== "A":
        contador = contador +1
        print(str(contador))

##Funciones

#Repaso 1) Ejecutar el siguiente programa:

def subrutina():
    a = 2
    print("El valor en subrutina es: " + str(a))
    return


subrutina()
a= 5
print("En programa el valor es: " + str(a))

#Repaso 2) Ejecutar el siguiente programa. ¿La variable 'a' es local o global? "Reperar" el programa para que el resultado sea correcto

##Respuesta
La a dentro de "def" es local mientras que la a de fuera de "def" es global

##Programa
def subrutina():
    print(a)
    a = 2
    print(a)
    return

a = 5
subrutina()
print(a)

##Reparado

def subrutina():
    a = 2
    print(a)
    return

a = 5
subrutina()
print(a)

#Repaso 3) Ejecutar el siguiente programa

def saludar(nombre, mensaje=' Hola '):
    print (mensaje + nombre)

usuario = input ("Introduce nombre")
saludar(usuario)

#Repaso 4) Crear un programa con dos funciones. En el programa principal el usuario introduce su nombre y edad. En una función llamada 'Saludo' , aparece en pantalla "Buenos dias, nombre" y en la otra función aparece en pantalla "Pareces más joven que x años".

def saludar(nombre, mensaje=' Hola '):
    print (mensaje + nombre)

usuario = input ("Introduce nombre")
saludar(usuario)

def msgedad(edad, msg=' Pareces más joven que una persona de '):
    print (msg + edad)

edad = input ("Introduce tu edad")
msgedad(edad)

#Repaso 5) Ejecutar el siguiente programa. ¿Qué diferencias hay con el anterior?

def calcula_media(x, y):
    resultado = (x + y) / 2
    return resultado

a = 3
b = 5
media = calcula_media(a, b)
print("Media de " + str(a) + " y " + str(b) + " es: " +str(media))
print("Programa terminado")

##Respuesta
Este programa tiene 2 numeros de base ya seleccionados, por lo tanto, este programa no pide al usuario dos números a diferencia del anterior

#Repaso 6) Realizar programa "Calculadora". El usuario introduce 2 numeros por teclado y en el programa hay 5 funciones: suma, resta, división, multiplicación y módulo de ambos números.

def calculadora():
    operacion= input("Que operacion quieres")
    a = float(input("Escribe un número"))
    b = float(input("Escribe otro número"))
    sum = a+b
    rest = a-b
    multi = a*b
    div = a/b
    residuo = a/b%2
    if operacion == "suma" or operacion=="Suma" or operacion == "SUMA":
        print ("El resultado es "+str(sum))
    if operacion == "resta" or operacion=="Resta" or operacion == "RESTA":
        print ("El resultado es "+str(rest))
    if operacion == "multiplicacion" or operacion=="Multiplicacion" or operacion == "MULTIPLICACION":
        print ("El resultado es "+str(multi))
    if operacion == "division" or operacion=="Division" or operacion == "DIVISiON":
        print ("El resultado es "+str(div))
    if operacion == "residuo" or operacion=="Residuo" or operacion == "RESIDUO":
        print ("El resultado es "+str(residuo))
    return
calculadora()