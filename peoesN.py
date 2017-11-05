#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:58:50 2017

@author: balsaj
"""

"""
IIA 17/18
Jogo dos Peões - N
"""

from jogos_iia import *
from copy import deepcopy
from functools import reduce


class JogoPeoes(Game) :
    """Representação para o jogo:
    Vamos assumir um tabuleiro com as coordenadas numeradas da seguinte forma:
    Exemplo de tabuleirto inicial para 8x8:
         
       8 . . . . . . . .
       7 p p p p p p p p
       6 . . . . . . . .
       5 . . . . . . . .
       4 . . . . . . . .
       3 . . . . . . . .
       2 b b b b b b b b 
       1 . . . . . . . . 
         a b c d e f g h (interacção)
         1 2 3 4 5 6 7 8 (interno)
         
    O tabuleiro é representado como um dicionário no qual as chaves são os 
    jogadores ('brancas' ou 'pretas') e os valores as coordenads das peças
    respectivas (coluna,linha).
    """
    jogadores = ['brancas','pretas']
    sentido = {'brancas':1,'pretas':-1}
    
    def outro_jogador(self,j) :
        return 'brancas' if j == 'pretas' else 'pretas'
    
    def __init__(self, linhas = 8, colunas = 8) :
        """Requires: número de linhas e número de colunas
        linhas > 4
        Assume-se 2 e 7 como linhas iniciais de 'brancas' e 'pretas',
        respectivamente
        """
        self.linhas = linhas # número de linhas
        self.cols = colunas   # número de colunas
        self.objectivo = {'brancas':self.linhas,'pretas':1}
        brancas_inic = [(x,2) for x in range(1,colunas+1)]
        pretas_inic = [(x,7) for x in range(1,colunas+1)]
        tabuleiro_inicial = {'brancas':brancas_inic,'pretas':pretas_inic}
        movs_possiveis = self.movimentos_possiveis(tabuleiro_inicial,self.jogadores[0])
        self.initial = GameState(
            to_move = self.jogadores[0],
            utility = 0,
            board = (0,tabuleiro_inicial), # (numero de jogadas,tabuleiro)
            moves = movs_possiveis)

       
    def movimentos_possiveis(self,tabuleiro,jogador) :
        """Três tipos de movimentos:
        - avança - ('avança',(x,y)) - avança a peça (x,y)
        - come-esq - ('come-esq',(x,y)) - peça (x,y) come à esquerda
        - come-dir - ('come-dir',(x,y)) - peça (x,y) come à direita
        """
        def frente_livre(tab,peca,jog) :
            pecas_todas = tab['brancas']+tab['pretas']
            x = peca[0]
            y = peca[1]+self.sentido[jog]
            return (1 <= y <= self.linhas) and (x,y) not in pecas_todas

        def pode_comer_esq(tab,peca,jog) :
            x = peca[0]-self.sentido[jog]
            y = peca[1]+self.sentido[jog]
            return (x,y) in tab[self.outro_jogador(jog)]

        def pode_comer_dir(tab,peca,jog) :
            x = peca[0]+self.sentido[jog]
            y = peca[1]+self.sentido[jog]
            return (x,y) in tab[self.outro_jogador(jog)]
        
        pecas = tabuleiro[jogador]
        movs = list()
        for p in pecas :
            if frente_livre(tabuleiro,p,jogador) :
                movs.append(("avança",p))
            if pode_comer_esq(tabuleiro,p,jogador) :
                movs.append(("come-esq",p))
            if pode_comer_dir(tabuleiro,p,jogador) :
                movs.append(("come-dir",p))
        return movs
        
        
    def actions(self,state) :
        return state.moves
    
    def result(self,state,move) :
        """
        Requires: 'move' é uma jogada válida no estado dado ('state')
        """
        accao,peca = move
        jogador = state.to_move
        adversario = self.outro_jogador(jogador)
        num_jogadas = state.board[0]
        tabuleiro = deepcopy(state.board[1])
        tabuleiro[jogador].remove(peca)
        if accao == 'avança' :
            x = peca[0]
            y = peca[1]+self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
        elif accao == 'come-esq' :
            x = peca[0]-self.sentido[jogador]
            y = peca[1]+self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
            tabuleiro[adversario].remove((x,y))
        else : # come-dir
            x = peca[0]+self.sentido[jogador]
            y = peca[1]+self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
            tabuleiro[adversario].remove((x,y))
        
        novo_board = (num_jogadas+1,tabuleiro)
        proximo = self.outro_jogador(jogador)
        movimentos = self.movimentos_possiveis(tabuleiro,proximo)
        utilidade = self.calcular_utilidade(proximo,tabuleiro,movimentos)
            
        estado = GameState(to_move = proximo,
                           board = novo_board,
                           moves = movimentos,
                           utility = utilidade)
        return estado

    
    def calcular_utilidade(self,jogador,tabuleiro,movimentos) :
        def objectivo(linha,jogador) :
            return linha in [y for (_,y) in tabuleiro[jogador]]
        
        utilidade = 0
        adversario = self.outro_jogador(jogador)
        if objectivo(self.objectivo[jogador],jogador) \
           or tabuleiro[adversario] == [] :
            utilidade = 1
        elif objectivo(self.objectivo[adversario],adversario) \
             or tabuleiro[jogador] == [] \
             or movimentos == []:
            utilidade = -1
        
        return utilidade
    
    def utility(self, state, player):
        return self.calcular_utilidade(player,state.board[1],state.moves)
    
    def terminal_test(self,state) :
        return state.moves == [] or any([self.utility(state,x) != 0 for x in self.jogadores])

    def display(self, state):
        print(state)
        linha = [chr(x) for x in range(ord('a'),self.cols + ord('a'))]
        board = state.board[1]
        print("Tabuleiro actual: ({})".format(state.board[0]))
        for y in range(self.linhas,0,-1):
            print(y,end=' ')
            for x in range(1, self.cols + 1):
                if (x,y) in board['brancas'] :
                    print('O', end=' ')
                elif (x,y) in board['pretas'] :
                    print('*', end=' ')
                else :
                    print('.',end=' ')
            print()
        print(reduce(lambda acc,x : acc+' '+x,linha,' '))

        if self.terminal_test(state) :
            print("FIM do Jogo")
        else :
            print("Próximo jogador:{}\n".format(state.to_move))
    
     
def teste(n) :
    if n == 1 :
        g = JogoPeoes()
        estado = g.initial
    elif n == 2 :
        estado =GameState(
                to_move='brancas',
                utility=0,
                board=(0, 
                       {'brancas': [(2, 4), (4,4), (5,5), (8, 3)], 
                        'pretas': [(2, 5), (3, 6), (4, 5), (6, 5), (7, 2), (8, 6)]}),
                moves=[('avança', (5, 5)), ('avança', (8, 3))])
    elif n == 3 :
        estado =GameState(
                to_move='pretas',
                utility=0,
                board=(19, 
                       {'brancas': [(1, 2), (2,3), (3,5), (4, 3), (5,2), (7, 3), (8,2), (4, 6)], 
                        'pretas': [(1,6), (2,7), (3, 6), (4, 4), (5,6), (6,7)]}),
                moves=[('avança', (1, 6)), ('avança', (2, 7)), 
                       ('avança', (5, 6)), ('avança', (6, 7))])
    else :
        raise Exception("Estado não definido")
    return estado


