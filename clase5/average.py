#algoritmo que halla el promedio general de una facultad
#M=masculino, F=femenino
students=int(input("ingrese la cantidad de los estudiantes: "))
sum=0
cm=cf=sum_age=max=0
min=5.0

for i in range(students):
    name=input(f"ingrese el nombre del estudiante {i+1} ")
    notes=float(input(f"ingrese la nota del estudiante #{i+1}: "))
    age=int(input("ingrese la edad del estudiante: "))

    sum=sum+notes
    sum_age=sum_age+age
    sexo=input(f"ingrese sexo del estudiante {i+1}: ")
    if sexo == "M" or sexo == "m":
        cm= cm+1
    elif sexo == "F" or sexo == "f":
        cf=cf=1
    
    if notes > max:
        max=notes
        higher=name
    
    if notes < min:
        min= notes
        lower = name

    


average=sum/students
average_age= sum_age/students
print("el promedio de las notas de la facultad es: ",average)
print(f"en la facultad hay {cm} hombres y {cf} de mujeres")
print("el promedio de edad de la facultas es: ",int(average_age))
print(f"la mejor nota de la facultad es de {max} y es del estudiante {higher}")
print (f"la peor nota de la facultad es de {min} y es del estudiante {lower}")
