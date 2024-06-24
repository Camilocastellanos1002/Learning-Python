'''
    Tipo de dato que almacena una cantidad finita de datos en una sola direccion, donde dichos datos pueden ser de cualquier tipo
    como lo son los strings, float, int, booleanos, etc. 

    para referenciarse algun elemento de la lista, es nesesario utilizar entre corchetes un indice
'''

list=[7,"hola",True,3.5]
print(list)
print(type(list))
print(list[2])

list.insert(2,"C")  #metodo que inserta nuevos valores a una lista donde se debe especificar ( posicion y/o indice, valor a agregar )
print(list)

list.append(False) #metodo que inserta o agrega valores, por defecto se agregan al final de la lista
print(list)

list2=["billetera","celular", 300000,"ey"]
list.extend(list2)      #metodo que genera la union entre 2 listas, extiende una lista con otra

print(list)

del list[-1]            #funcion que elimina un dato de la lista, se debe proporcionar la posicion que se desea eliminar
print(list)

list.remove("billetera")    #metodo que elimina un valor de la lista, se debe proporcionar que valor se desea eliminar
print(list)

list.clear()
print(list)

list=[7,"hola",True,3.5]
print(list)
object=list.pop(1)
print(object)
print(list)


longitud=len(list)
print(list)

list2=[1,2,3,4,5,6,7,8,9]
print(list2[0:5])


lista_3=[7,"hola", True, 3.54, "F", False, 10]
for i in lista_3:
    print(i)

lista_num=[3,5,6,7,8,30,434,53445,23,4543,121,23,1]
lista_num.sort()
print(lista_num)

lista_num.reverse()
print(lista_num)