'''Comentario'''
#adsasd

var = 1
print(type(var)) #Muestra el tipo de variable que es.
print("")
# Cadena de caracteres
cadena1="Clase n° 1"
cadena2='Curzo de Python'
print(type(cadena1))
# Boolean (True -> V, False -> F)
encendido= True
print(type(encendido))
print("")
# Operadores aritméticos
# Suma
x=20
y=5
res = x-y
print(res)
# Suma
res=x+y
print(res)
#Mult
res=x*y
print(res)
# Exponente **
res = x**2
print(res)
print("")
# Division entera //
res= x//3
# Modulo %. Divide el operando de la izquierda por el operador de 
# la derecha y devuelve el resto.
res=7%2
print(res)
print("")
# Operaciones con cadena
print(cadena1+" "+cadena2)
print(cadena1*2)
print("")
# Operaciones logicas con retorno Boolean
print(x==20) # True
print(x==2) # False
print(x!=20) # Negación que afirma que es verdad
print(x!=2) # Negación que afirma que es falso
print("")
# Listas = Arrays
personas=[]
personas=["Juan","Ana","Marcelo"]
numeros=[1, 2, 3, 10]
print(personas[0])
print("")
varios1=[True, -5, "hola mundo", [1, 10]]
varios1[3]= "Inicio de la clase"
print(varios1[3]) # Muestra lista dentro de lista
print("")
# Append -> Agrega un elemento al final
numeros.append(100)
print(numeros)
print("")
#Insert -> Inserta un elemento en una ubicacion especifica
numeros.insert(0, -20)
print(numeros)
print("")
#Eliminar elemento
del personas[2]
print(personas)
print("")
# Tuplas -> Inmutables. No se pueden modificar
var_t=(10, 20, 6)
print(var_t[0])
print("")
var_t_unica=(10,) # Crearcion tupla con un solo valor
print(var_t_unica[0])
print("")
var1=[10, 20, 30]
var2=[40, 50]
print(var1+var2)
print("")
# Diccionarios -> Clave: Valor
cliente={"Nombre": "Juan", "Edad":25, "Direccion":"25 de Mayo 1000"}
print("")
# None (is) -> Boolean
n=None
print(n is None)
print("")
# Operaciones logicas
#Conjuncion -> Retorna True siempre que ambos lados de la operacion sean verdaderas
print(True and True)
print(False and True)
print("")
# Disyuncion -> Reterona True siempre que alguno de los operandos sea True
print(True or True)
print(False or True)
print(False or False)
print("")
# Negacion -> not
print(not True)
print("")
#Condicionales
edad=int(input("ingrese edad: "))
if(edad>18):
    print("Mayor de edad")
else:
    print("Menor de edad")