'''
    problema ambiental
'''
n_municipalities=0

def reading(names,smells,illegal_towns,pollution_rivers,tons_trash):
    global n_municipalities

    name=input("ingrese el nombre del municipio: ")
    names.append(name)
    smells.append(int(input(f"ingrese el porcentaje de olores ofensivos en el municipio {name}: ")))
    illegal_towns.append(int(input(f"ingrese el porcentaje de asentamientos ilegales en el municipio {name}: ")))
    pollution_rivers.append(int(input(f"ingrese el porcentaje de contaminacion en los rios del municipio {name}: ")))
    tons_trash.append(int(input(f"Ingrese la cantidad de toneladas/dia de basura que el municipio {name} genera: ")))
    n_municipalities=n_municipalities+1

    
    return names,smells,illegal_towns,pollution_rivers,tons_trash

def more_tons(names,tons_trash):
    more=max(tons_trash)
    position=tons_trash.index(more)
    name=names[position]
    return name,more

def less_tons(names,tons_trash):
    less=min(tons_trash)
    position1=tons_trash.index(less)
    name=names[position1]
    return name,less
    
def average_tons_day(tons_trash):
    sum=0
    for i in range(len(tons_trash)):
        sum= sum + tons_trash[i]
    average=sum/n_municipalities
    return average

def average_tons_moth(tons_trash):
    sum1=0
    for i in range(len(tons_trash)):
        sum1= sum1 + tons_trash[i]
    average_moth=(sum1*30)/n_municipalities
    return average_moth

def average_smells(smells):
    sum=0
    for i in range(len(smells)):
        sum= sum + smells[i]
    average_smell=(sum*100)/n_municipalities
    return average_smell

def average_towns(illegal_towns):
    sum=0
    for i in range(len(illegal_towns)):
        sum= sum + illegal_towns[i]
    average_town=(sum*100)/n_municipalities
    return average_town

def average_rivers(pollution_rivers):
    sum=0
    for i in range(len(pollution_rivers)):
        sum= sum + pollution_rivers[i]
    average_rivers=(sum*100)/n_municipalities
    return average_rivers

def mayor_problem(names,smells,illegal_towns,pollution_rivers):
    sum_problem=[]
    for i in range(len(names)):
        sum_problem.append(smells[i]+illegal_towns[i]+pollution_rivers[i])
    mayor=max(sum_problem)
    position=sum_problem.index(mayor)
    town=names[position]
    return mayor,town

def menor_problem(names,smells,illegal_towns,pollution_rivers):
    sum=[]
    for i in range(len(names)):
        sum.append(smells[i]+illegal_towns[i]+pollution_rivers[i])
    menor=min(sum)
    position=sum.index(menor)
    town=names[position]
    return menor,town

def main():

    option="Z"
    names=[]
    smells=[]
    illegal_towns=[]
    pollution_rivers=[]
    tons_trash=[]

    while option != "K" or option!="k":
        option=input('''Menu
            A.Lectura de datos
            B.Municipio que mas toneladas/dias genera
            C.Municipio que menos toneladas/dias genera
            D.promedio de toneladas de basura/dia
            E.Promedio de toneladas de basura/mes
            F.Mayor problema ambiental
            G.Menor problema ambiental
            H.Promedio de olores ofensivos
            I.Promedio de creacion asentamientos ilegales
            J.Promedio de contaminacion de corrientes hidricas
            K.Terminar
            ''')
        if option == "A" or option == "a":

            names,smells,illegal_town,pollution_rivers,tons_trash= reading(names,smells,illegal_towns,pollution_rivers,tons_trash)
            print("Municipio ingresado satisfactoriamente!")
        elif option == "B" or option == "b":
            name,more= more_tons(names, tons_trash)
            print(f"el municipio que genera mas basura es: {name} con un total de {more} toneladas/dia ")
        elif option == "C" or option == "c":
            name2,less= less_tons(names, tons_trash)
            print(f"el municipio que genera menos basura es: {name2} con un total de {less} toneladas/dia ")
        elif option == "D" or option == "d":
            average=average_tons_day(tons_trash)
            print(f"El promedio de basuras por dia de todos los municipios es: {int(average)} toneladas/dia ")
        elif option == "E" or option == "e":
            average_moth=average_tons_moth(tons_trash)
            print(f"El promedio de basura por mes de todos los municipios es: {int(average_moth)} toneladas/mes")
        elif option == "H" or option == "h":
            average_smell=average_smells(smells)
            print(f"El promedio de olores ofensivos de todas las ciudades es: {int(average_smell)} OU(E/m^3)")
        elif option == "I" or option == "i":
            town=average_towns(illegal_towns)
            print(f"El promedio de asentamientos ilegales todos las municipios es: {int(town)} Personas/m^2")
        elif option == "J" or option == "j":
            rivers=average_rivers(pollution_rivers)
            print(f"El promedio de contaminacion de rios en los municipios es: {int(rivers)} ISQA(Indice Simplificado de calidad de agua)")
        elif option == "F" or option == "f":
            mayor,town2=mayor_problem(names,smells,illegal_towns,pollution_rivers)
            print(f"La ciudad con mas problema ambiental es: {town2} con un total de : {mayor}%")
        elif option == "G" or option == "g": 
            menor,town3=menor_problem(names,smells,illegal_towns,pollution_rivers)
            print(f"La ciudad con menos problema ambiental es: {town3} con un total de: {menor}%")
            
    print(f"Total de ciudades ingresadas: {n_municipalities}")
    print(f'''ciudades: {names}\nOlores ofensivos: {smells}\nAsentamientos ilegales: {illegal_town}\nContaminacion de rios: {pollution_rivers}\nToneladas de Basura/dia:{tons_trash}''')

if __name__ == "__main__":
    main()