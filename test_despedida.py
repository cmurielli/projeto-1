from app import despedida

def test_despedida():
    resultado = despedida('Teste')
    assert 'Olá, Teste!' in resultado
    assert 'DevSecOps' in resultado

def test_despedida_vazia():
    resultado = despedida('')
    assert 'Olá, !' in resultado