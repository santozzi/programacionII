def reverso(cadena:str)->str:
    r_cadena =""
    for i in range(len(cadena)-1,-1,-1):
        r_cadena += cadena[i]
    return r_cadena

def palindromo (cadena:str)->bool:
    return cadena.lower()==reverso(cadena).lower()

def es_bisiesto(year:int)->bool:
    return year % 4 ==0 and (year % 100 !=0 or year % 400 == 0)

def fecha_valida(day:int,month:int,year:int)->bool:
   traintayuno = [1,3,5,7,8,10,12]
   treinta = [4,6,9,11]
   es_valido = False
   if month in traintayuno:
       es_valido = day >=1 and day <= 31
       
   elif month in treinta:
       es_valido = day >=1 and day <= 30
   elif month == 2:
       if es_bisiesto(year):
           es_valido = day >=1 and day <= 29
       else:
           es_valido = day >=1 and day <= 28
            
       

       #enero 1 31

       #febrero 2 28
       #marzo 3 31
       #abril 4 30
       #mayo 5 31
       #junio 6 30
       #julio 7 31
       #agost 8 31
       #septiembre 9 30
       #octubre 10 31
       #noviembre 11 30
       #diciembre 12 31

