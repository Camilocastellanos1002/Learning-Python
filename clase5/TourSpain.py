#Vuelta a España
salary_leader=0
salary=int(input("Cual es el sueldo basico por kilometro: "))
athletes=int(input("ingrese la cantidad de atletas: "))
total=0
for i in range(athletes):
    name=input(f"ingrese el nombre del atleta #{i+1}: ")
    kilometers=int(input(f"ingrese la cantidad de kilometros recorridos del atleta {name}: "))
    if kilometers < 0 or kilometers <= 3277:
        leader=input("Utilizaste la camiseta lider, Solo Responde si ò no: ")
        if (leader == "si" or leader == "SI" or leader =="Si" or leader == "sI") and kilometers <3277:
            kilm_leader=int(input("ingresa la cantidad de kilometros recorridos como lider: "))
            
            if kilm_leader >= 1800:
                salary_leader=(kilm_leader-1800)*(salary*0.25)
        elif (leader == "si" or leader == "SI" or leader =="Si" or leader == "sI") and kilometers == 3277:
            print(f"{name} Ganaste la vuelta a España\nRecibiras el premio de 700 millones")
            continue
        else:
            salary_leader=0
        
        total=(salary*kilometers)+salary_leader
        print(f"el sueldo por kilometro del atleta {name} es: ${total}")             
    else:
        print("Ingresaste dato erroneo!")