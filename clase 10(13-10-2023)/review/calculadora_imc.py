def main():
    print('''Queremos ayudarte a cuidarte!\n''')
    kg=int(input("Ingrese su peso (en kg): "))
    height=float(input("Ingrese su altura (en m): "))
    imc=kg/height
    if imc < 18.5:
        print("Estas por debajo de tu peso ideal")
    elif imc >= 18.5 and imc <= 24.9:
        print("Estas en tu peso de rango ideal")
    elif imc >= 25 and imc <= 29.9:
        print("Ojo, tienes sobrepeso")
    elif imc >30 and imc <=34.9:
        print("Tienes obesidad\nGrado 1")
    elif imc > 35 and imc <= 39.9:
        print("Tienes obesidad\nGrado 2!")
    elif imc > 3:
        print("Tienes obesidad grado 3")