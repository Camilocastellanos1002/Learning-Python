'''
    programa del promedio de una facultad modificado con listas e iteraciones con while
    #M=masculino, F=femenino
'''
option=-1
while option!=0:
    print('''\nBienvenido a la plataforma de la facultad\n
          1.Ingrese datos de nuevo estudiante
          2.Ingresar notas del estudiante
          3.Calcular promedio del estudiante
          4.Ver la mejor nota de la facultad
          5.Ver la peor nota de la facultad
          6.Calcular el promedio de la Facultad
          7.Ver cantidad de mujeres en la facultad
          8.Ver cantidad de hombres en la facultad
          9.Ver cantidad de estudiantes en la facultad
          10.mi funcion1
          11.mi funcion2


''')
















'''
#algoritmo que halla el promedio general de una facultad
#M=masculino, F=femenino
students=int(input("ingrese la cantidad de los estudiantes: "))
sum=0
cm=cf=sum_age=max=0
min=5.0

for i in range(students):
    name=input(f"ingrese el nombre del estudiante: {i+1} ")
    sum_notes=0
    for j in range(3):
        sum_notes=sum_notes+float(input(f"ingrese la nota #{j+1} del estudiante #{i+1}: "))
    
    average_note_def=sum_notes/3
    print(f" la nota definitiva del estudiante {name} es de: {average_note_def}")
    age=int(input("ingrese la edad del estudiante: "))

    sum=sum+average_note_def
    sum_age=sum_age+age
    sexo=input(f"ingrese sexo del estudiante {i+1}: ")
    if sexo == "M" or sexo == "m":
        cm= cm+1
    elif sexo == "F" or sexo == "f":
        cf=cf=1
    
    if average_note_def > max:
        max=average_note_def
        higher=name
    
    if average_note_def < min:
        min= average_note_def
        lower = name

    


average=sum/students
average_age= sum_age/students
print("El promedio de las notas de la facultad es: ",average)
print(f"En la facultad hay {cm} hombres y {cf} de mujeres")
print("El promedio de edad de la facultas es: ",int(average_age))
print(f"La mejor nota de la facultad es de {max} y es del estudiante {higher}")
print (f"La peor nota de la facultad es de {min} y es del estudiante {lower}")

'''