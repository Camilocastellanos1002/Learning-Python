import random #se importa la libreria random para generar numeros aleatorios

#funcion que define si el jugador adivino o no
def juego(name):
    #variables locales
    intentos=0
    flag=False #bandera para saber si gano o no, False: Perdio, True: Gano

    print(f"\nAdivina el numero secreto {name}\n")
    numero_secreto=random.randint(1,20) #se genera un numero secreto entre el 1 y el 20 de forma aleatoria para que el usuario intente adivinarlo

    while intentos!=3: #cada jugador solo cuenta con 3 intentos
        
        intentos+=1 #se cuenta los intentos

        print(f"Intento #{intentos}") #se imprime en que intento se encuetra
        numero=int(input(f'''\nIngresa un numero: ''')) #el usuario ingresa el numero
        
        diferencia=abs(numero_secreto-numero) #se calcula la diferencia entre el numero ingresado y el numero secreto con valor absoluto para luego comparar


        if diferencia == 0: #si la diferencia es cero, es que se adivino el numero secreto
            print(f"Felicitaciones, Adivinaste {name}") #se imprime un mensaje de felicitaciones personalizado
            flag=True   #bandera en verdadero para determinar que le jugador gano
            break
        elif diferencia>0 and diferencia <=3: #si la diferencia entre el numero ingresado y el numero secreto esta entre 1 y 3, el usuario esta caliente
            flag=False #el usuario no perdiendo
            print("Estas caliente") 

        elif diferencia>3 and diferencia <=5: #si la diferencia entre el numero ingresado y el numero secreto esta entre 4 y 5, el usuario esta tibio
            flag=False #el usuario no perdiendo
            print("Estas tibio")
            
        else: #si la diferencia es mayor a 5, el usuario se encuentra frio y muy lejos de adivinar el numero
            flag=False #el usuario no perdiendo
            print("Estas frio")
        


    #se retorna la cantidad de intentos del jugador y el estado si gano o perdio
    return intentos,flag

#funcion principal
def main():

    option=-1
    #se generan listas de nombres de jugadores y aquellos que ganaron en el 1er, 2do, 3er intento o perdieron
    jugadores=[]
    ganador_uno=[]
    ganador_dos=[]
    ganador_tres=[]
    perdedores=[]

    while option!=0:

        #se imprime un menu y se espera una opcion ingresada por la terminal para ingresar jugador o salirse del juego
        option=int(input("\nMenu de juego\n1.Ingresar nuevo jugador\n0.No Jugar màs\nOpcion: "))
        if option==1: #si ingresa 1, el juego inicia
            print("Bienvenido")
            name=input("Ingrese nombre del jugador: ") #ingresa nombre del jugador

            jugadores.append(name) #se ingresa el nombre del jugador a la lista
            intento,flag=juego(name)    #se llama a la funcion jeugo y se asigna los valores retornados

            porcen1=len(ganador_uno)/len(jugadores)*100
            porcen2=len(ganador_dos)/len(jugadores)*100
            porcen3=len(ganador_tres)/len(jugadores)*100
            porcen4=len(perdedores)/len(jugadores)*100

            porcen=100


            if intento ==1 and flag ==True: #si el jugador gano y gano en el primer intento
                ganador_uno.append(name)    #se asigna a la lista de los ganadores con un solo intento
            elif intento == 2 and flag ==True:  #con dicion si el juegador gano y gando con dos intentos
                ganador_dos.append(name) #se asigna a la lista de los ganadores con dos intentos
                
            elif intento == 3 and flag ==True: #si el jugador gano y gano en el tercer intento
                ganador_tres.append(name) #se asigna a la lista de los ganadores con tres intentos
            elif flag ==False:  #si el jugador perdio sin importar la cantidad de intentos
                perdedores.append(name) #se asigna a una lista de perdedores

        #si se ingresa 0 para no jugar mas, imprime los resultados y se sale del programa
        elif option == 0:
            print(f"Cantidad de jugadores: {len(jugadores)}")
            print(f"Ganadores con 1 intento: {porcen-porcen1}%") #genera la impresion de todos los jugadores ganadores con un intento
            print(f"Nombres: {ganador_uno}")
            print(f"Ganadores con 2 intento: {porcen-porcen1-porcen2}%") #genera la impresion de todos los jugadores ganadores con dos intentos
            print(f"Nombres: {ganador_dos}")
            print(f"Ganadores con 3 intento: {porcen-porcen1-porcen2-porcen3}%")
            print(f"Nombres: {ganador_tres}") #genera la impresion de todos los jugadores ganadores con tres intentos
            print(f"Perdedores: {100-porcen4}%")
            print(f"Nombres: {perdedores}")#genera la impresion de todos los jugadores que no adivinaron y perdieron el juego
            break
            
#condicion para que el programa ejecute el main ya sea con el boton run o por la terminal
if __name__== "__main__":
    main()
