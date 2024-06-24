#ejercicio propio
#cuadre o cierre de ventas de una carniceria
sales=0
items=int(input("ingrese la cantidad de articulos (cortes de carne) que vende en el negocio: "))
for i in range(items):
    item_name=input(f"ingrese el nombre del articulo #{i+1}: ")
    ganado_kg=float(input(f"ingrese el valor de {item_name} por kg: "))
    initial_product=float(input(f"ingrese la cantidad de {item_name} por kg en inventario inicial: "))
    final_product=int(input(f"ingrese la cantidad de {item_name} por kg en inventario final: "))
    loss_kg=int(input(f"ingrese la cantidad de mermas y/o perdidas de {item_name} en kg: "))
    
    sales= sales+int(((initial_product-final_product)-loss_kg)*ganado_kg)

bills=int(input("ingrese el valor total de gastos de operacion del dia: "))

total = (sales-bills)

print(f"ventas: ${sales}\ngastos: ${bills}\nventa neta: ${total}")

if total < 0: print(f"estas en perdida, ponte las pilas!")
elif total == 0: print(f"punto de equilibrio!\nrentabilidad 0, los gastos igualan las ventas")
elif total > 0: print(f"Tienes ganancias, continua asi!")
else: print("ingreso datos erroneos")
