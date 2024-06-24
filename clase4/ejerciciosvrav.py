#ejercicio de sueldo empleado
'''
salary=int(input("ingrese el salario del empleado en pesos colombianos: "))
if salary > 10**6:
    print(f"tu salario ${salary} supera el monto de 10 millones, por lo tanto debes pagar impuesto")
else:
    print(f"tu salario ${salary}  no supera el monto de 10 millones, por lo tanto no debes pagar impuesto")

'''
#ejercicio de promedio
'''
income1=int(input("digita tu primer ingreso: "))
income2=int(input("digita tu segundo ingreso: "))
income3=int(input("digita tu tercero ingreso: "))
income4=int(input("digita tu cuarto  ingreso: "))
sum= income1+income2+income3+income4
average=sum/4
print("promedio de ingresos: ", int(average))
if sum < 5*10**5:
    print("tus ingresos son muy bajos, debes buscar trabajo")
else:
    print("tus ingresos son altos, dona a un niño de bajo recursos")
'''
'''
#ejercicio de corriente
resistance=int(input("ingrese la resistencia de la corriente: "))
intensity=int(input("ingrese la intensidad de la corriente: "))

voltage= intensity*resistance
if voltage > 2*10**3:
    print("el valor del voltaje es: ",voltage)
    print("Peligro, Alto Voltaje")
else:
    print("el valor del voltaje es: ",voltage)
'''

#ejercicio de facturacion
product=input("ingrese el nombre del producto: ")
price=int(input("ingrese el precio del producto: $"))
cuantity=int(input("ingrese la cantidad de productos: "))
total=int(price*cuantity)
tax=int(total*0.19)

if total >= 8*10**5 and total < 9*10**5 and total < 10**6:
    
    discount=int(total*0.1)
    total_with_dis=int(total-discount)
    fact=int(total_with_dis+tax)

    print("el monto de la compra es: $",total)
    print("descuento del 10%: $",int(discount))
    print("el monto con descuento es: $",int(total_with_dis))
    print("el monto facturado es menor que un millon, se te cobrara impuesto por bajo monto de comercializacion")
    print("impuesto 19% : $",int(tax))
    print(f"la factura por la compra de {product} es de ${fact}")

elif total >= 9*10**5 and total < 10**6:

    discount=int(total*0.15)
    total_with_dis=int(total-discount)
    fact=int(total_with_dis+tax)

    print("el monto de la compra es: $",total)
    print("descuento del 15%: $",discount)
    print("el monto con descuento es: $",total_with_dis)
    print("el monto facturado es menor que un millon, se te cobrara impuesto por bajo monto de comercializacion")
    print("impuesto 19% : $",tax)
    print(f"la factura por la compra de {product} es de ${fact}")

elif total >= 10**6:

    discount=int(total*0.5)
    total_with_dis=int(total-discount)
    
    print("el monto de la compra es: $",total)
    print("descuento del 50%: $",discount)
    print(f"la factura por la compra de {product} es de ${total_with_dis}")

else:
    fact=int(total+tax)

    print("el monto de la compra es: $",total)
    print("el monto facturado es menor que un millon, se te cobrara impuesto por bajo monto de comercializacion")
    print("impuesto 19% : $",tax)
    print(f"la factura por la compra de {product} es de ${fact}")