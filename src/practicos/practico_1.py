import math
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
