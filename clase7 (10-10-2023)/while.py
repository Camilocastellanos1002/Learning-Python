

def create_list():
    my_list=[]
    quantity=int(input("ingrese la longitud de que desea tener la lista: "))
    for i in range(quantity):
        my_list.append(int(input(f"ingrese el valor #{i+1} de la lista: ")))
    print("Lista creada exitosamente!")
    return my_list
        
def show(list):
    for i in range(len(list)):
        print(list[i])

def modify(my_list):
    value=int(input("ingrese el nuevo valor que desea agregar: "))
    key=int(input("ingrese la posicion donde desea agregar el nuevo valor: "))
    my_list.insert(key,value)
    print("valor agregado!")
    return my_list

def remov(my_list):
    del my_list[-1]
    print("valor eliminado!")
    return my_list

def new(my_list):
    value=input("ingrese el valor que de sea agregar: ")
    my_list.append(value)
    print("valor agregado!")
    return my_list

def delete(my_list):
    value=int(input("ingrese el valor que desea eliminar: "))
    my_list.remove(value)
    print("valor eliminado!")
    return my_list

def organize_asc(my_list):
    my_list.sort()
    print("Lista organizada de forma ascendente!")
    return my_list

def organize_des(my_list):
    my_list.sort()
    my_list.reverse()
    print("Lista organizada de forma descendente!")
    return my_list




option=-1
while (option)!=0:
    print('''Menu:
          1.Crear la lista
          2.Agregar un valor de la lista
          3.Agregar un nuevo valor en el final de la lista
          4.Remover el ultimo valor de la lista
          5.Eliminar un valor deseado
          6.Organizar valores de forma ascendente
          7.Organizar valores de forma descendente
          8.Imprimir la lista
          0.Salir

    ''')

    option=int(input("ingrese la opcion deseada: "))
    if option==1: new_list=create_list()
    elif option ==2: new_list=modify(new_list)
    elif option == 3: new_list=new(new_list)
    elif option == 4: new_list=remov(new_list)
    elif option == 5: new_list=delete(new_list)
    elif option == 6: new_list=organize_asc(new_list)
    elif option == 7: new_list=organize_des(new_list)
    elif option ==8: show(new_list) 
        