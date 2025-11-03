import time
import sys

def saudacao(nome):
    return f'Olá, {nome}! Bem-vindo ao DevSecOps!'

def despedida(nome):
    return f'Até logo, {nome}! Continue aprendendo DevSecOps!'

def loading_animation(duration=3):
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0

    while time.time() < end_time:
        # \r volta o cursor para o início da linha
        sys.stdout.write('\rCarregando... ' + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    # limpar linha no final
    sys.stdout.write('\rCarregamento concluído!   \n')
    sys.stdout.flush()

if __name__ == '__main__':
    nome_usuario = input('Digite seu nome: ')
    print(saudacao(nome_usuario))
    loading_animation(3)
    print(despedida(nome_usuario))
    




