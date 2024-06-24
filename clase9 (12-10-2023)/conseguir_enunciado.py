
vm=[]
va=[]
vv=[]
c=-1
for i in range(4):
    vm.append(input("escriba el nombre estudiante que perdio matematicas "))
for j in range(4):
    va.append(input("escriba el nombre estudiante que perdio algebra "))
for a in range(4):
    for b in range(4):
        if vm[a] == va [b]:
            c=c+1
            vv.append(vm[a])

for x in range(len(vv)):
    print("estos estudiantes perdieron las dos materias",vv[x])
    