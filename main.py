import random

v1 = 0
v2 = 0
empate = 0
print('                JOGO PEDRA PAPEL TESOURA')
print('1 - PARA PEDRA      2 - PARA PAPEL      3 - PARA TESOURA')
print('Para mostrar os resultador digite = 4')
print('Para sair digite = 5')
print('-'*20)
while(True):
    try:
        res = int(input('Digite aqui: '))
        if(res==1):
            lista = [1,2,3]
            escolha = random.choice(lista)
            print('Escolho {}'.format(escolha))
            if(escolha==1):
                print('Empate!')
                print('-' * 10)
                empate +=1
            elif(escolha==2):
                print('Você perdeu!')
                print('-' * 10)
                v2 +=1
            elif(escolha==3):
                print('Você ganhou!')
                print('-' * 10)
                v1 +=1
        elif (res == 2):
            lista = [1, 2, 3]
            escolha = random.choice(lista)
            print('Escolho {}'.format(escolha))
            if (escolha == 2):
                print('Empate!')
                print('-' * 10)
                empate +=1
            elif (escolha == 1):
                print('Você ganhou!')
                print('-' * 10)
                v1 +=1
            elif (escolha == 3):
                print('Você perdeu!')
                print('-' * 10)
                v2 +=1
        elif (res == 3):
            lista = [1, 2, 3]
            escolha = random.choice(lista)
            print('Escolho {}'.format(escolha))
            if (escolha == 3):
                print('Empate!')
                print('-' * 10)
                empate +=1
            elif (escolha == 1):
                print('Você perdeu!')
                print('-' * 10)
                v2 +=1
            elif (escolha == 2):
                print('Você ganhou!')
                print('-' * 10)
                v1 +=1
        elif(res==4):
            print('-'*10)
            print('Você ganhou {} vezes'.format(v1))
            print('E perdeu {} vezes'.format(v2))
            print('Empatando {} vezes'.format(empate))
            print('-' * 10)
            print('Jogar novamente?  Sim == 4   Não == 5 ')
            res2 = int(input('Digite aqui: '))
            if(res2==4):
                print('Preparado para perder? ')
                print('-' * 10)
                continue
            elif(res2==5):
                print('Encerrando o Programa.....')
                break
        elif(res>=6 or res<=0):
            print('Valor inválido!')
    except ValueError:
        print('Valor inválido!')