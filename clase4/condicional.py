#condicional
number=int(input("ingrese un numero: "))

if number%2 == 0 and number < 10:
    print("el numero es par")
    print("y el numero es menor a 10")
elif number%2 ==0 and number >10:
    print("el numero es par y es mayor que 10")
elif number%3 == 0 and number < 10:
    print("el numero es impar y menor que 10")
else:
    print("el numero es impar y mayor de 10")