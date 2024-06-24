import random
contador_wins_user=0
contador_wins_pc=0
contador_rondas=0


def lanzar_dado():
    dado=random.randint(1,6)
    return dado

def lanzamiento_computadora(lanzar_dado):
    dado_pc=lanzar_dado()
    return dado_pc

def comparacion(dado1,dado2,saldo_user,saldo_pc,saldo_apuesta_user,saldo_apuesta_pc):
    if dado1>dado2:
        print("el dado del usuario es mayor")
        print("Ganaste la apuesta")
        saldo_user=saldo_user+saldo_apuesta_user+saldo_apuesta_pc
        
    elif dado2 > dado1:
        print("el dado de la computadora es mayor")
        print("La Computadora gano la apuesta")
        saldo_pc=saldo_pc+saldo_apuesta_pc+saldo_apuesta_user
    
    else:
        saldo_user=saldo_user+saldo_apuesta_user
        saldo_pc=saldo_pc+saldo_apuesta_pc
    
    return saldo_user,saldo_pc


def ronda(dado1,dado2):
    global contador_wins_user
    global contador_wins_pc
    global contador_rondas
    
    contador_rondas=contador_rondas+1
    
    if dado1 > dado2:
        contador_wins_user=contador_wins_user+1
    elif dado2 > dado1:
        contador_wins_pc=contador_wins_pc+1
    
      
    return contador_wins_user,contador_wins_pc,contador_rondas


def saldo(saldo_user,saldo_pc,dado1,dado2):
    flag1=False
    flag2=False
    
    print(f"\nSaldo Usuario: {saldo_user}\nSaldo Computadora: {saldo_pc}\n")
    saldo_apuesta_user=int(input(f"Ingrese el saldo que desea apostar: "))
    saldo_apuesta_pc=random.randint(1,100)
    print(f"Saldo apostado de la computadora: {saldo_apuesta_pc}")
    
    if saldo_apuesta_user > 0 and saldo_apuesta_user <= 100:
        saldo_user= saldo_user - saldo_apuesta_user
        dado1=lanzar_dado()
        flag1=True
    else:
        flag1=False
    
    if saldo_apuesta_pc > 0 and saldo_apuesta_pc <= 100:
        saldo_pc= saldo_pc - saldo_apuesta_pc
        dado2=lanzamiento_computadora(lanzar_dado)
        flag2=True
    else:
        flag2=False
        
    print(f"\ndado usuario: {dado1}, dado computadora: {dado2}\n")
    saldo_user,saldo_pc=comparacion(dado1,dado2,saldo_user,saldo_pc,saldo_apuesta_user,saldo_apuesta_pc)
    ronda(dado1,dado2)

    return saldo_user,saldo_pc,dado1,dado2,flag1,flag2
        
    
    
def  main():
    saldo_user=100
    saldo_pc=100
    ganador=-1
    dado1=0
    dado2=0
    
    while saldo_user>0 or saldo_pc>0 or ganador!=0:
        print(f'''\nRonda #{contador_rondas+1}:''')
        saldo_user,saldo_pc,dado1,dado2,flag1,flag2=saldo(saldo_user,saldo_pc,dado1,dado2)
        
        if saldo_user == 0 or saldo_user < 0:
            saldo_user=0
            print("No tienes saldo para apostar!")
            break
            
        if saldo_pc == 0 or saldo_pc <= 0:
            saldo_pc=0
            print("La computadora no tiene saldo para apostar!")
            break
        
        if flag1 == False:
            break
        elif flag2 == False:
            break
        
        print(f'''Usuario: {contador_wins_user} vs Computadora: {contador_wins_pc}''')
        if contador_wins_user== 3:
            print(f"\nEl usuario es el ganador {contador_wins_user} vs {contador_wins_pc}")
            break
        elif contador_wins_pc ==3:
            print(f"\nla computadora es la ganadora {contador_wins_pc} vs {contador_wins_user}")
            break
        
    print(f'''Saldo usuario: {saldo_user}\nSaldo computadora: {saldo_pc}''')

if __name__ == "__main__":
    main()