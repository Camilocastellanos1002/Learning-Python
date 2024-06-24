import random

def lanzar_dado():
    dado=random.randint(1,6)
    return dado

def lanzamiento_computadora(lanzar_dado):
    dado_pc=lanzar_dado()
    return dado_pc

def comparacion(dado,dadopc):
    
    contador_win_usuario=0
    contador_win_computadora=0
    if dado > dadopc:
        print("el ganador es el usuario")
        contador_win_usuario=contador_win_usuario+1
    elif dado < dadopc:
        print("el ganador es la computadora")
        contador_win_computadora=contador_win_computadora+1
    return contador_win_usuario, contador_win_computadora

def jugar_turno():
    saldo_usuario=100
    saldo_pc=100
    
    valor_apuesta=int(input("ingresar el monto de apuesta:\nel valor debe ser multimo de 10\nvalor: "))
    valor=int(valor_apuesta%10)

    if valor == 0:
        
        saldo_usuario=saldo_usuario-valor_apuesta  
        
        if saldo_usuario< 0:
            print("No puedes jugar, no tienes saldo")
        elif saldo_usuario >0:
            dado=lanzar_dado()
            print(f"cara de dado: {dado}")
            
             
    elif valor!=0:
        
        valor_apuesta=valor_apuesta-valor
        saldo_usuario=saldo_usuario-valor_apuesta 
        
        if saldo_usuario< 0:
            print("No puedes jugar, no tienes saldo")
        elif saldo_usuario >0:
            dado=lanzar_dado()
            print(f"cara de dado: {dado}")

    
    #computadora
    valor_apuesta_pc=random.randint(1,100)
    valor2=valor_apuesta_pc%10
    if valor2 == 0:
        
        print(f"valor apuesta del pc: {valor_apuesta_pc}")
        saldo_pc=saldo_usuario-valor_apuesta_pc 
        
        if saldo_pc< 0:
            print("No puedes jugar, no tienes saldo")
        elif saldo_pc >0:
            
            dadopc=lanzamiento_computadora(lanzar_dado)
            print(f"cara de dado de la computadora: {dadopc}") 
                
    elif valor2!=0:
        
        valor_apuesta_pc=valor_apuesta_pc-valor
        print(f"valor apuesta del pc: {valor_apuesta_pc}")
        saldo_pc=saldo_pc-valor_apuesta_pc 
        
        if saldo_pc< 0:
            print("No puedes jugar, no tienes saldo")
        elif saldo_pc >0:
            dadopc=lanzamiento_computadora(lanzar_dado)
            print(f"cara de dado de la computadora: {dadopc}") 
            
    return dado,dadopc

def main():
    
    ganador=0
    while ganador !=1:
        print("\nInicio del juego\n")
        dado,dadopc=jugar_turno()
        win_user,win_pc=comparacion(dado,dadopc)
        if win_user == 3:
            print("ganador del juego es el usuario")
            ganador = 1
        elif win_pc == 3:
            print("ganador del juego es la computadora")
            ganador =1


if __name__== "__main__": 
    main()
    
    
    
        
    