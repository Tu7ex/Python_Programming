largo=int(input("Ingrese largo de la lista: "))
lista=[]
i=0
while i<largo:
    i=i+1
    print("Ingrese", i)
    add=int(input("Valor: "))
    lista.append(add)
    print("----------")
print("La lista es:", lista)
print("")
i=0
posicion=0
suma=0
for i in range(len(lista)):
    posicion=lista[i]
    suma=posicion+suma
total=suma-posicion
print("")
print("El total menos el ultimo numero es: ", total)
