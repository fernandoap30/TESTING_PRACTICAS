
from primo import es_primo

def test_es_primo():
    resultado = es_primo(3)
    assert resultado == True

def test_no_es_primo():
    resultado = es_primo(10)
    assert resultado == False