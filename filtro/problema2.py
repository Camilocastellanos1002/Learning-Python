#funcion que calcula el interes de los CDTs
def interes(capital, tiempo): #recibe dos parametros

    #a continuacion dependiendo del tiempo se calucla el interes

    if tiempo>=1 and tiempo <=2:
        tasa_int=7
        valor_CDT=capital*tasa_int*tiempo   #interes con el 7%
        valor_final=capital*(1+tasa_int*tiempo)
    elif tiempo>2 and tiempo<=5:
        tasa_int=10
        valor_CDT=capital*tasa_int*tiempo
        valor_final=capital*(1+tasa_int*tiempo) #interes con el 10%
    elif tiempo>5:
        tasa_int=15
        valor_CDT=capital*tasa_int*tiempo
        valor_final=capital*(1+tasa_int*tiempo) #interes con el 15%
    
    return valor_CDT,valor_final    #se retorna el interes y el valor final

#funcion principal
def main():
    #variables
    capital=-1
    usuario=[]
    #se ingresa el nombre del usuario 
    usuario.append(input("Ingrese su nombre: "))
    #contador de cantidad de CDTs que tiene el usuario
    cantidad_CDT=0

    while capital!=0:

    
        cantidad_CDT+=1
        #se generan dos listas que tendran el interes de cada CDT y el valor final del CDT respectivamente
        interes_CDT=[]
        capital_CDT=[]
     
        #ingreso de datos del usuario por terminal
        capital=int(input(f"Ingrese el monto inicial del CDT #{cantidad_CDT}: "))
        tiempo=int(input("Ingrese el tiempo de inversion en años: "))

        #se llama a la funcion interes para realizar operaciones
        valor_CDT,valor_final=interes(capital,tiempo)   #retorna 2 valores

       

        #si el usuario ingresa el monto 0, se termina la operacion
        if capital==0:
            break
        elif capital <0: #si el usuario ingresa un valor menor a cero, imprime mensaje de error
            print("ingreso datos erroneos")
            continue #si se ingresa datos erroneos se obliga a ejecutar la siguiente iteracion

        #el usuario debe ingresar un tiempo mayor a cero para realizar operaciones, en caso contrario mensaje de error
        if tiempo<=0:
            print("ingreso datos erroneos")
            continue #si se ingresa datos erroneos se obliga a ejecutar la siguiente iteracion


        #se ingresa los intereses y el valor final de cada CDT en las listas respectivamente
        interes_CDT.append(valor_CDT)
        capital_CDT.append(valor_final)

        interes_ganado=sum(interes_CDT) #se calcula el total del interes ganado en todos los CDTs del usuario
        capital_total=sum(capital_CDT)  #se calcula la capital total del usuario



    print(f'''Capital total de todos los CDT: {capital_total}, cuyos total de interes ganados fueron: {interes_ganado}''') #se imprime el interes total de los CDTs y el capital total del usuario


#condicion para que el programa ejecute el main ya sea con run o por la terminal
if __name__== "__main__":
    main()



