#Ganador de medalla de oro de salto triple

numbers_athletes=int(input("ingrese la cantidad de atletas que van a competir: "))
record=0
for i in range(numbers_athletes):
    name=input(f"ingrese el nombre del atleta #{i+1}: ")
    score=float(input(f"""ingrese el resultado del salto triple en metros (m) del atleta {name}: """))
    
    if score > record:
        record=score
        winner=name
    
print(f"La medalla de oro es para {winner}")

if record > 15.50:
    print(f"Rompiste record {winner} con {record} (m), eres el ganador de 500 millones de pesos")
 
