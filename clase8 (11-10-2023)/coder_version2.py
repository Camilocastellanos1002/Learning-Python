trainers=[]
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

count_students=0
flag= True
total=0

def coder_create():
  
    global group_A
    global group_A_age
    global group_A_moth
    global group_B
    global group_B_age
    global group_B_moth
    global group_C 
    global group_C_age
    global group_C_moth
    global absences_days_A
    global absences_days_B
    global absences_days_C
    global count_students
    
    if flag==True:
        
        count_students=count_students+1
        
        group=input("ingrese el grupo del coder: ")
        group.upper()
    
        if group =="A" or group =="a":
            
            name=input("ingrese el nombre del coder: ")
            moth=int(input('''Ingrese el mes de ingreso del coder:\ningrese numeros del 1 al 12 que representan el mes respectivamente          
            '''))
            age=int(input("ingrese la edad del coder: "))
            abs=int(input('''Ingrese la cantidad de inasistencias del coder: 
            '''))

            group_A.append(name)
            group_A_age.append(age)
            group_A_moth.append(moth)
            absences_days_A.append(abs)
            
        elif group == "B" or group =="b":
            
            name=input("ingrese el nombre del coder: ")
            moth=int(input('''Ingrese el mes de ingreso del coder:\ningrese numeros del 1 al 12 que representan el mes respectivamente          
            '''))
            age=int(input("ingrese la edad del coder: "))
            abs=int(input('''Ingrese la cantidad de inasistencias del coder: 
            '''))
            
            group_B.append(name)
            group_B_age.append(age)
            group_B_moth.append(moth)
            absences_days_B.append(abs)
            
        elif group == "C" or group =="c":
            
            name=input("ingrese el nombre del coder: ")
            moth=int(input('''Ingrese el mes de ingreso del coder:\ningrese numeros del 1 al 12 que representan el mes respectivamente          
            '''))
            age=int(input("ingrese la edad del coder: "))
            abs=int(input('''Ingrese la cantidad de inasistencias del coder: 
            '''))
            
            group_C.append(name)
            group_C_age.append(age)
            group_C_moth.append(moth)
            absences_days_C.append(abs)
            
            
    print("Coder ingresado satisfactoriamente")

def trainer_group():
    global trainers

    group=input("Ingrese el grupo donde desea registrar el trainer: ")
    name_trainer=input("Ingrese el nombre del trainer del grupo: ")
    
    if group == "A" or group=="a":
        trainers.insert(0,name_trainer)
    
    elif group == "B" or group=="b":
        trainers.insert(1,name_trainer)
        
    elif group == "C" or group=="c":
        trainers.insert(2,name_trainer)
    
    if len(trainers)>3:
        trainers.pop()
        
    print("Trainer ingresado satisfactoriamente")

def search():
    global group_A
    global group_B
    global group_C
    
    name=input("Ingrese el nombre del coder que desea buscar en los grupos: ")
    group1=input("Ingrese el primer grupo donde desea buscar coder: ")
 
    
    if group1 == "A" or group1=="a":
        
        group2=input("Ingrese el segundo grupo donde desea buscar coder: ")
        
        if group2 == "B" or group1=="b":         
            print(f"\nEn el grupo  A y B {name} existe: {group_A.count(name) + group_B.count(name)} veces\n")
        elif group2 == "C" or group1=="c":
            print(f"\nEn el grupo  A y C {name} existe: {group_A.count(name) + group_C.count(name)} veces\n")
            
    elif group1 == "B" or group1=="b":
        
        group2=input("Ingrese el segundo grupo donde desea buscar coder: ")
        
        if group2 == "A" or group1=="a":
            print(f"\nEn el grupo  B y A {name} existe: {group_B.count(name) + group_A.count(name)} veces\n")
        elif group2 == "C" or group1=="c":
            print(f"\nEn el grupo  B y C {name} existe: {group_B.count(name) + group_C.count(name)} veces\n")
            
    elif group1 == "C" or group1=="c":
        group2=input("Ingrese el segundo grupo donde desea buscar coder: ")
     
        if group2 == "A" or group1=="a":
            print(f"\nEn el grupo  C y A {name} existe: {group_C.count(name) + group_A.count(name)} veces\n")
        elif group2 == "B" or group1=="b":
            print(f"\nEn el grupo  C y B {name} existe: {group_C.count(name) + group_B.count(name)} veces\n")
    else:
        print("Ingresaste dato erroneo")


def absences():
    global group_A
    global group_A_age
    global group_A_moth
    global group_B
    global group_B_age
    global group_B_moth
    global group_C 
    global group_C_age
    global group_C_moth
    global absences_days_A
    global absences_days_B
    global absences_days_C
    
    print(f"faltas del grupo A: {absences_days_A}")
    print(f"faltas del grupo A: {absences_days_B}")
    print(f"faltas del grupo A: {absences_days_C}")
    
    
    top=int(input("ingrese el maximo numero de inasistencias que puede tener un estudiante: "))

    if max(absences_days_A) >= top:
        position=absences_days_A.index(max(absences_days_A))

        del group_A[position]
        del group_A_age[position]
        del group_A_moth[position]
        del absences_days_A[position]
        print("Estudiante eliminado exitosamente!")
    
    elif max(absences_days_B) >= top:
        position=absences_days_B.index(max(absences_days_B))

        del group_B[position]
        del group_B_age[position]
        del group_B_moth[position]
        del absences_days_B[position]
        print("Estudiante eliminado exitosamente!")

    elif max(absences_days_C) >= top:
        position=absences_days_C.index(max(absences_days_C))

        del group_C[position]
        del group_C_age[position]
        del group_C_moth[position]
        del absences_days_C[position]
        print("Estudiante eliminado exitosamente!")
    
    else:
        print("Ningun estudiante tiene tantas inasistencias, ninguno fue eliminado(a)")
        
    #aca se encuentra el error de que encuentra el primer numero mayor y elimina
    #no evalua si en la siguiente iteracion existe uno mas grande

def show(group_A,group_B,group_C):
    global trainers
    print(f'''Grupo A\nTrainer del grupo: {trainers[0]}\nEstudiantes: {group_A} ''')
    print(f'''Grupo B\nTrainer del grupo: {trainers[1]}\nEstudiantes: {group_B} ''')
    print(f'''Grupo C\nTrainer del grupo: {trainers[2]}\nEstudiantes: {group_C} ''')

def show_student(group_A,group_B,group_C):
    print("\n")
    print("Grupo A")
    for i in range(len(group_A)):
        print(f'''
        Estudiante {i+1}:\nnombre: {group_A[i]}\nmes de ingreso: {group_A_moth[i]}\nedad: {group_A_age[i]}\ninasistencias: {absences_days_A[i]}''')
    print("\n")
    print("Grupo B")
    for j in range(len(group_B)):
        
        print(f'''
        Estudiante {j+1}:\nnombre: {group_B[j]}\nmes de ingreso: {group_B_moth[j]}\nedad: {group_B_age[j]}\ninasistencias: {absences_days_B[j]}''')
    print("\n")
    print("Grupo C")
    for k in range(len(group_C)):
       
        print(f'''
        Estudiante {k+1}:\nnombre: {group_C[k]}\nmes de ingreso: {group_C_moth[k]}\nedad: {group_C_age[k]}\ninasistencias: {absences_days_C[k]}''')
    print("\n")

def traslate():
    group1=input("Ingrese el grupo del coder que desea trasladar: ")
    group2=input("Ingrese el grupo que desea trasladarlo: ")
    name=input("Ingrese el nombre del coder que desea buscar en los grupos: ")
    if (group1 == "A" or group1 == "a") and (group2 =="B" or group2 == "b"):
        
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
        
    elif (group1 == "A" or group1 == "a") and (group2 =="C" or group2 == "c"):

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
        
    elif (group1 == "B" or group1 == "b") and (group2 == "A" or group2 == "a"):

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
        
    elif (group1 == "B" or group1 == "b") and (group2 == "C" or group2 == "c"):

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
    
    elif (group1 == "C" or group1 == "c") and (group2 == "A" or group2 == "a"):

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

    elif (group1 == "C" or group1 == "c")  and (group2 == "B" or group2 == "b"):
        
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


def old_or_young(group_A_age,group_B_age,group_C_age):
  
    
    position1=group_A_age.index(max(group_A_age))
    print(group_A_age)
    print(f"la persona con mayor edad del grupo A es: {group_A[position1]}")
    position2=group_A_age.index(min(group_A_age))
    print(f"la persona con menor edad del grupo A es: {group_A[position2]}")
    print(group_B_age)
    position3=group_B_age.index(max(group_B_age))
    print(f"la persona con mayor edad del grupo B es: {group_B[position3]}")
    position4=group_B_age.index(min(group_B_age))
    print(group_C_age)
    print(f"la persona con menor edad del grupo B es: {group_B[position4]}")
    position5=group_C_age.index(max(group_C_age))
    print(f"la persona con mayor edad del grupo C es: {group_C[position5]}")
    position6=group_C_age.index(min(group_C_age))
    print(f"la persona con menor edad del grupo C es: {group_C[position6]}")

    
def main():
    option=-1 
    while option != 0:
        option=int(input('''Menu
            Ingrese la opcion deseada: 
            1.crear nuevo coder
            2.Registrar Trainer del grupo
            3.Buscar coders duplicados en 2 grupos
            4.Eliminar coders por inasistencia
            5.Ver lista de estudiantes de cada grupo
            6.Ver datos completos de los estudiantes
            7.Trasladar coder de un grupo a otro grupo
            8.Reportar mayor y menor edad de cada grupo
            0.salir
            Opcion : '''))
        
        if option == 1: 
            global flag
            coder_create()
            flag==False
            print(f"cantidad de coders: {count_students}")
        elif option == 2: 
            global trainers
            trainer_group()
        elif option == 3:
            search()
        elif option == 4: 
            absences()
        elif option == 5: 
            show(group_A,group_B,group_C)
        elif option == 6:
            show_student(group_A,group_B,group_C)
        elif option == 7: 
            traslate()
        elif option == 8: 
            old_or_young(group_A_age,group_B_age,group_C_age)



if __name__ == "__main__":
    main()