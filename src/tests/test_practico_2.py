
from src.practicos.practico_2 import *
import pytest
@pytest.mark.parametrize(
        "cadena, esperado",
        [
            ("cadena","anedac"),
            ("",""),
            ("Cadena","anedaC")
        ]
        )
def test_reverso(cadena:str,esperado:str):
    assert revertir_cadena(cadena) == esperado


@pytest.mark.parametrize(
        "cadena, esperado",
        [
            ("cadena",False),
            ("",True),
            ("Ana",True),
            ("radar",True),
            ("Radar",True)
        ]
        )
def test_palindromo(cadena:str,esperado:bool):
    assert is_palindromo(cadena) == esperado


@pytest.mark.parametrize(
        "year, esperado",
        [
            (2004,True),
            (2005,False),
            (2016,True),
            (2100,False)
          
        ]
        )
def test_es_bisiesto(year:int,esperado:bool):
    assert es_bisiesto(year) == esperado

@pytest.mark.parametrize(
        "day,month, year, esperado",
        [
            (3,8,2023,True),
            (29,2,2023,False),
            (28,8,2023,True),
            (32,8,2023,False),
            (0,0,0,False),
            (31,4,2023,False),
            (31,6,2023,False),
            (31,9,2023,False),
            (31,11,2023,False),
            (30,12,2023,True),
            (30,13,2023,False),
            (-30,-12,2023,False),
            
            ("sergio",1,2023,False),
       
          
        ]
        )
def test_fecha_valida(day:int,month:int,year:int,esperado:bool):
    assert fecha_valida(day,month,year) == esperado