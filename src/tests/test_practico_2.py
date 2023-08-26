
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
    assert reverso(cadena) == esperado


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
    assert palindromo(cadena) == esperado


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