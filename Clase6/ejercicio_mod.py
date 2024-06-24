#ejercicio de promedio

average_total=0
amount=int(input("ingrese la cantidad personas: "))
for i in range(amount):
    name=input(f"ingrese el nombre de la persona #{i+1}: ")
    income1=int(input("digita tu primer ingreso: "))
    income2=int(input("digita tu segundo ingreso: "))
    income3=int(input("digita tu tercero ingreso: "))
    income4=int(input("digita tu cuarto  ingreso: "))
    sum= income1+income2+income3+income4
    average=sum/4
    average_total=average_total+average

    print(name,"tu promedio de ingresos es: $", int(average))
    if sum < 5*10**5:
        print("tus ingresos son muy bajos, debes buscar trabajo")
    else:
        print("tus ingresos son altos, dona a un niño de bajo recursos")

print(f"el total de promedios de las {amount} personas es: {int(average_total)}")
