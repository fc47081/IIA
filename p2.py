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


## PARA A P4 ##  
def f_aval_funcao3(estado, jogador):
    return round(0.5 * f_aval_funcao1(estado, jogador) + 0.5 * f_aval_funcao2(estado, jogador),2)

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
        resultado = jogo.jogar(jog1, jog2)
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


##def test(n):
##    estado1 = GameState(to_move='brancas', utility=0, board=(0,
##    {'brancas': [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],'pretas': [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)]}),
##    moves=[('avança', (1, 2)), ('avança', (2, 2)), ('avança', (3, 2)), ('avança', (4, 2)), ('avança', (5, 2)), ('avança', (6, 2)), ('avança', (7, 2)), ('avança', (8, 2))])
##
##    estado2 = GameState(to_move='brancas',utility=0,board=(19,
##    {'brancas': [(2,4),(4,4),(5,5),(8,3)],'pretas':[(2,5),(3,6),(4,5),(6,5),(7,2),(8,6)]}),
##    moves=[('avança',(5,5)),('avança',(8,3))])
##    
##    estado3 = GameState(to_move='brancas',utility=0,board=(19,
##    {'brancas': [(1,2),(2,3),(3,5),(4,3),(5,2),(7,3),(8,2),(8,6)],'pretas':[(1,6),(2,7),(3,6),(4,4),(5,6),(6,7)]}),
##    moves=[('avança',(1,6)),('avança',(2,7)),('avança',(5,6)),('avança',(6,7))])
##    
##    if (n == '1'):
##        return estado1
##    elif (n == '2'):
##        return estado2
##    elif (n == '3'):
##        return estado3


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
