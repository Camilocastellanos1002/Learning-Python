option=-1
trainers=[3]

def coder_create():

    group_A=[] 
    group_A_age=[] 
    group_A_moth=[] 
    group_B=[] 
    group_B_age=[] 
    group_B_moth=[] 
    group_C=[] 
    group_C_age=[] 
    group_C_moth=[]
    absences_days_A=[]
    absences_days_B=[]
    absences_days_C=[]

    name=input("ingrese el nombre del coder: ")
    moth=int(input('''Ingrese el mes de ingreso del coder:
    ingrese numeros del 1 al 12 que representan el mes respectivamente          
    '''))
    group=input("ingrese el grupo del coder: ")
    group.upper()
    age=int(input("ingrese la edad del coder: "))
    abs=int(input('''Ingrese la cantidad de inasistencias del coder: 
    '''))

    if group == "A":
        group_A.append(name)
        group_A_age.append(age)
        group_A_moth.append(moth)
        absences_days_A.append(abs)
    elif group == "B":
        group_B.append(name)
        group_B_age.append(age)
        group_B_moth.append(moth)
        absences_days_B.append(abs)
    elif group == "C":
        group_C.append(name)
        group_C_age.append(age)
        group_C_moth.append(moth)
        absences_days_C.append(abs)
    else:
        print("ingresaste dato erroneo")

    print("Coder ingresado satisfactoriamente")

    return group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C


def trainer_group():
    global trainers

    group=input("Ingrese el grupo donde desea registrar el trainer: ")
    name_trainer=input("Ingrese el nombre del trainer del grupo: ")
    if group == "A":
        trainers.insert(0,name_trainer)
    elif group == "B":
        trainers.insert(1,name_trainer)
    elif group == "C":
        trainers.insert(2,name_trainer)
    else:
        print("ingresaste dato erroneo")


def search():
    group1=input("Ingrese el primer grupo donde desea buscar coder: ")
    group2=input("Ingrese el primer grupo donde desea buscar coder: ")
    group1.upper()
    group2.upper()
    name=input("Ingrese el nombre del coder que desea buscar en los grupos: ")
    if group1 == "A":
        if group2 == "B":
            total=int(group1.count(name) + group2.count(name))
        elif group2 == "C":
            total=int(group1.count(name) + group2.count(name))
    elif group1 == "B":
        if group2 == "A":
            total=int(group1.count(name) + group2.count(name))
        elif group2 == "C":
            total=int(group1.count(name) + group2.count(name))
    elif group1 == "C":
        if group2 == "A":
            total=int(group1.count(name) + group2.count(name))
        elif group2 == "B":
            total=int(group1.count(name) + group2.count(name))
    else:
        print("ingresaste dato erroneo")
    return name,total


def absences(group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C):
    top=int(input("ingrese el maximo numero de inasistencias que puede tener un estudiante: "))

    maxA=max(absences_days_A)
    maxB=max(absences_days_B)
    maxC=max(absences_days_C)


    if maxA >= top:
        #al encontrar la posicion del nombre del coder quien tenga mas inasistencia, se tiene la posicion de su edad, mes de ingreso para eliminar el coder del sistema
        position=group_A.index(maxA)

        del group_A[position]
        del group_A_age[position]
        del group_A_moth[position]
        del absences_days_A[position]
        print("Estudiante eliminado exitosamente!")
    
    elif maxB >= top:
        position=group_B.index(maxA)

        del group_B[position]
        del group_B_age[position]
        del group_B_moth[position]
        del absences_days_B[position]
        print("Estudiante eliminado exitosamente!")

    elif maxC >= top:
        position=group_C.index(maxA)

        del group_C[position]
        del group_C_age[position]
        del group_C_moth[position]
        del absences_days_C[position]
        print("Estudiante eliminado exitosamente!")
    return group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C

def show(group_A,group_B,group_C):
    global trainers
    print(f'''Grupo A:
        trainer: {trainers[0]}
        Estudiantes: {group_A}''')
    print(f'''Grupo B:
        trainer: {trainers[1]}
        Estudiantes: {group_B}''')
    print(f'''Grupo C:
        trainer: {trainers[2]}
        Estudiantes: {group_C}''')


def old_or_young(group_A,group_B,group_C,group_A_age,group_B_age,group_C_age):
    oldA=max(group_A_age)
    oldB=max(group_B_age)
    oldC=max(group_C_age)
    youngA=min(group_A_age)
    youngB=min(group_B_age)
    youngC=min(group_C_age)
    
    position1=group_A.index(oldA)
    print(f"la persona con mayor edad del grupo A es: {group_A[position1]}")
    position2=group_A.index(youngA)
    print(f"la persona con mayor edad del grupo A es: {group_A[position2]}")
    position1=group_B.index(oldB)
    print(f"la persona con mayor edad del grupo A es: {group_B[position1]}")
    position2=group_B.index(youngB)
    print(f"la persona con mayor edad del grupo A es: {group_B[position2]}")
    position1=group_C.index(oldC)
    print(f"la persona con mayor edad del grupo A es: {group_C[position1]}")
    position2=group_C.index(youngC)
    print(f"la persona con mayor edad del grupo A es: {group_C[position2]}")

def traslate(group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C):
    group1=input("Ingrese el grupo del coder que desea trasladar: ")
    group1.upper()
    group2=input("Ingrese el grupo que desea trasladarlo: ")
    group2.upper()
    name=input("Ingrese el nombre del coder que desea buscar en los grupos: ")
    if group1 == "A" and group2 =="B":

        position=group_A.index(name)
        group_B.append(group_A[position])
        group_B_age.append(group_A_age[position])
        group_B_moth.append(group_A_moth[position])
        absences_days_B.append(absences_days_A[position])

        del group_A[position]
        del group_A_age[position]
        del group_A_moth[position]
        del absences_days_A[position]
    
        print("Estudiante trasladado exitosamente!")
        
    elif group1 == "A" and group2 =="C":

        position=group_A.index(name)
        group_C.append(group_A[position])
        group_C_age.append(group_A_age[position])
        group_C_moth.append(group_A_moth[position])
        absences_days_C.append(absences_days_A[position])

        del group_A[position]
        del group_A_age[position]
        del group_A_moth[position]
        del absences_days_A[position]

        print("Estudiante trasladado exitosamente!")
        
    elif group1 == "B" and group2 =="A":

        position=group_B.index(name)
        group_A.append(group_B[position])
        group_A_age.append(group_B_age[position])
        group_A_moth.append(group_B_moth[position])
        absences_days_A.append(absences_days_B[position])

        del group_B[position]
        del group_B_age[position]
        del group_B_moth[position]
        del absences_days_B[position]

        print("Estudiante trasladado exitosamente!")
        
    elif group1 == "B" and group2 =="C":

        position=group_B.index(name)
        group_C.append(group_B[position])
        group_C_age.append(group_B_age[position])
        group_C_moth.append(group_B_moth[position])
        absences_days_C.append(absences_days_B[position])

        del group_B[position]
        del group_B_age[position]
        del group_B_moth[position]
        del absences_days_B[position]

        print("Estudiante trasladado exitosamente!")
    
    elif group1 == "C" and group2 =="A":

        position=group_C.index(name)
        group_A.append(group_C[position])
        group_A_age.append(group_C_age[position])
        group_A_moth.append(group_C_moth[position])
        absences_days_A.append(absences_days_C[position])

        del group_C[position]
        del group_C_age[position]
        del group_C_moth[position]
        del absences_days_C[position]

        print("Estudiante trasladado exitosamente!")

    elif group1 == "C" and group2 =="B":
        
        position=group_C.index(name)
        group_A.append(group_C[position])
        group_A_age.append(group_C_age[position])
        group_A_moth.append(group_C_moth[position])
        absences_days_A.append(absences_days_C[position])

        del group_C[position]
        del group_C_age[position]
        del group_C_moth[position]
        del absences_days_C[position]

        print("Estudiante trasladado exitosamente!")
    else:
        print("Se ingreso datos erroneos!")
    return group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C
    
    
while option != 0:
    option=input('''Menu
                Ingrese la opcion deseada: 
                 1.crear nuevo coder
                 2.Registrar Trainer del grupo
                 3.Buscar coders duplicados en 2 grupos
                 4.Eliminar coders por inasistencia
                 5.Ver lista de estudiantes de cada grupo
                 6.Trasladar coder de un grupo a otro grupo
                 7.Reportar mayor y menor edad de cada grupo
                 0.salir
                 Opcion :
    ''')
    if option == 1: 
        group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C=coder_create()
    '''elif option == 2: 
        trainer_group()
    elif option == 3: 
        name,totalsearch=search()
        print(f"{name} se encuentra {totalsearch} veces en los grupos")
    elif option == 4: 
        group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C=absences(group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C)
    elif option == 5: 
        show(group_A,group_B,group_C)
    elif option == 6: 
        group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C =traslate(group_A,group_A_age,group_A_moth,group_B,group_B_age,group_B_moth,group_C,group_C_age,group_C_moth,absences_days_A,absences_days_B,absences_days_C)
    elif option == 7: 
        old_or_young(group_A_age,group_B_age,group_C_age)'''