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
