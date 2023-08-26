import pytest
from src.practicos.practico_1 import *

@pytest.mark.parametrize(
        "input_x,input_y,input_z, expected",
        [
            (1,1,1,"equilatero"),
            (1,1,2, "isosceles"),
            (1,2,3,"escaleno")
        ]
        )
def test_tipo_de_triangulo(input_x,input_y,input_z, expected):
    assert tipo_de_triangulo(input_x,input_y,input_z) == expected

@pytest.mark.parametrize(
        "ancho,alto,largo,esperado",
        [
            (4,3,4,6.24),
          
        ]
        )
def test_pintura_para_habitacion_rectangular(ancho,alto,largo,esperado):
    """
    Suponiendo:
      ancho = 4
      alto = 3
      largo = 4
    Puerta: 0,8x2 = 1,6 m2
    Pintura: para 10 m2 ------ 1 litro
    Paredes: 
       A = 2*4*3 = 24
       B = 2*4*3 = 24
       total paredes = 48 m2
    Techo: 4*4 = 16
    Total m2 = paredes + techo - puerta = 62.4 m2
    Suponiendo que la unidad minima que contiene un tacho es 1 litro, redondeo
    hacia arriba
    Litros de pintora = 62.4/10 = 6.24 => 7
    """
    assert pintura_para_habitacion_rectangular(ancho,alto,largo) == esperado

@pytest.mark.parametrize(
    "ancho,alto,largo,manos,esperado",
        [
            (4,3,4,1,6.24),
            (4,3,4,2,12.48),
            (4,3,4,10,62.40),

          
        ]
        )
def test_pintura_para_habitacion_rectangular_manos(ancho,alto,largo,manos,esperado):
    """
    Suponiendo:
      ancho = 4
      alto = 3
      largo = 4
    Puerta: 0,8x2 = 1,6 m2
    Pintura: para 10 m2 ------ 1 litro
    Paredes: 
       A = 2*4*3 = 24
       B = 2*4*3 = 24
       total paredes = 48 m2
    Techo: 4*4 = 16
    Total m2 = paredes + techo - puerta = 62.4 m2
    Suponiendo que la unidad minima que contiene un tacho es 1 litro
    Litros de pintora = 62.4/10 = 6.24
    """
    assert pintura_para_habitacion_rectangular_manos(ancho,alto,largo,manos) == esperado

@pytest.mark.parametrize(
        "n1,n2,n3,esperado",
        [
            (1,2,3,3),
            (3,2,3,3),
            (1,4,3,4),
            (-7,2,7,7),
            (-7,2,7.38,7.38),
        ]
)
def test_mayor_de_tres(n1,n2,n3,esperado):
    assert mayor_de_tres(n1,n2,n3) == esperado

@pytest.mark.parametrize(
        "cadena,esperado",
        [
            ("tengo algunos espacios",2),
            ("tengo",0),
            ("tengo espacios",1),

        ]
)
def test_cuantos_espacios(cadena,esperado):
    assert cuantos_espacios(cadena) == esperado

@pytest.mark.parametrize(
        "serie,esperado",
        [
            ([1,2,3,4,5,6],21),
        ]
)
def test_suma_de_secuencia(serie,esperado):
    assert suma_de_secuencia(serie) == esperado

@pytest.mark.parametrize(
        "serie,esperado",
        [
            ([1,2,3,4,5],3),
        ]
)
def test_promedio_de_secuencia(serie,esperado):
    assert promedio_de_secuencia(serie) == esperado

@pytest.mark.parametrize(
        "a,b,x,esperado",
        [
            (1,78,6,[6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78]),
            (1,5,6,[]),
        ]
)
def test_multiplo_entre_intervalo(a,b,x,esperado):
    assert multiplo_entre_intervalo(a,b,x) == esperado


@pytest.mark.parametrize(
        "cadena,esperado",
        [
            ("cadena123.56",11),
            ("123",3),
            ("",0),
            (",.-a",1)
        ]
)
def test_cantidad_sin_ppuntuacion(cadena,esperado):
    assert cantidad_sin_ppuntuacion(cadena)== esperado

@pytest.mark.parametrize(
        "cadena,esperado",
        [
            ("cadena123 palabra  otraapalabra",3),
            ("",0),
            ("  ",0),
            ("palabra",1)
        ]
)
def test_palabras_separadas_por_espacios(cadena,esperado):
    assert palabras_separadas_por_espacios(cadena) == esperado