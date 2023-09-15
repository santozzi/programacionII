#Ejercicio 1
def reverso(cadena:str)->str:
    r_cadena =""
    for i in range(len(cadena)-1,-1,-1):
        r_cadena += cadena[i]
    return r_cadena

def palindromo (cadena:str)->bool:
    return cadena.lower()==reverso(cadena).lower()

#fin ejercicio 1

#Ejercicio 2
def es_bisiesto(year:int)->bool:
    return year % 4 ==0 and (year % 100 !=0 or year % 400 == 0)

def fecha_valida(day:int,month:int,year:int)->bool:
   traintayuno = [1,3,5,7,8,10,12]
   treinta = [4,6,9,11]
   es_valido = False
   try:
      if month in traintayuno:
            es_valido = day >=1 and day <= 31
            
      elif month in treinta:
            es_valido = day >=1 and day <= 30
      elif month == 2:
          if es_bisiesto(year):
               es_valido = day >=1 and day <= 29
          else:
               es_valido = day >=1 and day <= 28
   except:
       es_valido=False 
                    
   return es_valido

#fin ejercicio 2
#Ejercicio 3
def indice_mas_grande(lista:list)->int:
    indice = 0
    mayor = lista[0]
    for i in range(0,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i
    #tupla mayor, indice
    return (mayor,indice)

def ingreso_de_notas():
    notas:list = []
    cantidad_de_notas = int(input("Ingrese la cantidad de notas: "))
    mayor:float = 0
    indice = 0
    for i in range(0,cantidad_de_notas):
        nota = float(input("Ingrese la nota: "))
        notas.append(nota)
    #desestructuracion de tupla   
    mayor,indice = indice_mas_grande(notas)    
    print("La nota mayor es: ",mayor," y se encuentra en la posicion: ",indice)
    
#ingreso_de_notas()
#ejercicio 4
def lista_de_digitos():
    lista = []
    try:
        numero = int(input("Ingrese un numero: "))
        while numero > 0:
            lista.insert(0,numero % 10)
            numero = numero // 10
    except:
        print("El numero ingresado no es valido")
    
    print(f"La lista de digitos es: {lista}")
    print(f"El mayor es: {indice_mas_grande(lista)[0]}")
    print(f"El indice del mayor es: {indice_mas_grande(lista)[1]}")

#lista_de_digitos()
#fin ejercicio 4
#Ejercicio 5

def esta_aprobado(nota:float)->bool:
    return nota >= 40;

def alumnos_notas():
    diccionario:dict = {}
    cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(0,cantidad_de_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        nota = float(input("Ingrese la nota: "))
        diccionario[nombre] = nota
    
    return diccionario

def listado():
    items = alumnos_notas().items()
    print ("{:<10} {:<10} {:<10}".format('ALUMNOS','PARCIAL','RESUTADO'))
    for item in items:
        print("{:<10} {:<10} {:<10}".format(item[0],item[1],'Aprobado' if esta_aprobado(item[1]) else 'Desaprobado') )
   

#listado()
#fin ejercicio 5
#Ejercicio 6
def leer_archivo():
   lista = list()
   try:
       archivo = open("src/practicos/db/ejercicio6.txt","r")
       
       for linea in archivo:
            lista.append(linea)
       archivo.close() 
   except:
        print("No se pudo abrir el archivo")    
   
   return lista
   
 


def promedio_de_lista(lista):
    suma = 0
    for linea in lista:
        suma += float(linea)
    return suma / len(lista)
    

def numeros_superan_promedio(lista,promedio):
    lista_superan = list()
    for linea in lista:
        if float(linea) > promedio:
            lista_superan.append(linea)
    return lista_superan

#lista = leer_archivo()
#promedio = promedio_de_lista(lista)
#print(f"La distancia promedio de los viaes es {promedio} y los vias con distancia mayor son: {numeros_superan_promedio(lista,promedio)}")
#print(promedio_de_lista())


def precio_de_producto_por_codigo(codigo:int,lista:list,delimitador:str):
    # 100;producto;100

    #item = [valor for valor in lista if valor.split(delimitador)[0] == codigo]
    valor =""
    for item in lista:
        if int(item.split(delimitador)[0]) == codigo:
            valor = item.split(delimitador)
    return valor

def precio_de_producto_por_nombre(producto:str,lista:list,delimitador:str):
    # 100;producto;100

    #item = [valor for valor in lista if valor.split(delimitador)[0] == codigo]
    valor =""
    for item in lista:
        if item.split(delimitador)[1] == producto:
            valor = item.split(delimitador)
    return valor
  


lista = [
    "100;arroz;10",
    "102;fideos;5",
    "135;lentejas;8",
    "138;porotos;6",
    "140;sal gruesa;5",
    "201;aceite;20"
]

item = precio_de_producto_por_nombre("fideos",lista,";")

print(f"Nombre del producto: {item[1]}")
print(f"precio del producto: {item[2]}")


""" #Estructuas en python

#lista
lista = list()
lista=[]
lista = [1,2,3,4,5,6,7,8,9,10]
lista[0] = 5

lista = ["sergio",75]

#tupla
tupla = tuple()
tupla = ()
tupla = (1,2,3,4,5,6,7,8,9,10)

#diccionario
diccionario = dict()
diccionario = {}

diccionario["sergio"] =75
diccionario["maria"] = 80
diccionario["jose"] = 90

print(diccionario["sergio"])

print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())

for item in diccionario.items():
    print(f"Nombre: {item[0]},Nota: {item[1]}")

for key in diccionario.keys():
    print(f"Nombre: {key},Nota: {diccionario[key]}") """
