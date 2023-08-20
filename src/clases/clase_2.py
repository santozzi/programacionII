def lista_de_multiplos(num):
    lista = []
    for i in range(0,num):
        if i % 2 == 0 and i % 3 ==0:
            lista.append(i)
    return lista

def ingreso_de_datos():
    lista = []
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero >=0:
        lista = lista_de_multiplos(numero)
    
        
