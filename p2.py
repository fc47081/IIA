# -*- coding: utf-8 -*-
from jogos_iia import *
from peoesN import *

##def win (jogador, estado):
##    obj = 1 if jogador == 'pretas' else 8
##    condicao1 = obj in [x for (x, _) in estado.board[1][jogador]]
##    condicao2 = estado.board[1][JogoPeoes().outro_jogador(jogador)] == []
##    return condicao1 or condicao2

def f_aval_funcao1(estado, jogador):
    adversario =JogoPeoes().outro_jogador(jogador)
    pontos = len(estado.board[1][jogador]) - len(estado.board[1][adversario])
    return pontos
    
def f_aval_funcao2(estado, jogador):
    
    somatorioBrancas = 0
    somatorioPretas = 0
    for (_,x) in estado.board[1]['brancas']:
        somatorioBrancas += 2**(x - 2)
    for (_,x) in estado.board[1]['pretas']:
        somatorioPretas += 2**(7 - x)
    if(len(estado.board[1]['brancas']) == 0):
        somatorioPretas = somatorioPretas / len(estado.board[1]['pretas'])
        somatorioBrancas = 0
    elif (len(estado.board[1]['pretas']) == 0):
        somatorioBrancas = somatorioBrancas / len(estado.board[1]['brancas'])
        somatorioPretas = 0

    else:
        somatorioBrancas = somatorioBrancas / len(estado.board[1]['brancas'])
        somatorioPretas = somatorioPretas / len(estado.board[1]['pretas'])
        
    return round(somatorioBrancas - somatorioPretas, 2) if jogador == 'brancas' else round(somatorioPretas - somatorioBrancas,2)


## PARA A P3 ## 
def f_aval_funcao3(estado, jogador): 
    return round(0.8 * f_aval_funcao1(estado, jogador) + 0.2 * f_aval_funcao2(estado, jogador),2)


def n_jogos(jogo,n,jogador1,jogador2):
    estados_jogos = []
    i = 0 
    tupleList = [['empate',0],[jogador1,0],[jogador2,0]]
    if jogador1 == "F1":
        jog1 = jogador_alfabeta_1
    elif jogador1 == "F2":
        jog1 = jogador_alfabeta_2
    elif jogador1 == "F3":
        jog1 = jogador_alfabeta_3
    else:
        jog1 = random_player

    if jogador2 == "F1":
        jog2 = jogador_alfabeta_1
    elif jogador2 == "F2":
        jog2 = jogador_alfabeta_2
    elif jogador2 == "F3":
        jog2 = jogador_alfabeta_3
    else:
        jog2 = random_player
        
    while i < n:
        resultado = jogo.jogar(jog1, jog2, verbose = False)
        if resultado > 0:
            tupleList[1][1] += 1
        elif resultado < 0:
            tupleList[2][1] += 1
        else:
            tupleList[0][1] += 1    
        i += 1
            
    return jogador1 if tupleList[1][1] > tupleList[2][1] else jogador2

def jogador_alfabeta_1(jogo,estado) :
    return alphabeta_cutoff_search(estado,jogo,3,eval_fn=f_aval_funcao1)

def jogador_alfabeta_2(jogo,estado) :
    return alphabeta_cutoff_search(estado,jogo,3,eval_fn=f_aval_funcao2)

def jogador_alfabeta_3(jogo,estado) :
    return alphabeta_cutoff_search(estado,jogo,3,eval_fn=f_aval_funcao3)

###########################testes###########################


###P1,P2,P3
#Parg = input()#"Coloque o estado que pretende: "
#if Parg.isdigit():
#    state = teste(int (Parg))
#else:
#    state = eval(Parg)
#pieces = input()#"pretas ou brancas: "
#print(f_aval_funcao1(state,pieces))#p1
#print(f_aval_funcao2(state,pieces))#p2
#print(f_aval_funcao3(state,pieces))#p3

#inputFuncao1 = input()
#inputFuncao2= input()
#print(n_jogos(JogoPeoes(),10,inputFuncao1,inputFuncao2))
