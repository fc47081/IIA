from search import *
from math import *
#from copy import *

class Estadotabuleiro:


#--------------------------------Funcoes base--------------------------------#
    def __init__(self,t):
        self.t = t

    def __str__(self):
        return str(self.t)

    def __eq__(self,estado):
        return self.t == estado.t

    def __hash__(self):
        ta = 0
        for i in range (0,len(self.t)):
            ta += hash(self.t[i])
        return ta
    #REDIFINIR O LT
    def __lt__(self, node):
        return True
#--------------------------------Checks para movimentar--------------------------------#      
    def checkEsq(self):
        czero = self.checkZero()
        if czero[1] > 0 and czero[1] <= len(self.t[0])-1:
            return True
        return False
    
    def checkDir(self):
        czero = self.checkZero()
        if czero[1] >= 0 and czero[1] < len(self.t[0])-1:
            return True
        return False
           
    def checkCima(self):
        czero = self.checkZero()
        if czero[0] > 0:
          return True
        return False
        
    def checkBaixo(self):
        czero = self.checkZero()
        if czero[0] <  len(self.t[0])-1:
          return True
        return False
        
    def checkZero(self):
        linhas = -1
        colunas = -1
        for i in range(0, len(self.t)):
            for j in range(0,len(self.t[0])):
              if (self.t[i][j] == 0):
                linhas = i
                colunas = j
        return (linhas,colunas)

#--------------------------------Movimentaçoes cima , baixo , esq, dir--------------------------------#

    def converterTuplo(self,lista):
        return tuple(tuple(i) for i in lista)
    
    def converterLista(self):
        return list(list(i) for i in self.t)
        
    def moveEsq(self):
        newt = self.converterLista()
        posAnterior = 0
        if self.checkEsq() == True:
            posZero = self.checkZero()
            posEsq = (posZero[0],posZero[1]-1)
            posAnterior = newt[posEsq[0]][posEsq[1]]
            newt[posEsq[0]][posEsq[1]] = 0
            newt[posZero[0]][posZero[1]] = posAnterior
        return self.converterTuplo(newt)

    def moveDir(self):
        newt = self.converterLista()
        posAnterior = 0
        if self.checkDir() == True:
            posZero = self.checkZero()
            posDir =(posZero[0],posZero[1]+1)
            posAnterior = newt[posDir[0]][posDir[1]]
            newt[posDir[0]][posDir[1]] = 0
            newt[posZero[0]][posZero[1]] = posAnterior
        return self.converterTuplo(newt)
    
    def moveCima(self):
        newt = self.converterLista()
        posAnterior = 0
        if self.checkCima() == True:
            
            posZero = self.checkZero()
            posCima =(posZero[0]-1,posZero[1])
            posAnterior = newt[posCima[0]][posCima[1]]
            newt[posCima[0]][posCima[1]] = 0
            newt[posZero[0]][posZero[1]] = posAnterior           
        return self.converterTuplo(newt)

    
    def moveBaixo(self):
        newt = self.converterLista()
        posAnterior = 0
        if self.checkBaixo() == True:
            posZero = self.checkZero()
            posBaixo =(posZero[0]+1,posZero[1])
            posAnterior = newt[posBaixo[0]][posBaixo[1]]
            newt[posBaixo[0]][posBaixo[1]] = 0
            newt[posZero[0]][posZero[1]] = posAnterior
        return self.converterTuplo(newt)
    
#--------------------------------Definiçao do problema--------------------------------#

class ProblemaPuzzle(Problem):

    #CONSTRUTOR
    def __init__(self,t):
        super().__init__(t)
        self.initial = t

    
#--------------------------------Goal_test--------------------------------#           
    def goal_test(self,estado):
        listaconcat = []
        listatuplo = []
        for i in range(0, len(estado.t)):
            listaconcat.append(list(estado.t[i]))
        #print(listaconcat)
        boolean = True
        for j in range(0,len(listaconcat)):
            listatuplo += listaconcat[j]
        for k in range(len(listatuplo)-1):
            if listatuplo[k] != k+1:
                boolean = False
        return boolean

    
#--------------------------------Actions--------------------------------#
    def actions(self,estado) :
        action = list()
        if estado.checkEsq():
            action.append("mover para a esquerda")
        if estado.checkDir():
            action.append("mover para a direita")
        if estado.checkCima():
            action.append("mover para a cima")
        if estado.checkBaixo():
            action.append("mover para baixo")
        return action

#--------------------------------Result--------------------------------#
    def result(self, estado, accao) :
        lista=[]
        if accao == "mover para a esquerda":
            lista = Estadotabuleiro(estado.moveEsq())
        elif accao == "mover para a direita":
            lista = Estadotabuleiro(estado.moveDir())
        elif accao == "mover para a cima":
            lista = Estadotabuleiro(estado.moveCima())
        elif accao == "mover para baixo":
            lista = Estadotabuleiro(estado.moveBaixo())
        else:
            raise "Existe accao nao reconhecida"
        return lista
        
#--------------------------------Heuristicas + distanciaDeManhatan-------------------------------#
    def h1(self,no) : 
        lista=[]
        contador = 0
        for i in range(0, len(no.state.t)):
            lista +=no.state.t[i]
        for j in range(0, len(lista)-1):
            if lista[j] != j+1:
                contador+=1
        return contador

    def distanciaDeManhatan(self,estado,pos):
        linha = pos[0]
        col = pos[1]
        size = len(estado.t)
        return abs(linha - ((estado.t[linha][col]-1)//size)) + abs (col - ((estado.t[linha][col]-1)% size))
               
    def h2(self,no) : 
        contador = 0
        for i in range(0, len(no.state.t)):
           for j in range(0, len(no.state.t)):
               if no.state.t[i][j] != 0:
                   contador += self.distanciaDeManhatan(no.state,(i,j))
        return contador
         

#--------------------------------MAIN-------------------------------#

#LER INPUT
size = input()
m = []
tuploM = ()
for i in range(int(sqrt(int(size) + 1))):
    lista1 = input()
    lista2 = (lista1.split())
    m.append(list(map(int, lista2)))
for j in range(0, len(m)):
    tuploM +=(tuple(m[j]),)
    
#INCIALIZAR
tab = Estadotabuleiro(tuploM)
problem = ProblemaPuzzle(tab)
estado = Node(tab)

#####P1#####
#print(problem.h1(estado))
#print(problem.h2(estado))
#####P1#####

#####P2#####
#cost = uniform_cost_search(problem)
#print(cost.path_cost)
#####P2#####

#####P3#####
#astar1 = astar_search(problem,problem.h1)
#aastar2 = astar_search(problem,problem.h2)
#print(astar1.path_cost)
#print(astar2.path_cost)
#####P3#####

#####P4#####
#astar1 = astar_search(problem,problem.h1)
#astar2 = astar_search(problem,problem.h2)
#print(astar1.path_cost)
#print(astar2.path_cost)
#####P4#####
