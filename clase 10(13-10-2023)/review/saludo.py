#importar libreria datetime
from datetime import datetime
#funcion now, devuelve fecha y hora actual del sistema
real_time =datetime.now()
#formato de impresion de la hora
reloj=real_time.strftime("%H:%M:%S")
#ingresar el nombre del estudiante
name=input("ingrese el nombre del estudiante: ")
#Hora actualizada
#print(real_time.year, real_time.month, real_time.day)
#print(reloj)
#Criterio
if reloj > "0:0:0" and reloj < "11:59:59":
    print(f"Buenas dias, {name}!\nBienvenido(a)")
elif reloj > "11:59:59" and reloj < "18:59:59":
    print(f"Buenas tardes, {name}\nBienvenido(a)")
elif reloj > "18:59:59" and reloj < "23:59:59":
    print(f"Buenas noches, {name}\nBienvenido(a)")


