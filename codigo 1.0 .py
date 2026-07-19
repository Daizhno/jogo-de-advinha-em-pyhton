#jogo de advinha
import random
pontuacao_global = []
jogador = []

def jogadores():
    while True:
        jogadores = input('insira o(s) jogador(es): ').strip()
        jogador.append(jogadores)
        print('mais jogadores?(s/n)')
        opcao = input('').strip().lower()
        if opcao =='s':
            continue 
        if opcao =='n':
            break
            
def jogar_novamente():
        print('jogar novamente?(s/n)')
        opcao = input('').strip().lower()
        if opcao == 'n' :
            nomes = ', '.join(jogador)
            print('='*30)
            print('adeus ;)')
            print(f'Jogadores: {nomes}')
            print(f'Pontuação total: {sum(pontuacao_global)} pontos')
            print('='*30)
            return False
        return True   
             
def pontuacao():
    global pontuacao_global
    print('='*30)
    print('Bem vindo ao jogo da advinha!')
    print('='*30)
    print('facil -- acima de 10 tentativas')
    print('medio -- 10 tentativas')
    print('difícil -- abaixo de 10 tentativas')
    print('-'*30)
    opcao = input('insira a dificuldade: ').strip().lower()
    pontos = {
        'facil': 15 , 
        'medio': 20 , 
        'dificil': 30 , 
        }
    if opcao in ['facil','facíl']:
        print('modo facil selecionado')
        pontuacao_global.append(15)
    elif opcao in ['medio','médio']:
        print('modo medio selecionado')
        pontuacao_global.append(20)
    elif opcao in ['dificil','difícil']:
        print('modo dificil selecionado')
        pontuacao_global.append(30)
    soma = sum(pontuacao_global)
    print(f'Sua pontuação nesta rodada foi somada! Total acumulado: {soma}')
    print('-'*30) 
               
def variacao_numero():
    numero_aleatorio= random.randint(1,101)
    e = 0 # tentativas ate o acerto
    i = int(input('insira em quantas tentativas voce quer tentar: ')) # tentativas
    while i != 0:
        print('-'*20)
        print(f'voce tem',i,'tentativa(s):')
        print('-'*20)
        palpite = int(input('insira seu palpite (de 0 a 100): '))
        e += 1 
        i -= 1 
        
        if palpite > numero_aleatorio:
            print('valor menor')
        elif palpite < numero_aleatorio:
            print('numero maior')
        elif palpite == numero_aleatorio:
            print(f'parabens voce acertou em',e,'tentativas!')
            break
        if i == 0 :
            print('---nao foi dessa vez o numero secreto era:',numero_aleatorio,'---')
            break

jogadores()
continuar = True
while continuar:
    pontuacao()
    variacao_numero()
    continuar = jogar_novamente()
