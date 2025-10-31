from app import saudacao

def test_saudacao():
    resultado = saudacao('Teste')
    assert 'Olá, Teste!' in resultado
    assert 'DevSecOps' in resultado

def test_saudacao_vazia():
    resultado = saudacao('')
    assert 'Olá !' in resultado