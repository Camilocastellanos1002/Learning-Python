
#funcion que calcula el interes simple y su valor final
def interesSimple(capital, tasa_in,tiempo):
    
    list=[] #se crea una lista en vacio

    interes_simple=capital*tasa_in*tiempo #se calcula el interes simple

    list.append(interes_simple) #se agrega el interes simple a la lista

    valor_final=capital*(1+tasa_in*tiempo)  #se calcula el valor final de la inversion

    list.append(valor_final) #se agrega el valor final a la lista

    return list #se retorna una lista con dos valores (interes y valor final)


#funcion principal
def main():

    #A continuacion se le pide al usuario ingresar los datos para realizar las operaciones
    capital=int(input("Ingrese la capital o monto inicial: "))
    tasa_in=float(input("Ingrese la tasa de interes: "))
    tiempo=int(input("Ingrese el tiempo de la inversion en años: "))

    #se captura los valores que retorna la funcion interesSimple en una lista
    list=interesSimple(capital,tasa_in,tiempo)
    #se imprese los valores en pantalla
    print(f'''\nInversion: {capital},tasa: {tasa_in},tiempo: {tiempo} años\nInteres simple: {int(list[0])}\nValor final: {int(list[1])}''')


#condicion para que el programa ejecute el main ya sea con run o por la terminal
if __name__== "__main__":
    main()

