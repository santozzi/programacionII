
def tipo_de_triangulo(l1:float,l2:float,l3:float)->float:
    triangulo = "isoseles"
    if l1 > 0 and l2 >= 0 and l3 >=0:
        if l1==l2 and l2==l3:
            triangulo= "equilatero"
        elif l1==l2 or l2==l3:
            triangulo = "isosceles"
        else:
            triangulo = "escaleno"
    else:
        triangulo = "los lados del triangulo deben ser mayores que 0"
    return triangulo

def pintura_para_habitacion_rectangular(ancho:float,alto:float,largo:float)->float:
    """
    Ejercicio 2
    A partir del ancho, alto y largo de una habitación rectangular, calcula 
    la cantidad de pintura en litros necesarios para pintarla
    teniendo en cuenta que 1 litro de pintura sirve para 10 m2
    y la habitacion tiene solo una puerta de 0.8x2 m 
    Agrego que el piso no se pinta pero si el techo
    """
    puerta = 0.8*2
    proporcion_pintura_m2 = 1/10
    m2 = 2*ancho*alto + 2*alto*largo + ancho*largo - puerta
    return float("{:.2f}".format(m2*proporcion_pintura_m2))

def pintura_para_habitacion_rectangular_manos(ancho:float,alto:float,largo:float,manos:int)->float:
    """
    Ejercicio 3
    Igual al 2 pero con cantidad de manos

    """
   
    return float("{:.2f}".format(pintura_para_habitacion_rectangular(ancho,alto,largo)*manos))

def mayor_de_tres(n1:float,n2:float,n3:float)->float:
    """
    Ejercicio 4
    Cual n es mayor y mostrar un mensaje en pantalla
    
    """
    return max(n1,n2,n3)

def ingreso_de_mayor_de_tres_in():
    """
    Ejercicio 4 ingreso
    """
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))

    #TODO verificar que sean correctos
    mayor = mayor_de_tres(n1,n2,n3)
    print(f"El manyor entre {n1},{n2} y {n3} es {mayor}")

def cuantos_espacios(cadena:str)->int:
    """
    Ejercicio 5
    """
    return cadena.count(' ')

def cuantos_espacios_ingreso():
    """
    Ejercicio 5 ingreso
    TODO hacer el ingreso de datos
    """

def secuencia(n:int):
    for i in range(1,n+1):
        print(f"{i}",end=' ')

def secuencia_par(n:int):
    for i in range(1,n+1):
        if i % 2 == 0:
            print(f"{i}",end=' ')

def secuencia_ingreso():
    secuencia(int(input("ingrse un numero positivo: ")))
    print()
    secuencia_par(int(input("ingrse un numero positivo: ")))
#secuencia_ingreso()

def suma_de_secuencia(numeros:list) -> float:
    resultado:float = 0
    for numero in numeros:
        resultado = resultado + numero
    return resultado
        
def promedio_de_secuencia(numeros:list)->float:
    return suma_de_secuencia(numeros)/len(numeros)

def operaciones_numeros():
   lista = []
   n = int(input("Ingrese la cantidad de numeros para la secuencia: "))
   for i in range(0,n):
       numero = float(input(f"numero {i+1}: "))
       lista.append(numero)
   print(f"La suma de la secuencia es: {suma_de_secuencia(lista)}")
   print(f"El promedio de la secuencia es: {promedio_de_secuencia(lista)}")

#operaciones_numeros()

def multiplo_entre_intervalo(a:int,b:int,x:int)->list:
    lista = []
    for i in range(a,b+1):
        if i % 6 == 0:
            lista.append(i)
    return lista

def dibujar_rectangulo(ancho,alto,caracter,relleno):
    carsep = caracter + '  '
    print(carsep*ancho)
    for i in range(0,alto-2):
        print(f"{caracter}  {(relleno+'  ')*(ancho-2)}{caracter}",sep='')
    print(carsep*ancho)

#dibujar_rectangulo(40,40,'b','o')

def promedio_y_cantidad_ingresada():
    salida = False
    lista = []
    while not salida:
        numero = int(input("ingrese num pos: "))
        if numero >=0:
            lista.append(numero)
        else:
            salida = True
    
    print(f"El Promedio es: {promedio_de_secuencia(lista):.2f} con cantidad de numeros {len(lista)}")

#promedio_y_cantidad_ingresada()
#Inicio Ejercicio 12
def esta_ordenada(lista:list) ->bool:
    listaOrdenada:list = []
    for item in lista:
        listaOrdenada.append(item)
    listaOrdenada.sort()

    return listaOrdenada == lista

def recolectar_secuencia_de_numeros():
    salida = False
    lista = []
    while not salida:
        try:
            numero = int(input("ingrese num pos: "))
            if numero !=0:
                lista.append(numero)
            else:
                salida = True
            
        except:
            print("Ingrese un número: ")
    print(f"Lista ingresada ordenada: {esta_ordenada(lista)}")

#recolectar_secuencia_de_numeros()
#Fin Ejercicio 12
def caracter_consecutivo():
    caracter = input("Ingresar un caracter: ")
    numero = int(input("Ingrese un número: "))
    print(caracter*numero)

#caracter_consecutivo()

def cantidad_de_vocales():
    cadena= input("Ingrese una cadena: ")
    cantidad_de_vocales = cadena.count('a')
    cantidad_de_vocales += cadena.count('e')
    cantidad_de_vocales += cadena.count('i')
    cantidad_de_vocales += cadena.count('o')
    cantidad_de_vocales += cadena.count('u')
    print(f"La cantidad de vocales de la cadena es: {cantidad_de_vocales}")
    return cantidad_de_vocales
#cantidad_de_vocales()
def cantidad_sin_ppuntuacion(cadena:str):
    contador:int = 0
    for caracter in cadena:
        if caracter.isalpha() or caracter.isalnum():
            contador += 1
    return contador

def palabras_separadas_por_espacios(cadena:str):
    lista = cadena.split()
    return len(lista)

def propiedades_de_cadena(cadena:str):
    print(f"Número total de caracteres: {len(cadena)}")
    print(f"Cantidad de total de letras sin signos de puntuación: {cantidad_sin_ppuntuacion(cadena)}")
    print(f"Cantidad de palabras separadas por espacios: {palabras_separadas_por_espacios(cadena)}")