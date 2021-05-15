import copy 
from time import time
from typing import Reversible
from math import sqrt

class nodo():
    def __init__(self, estado, padre, coste):
        self.estado = estado
        self.padre = padre
        self.coste = coste    

    def buscar_moviminetos(self,origen1):
        list_x_yposNew = []
        for f in range(3):
            for c in range(5):
                if self.estado[f][c] == origen1:
                    pos_0 = copy.deepcopy([f,c])
                    list_x_yposNew.append(pos_0)
                    if (c+1)<5:
                        list_x_yposNew.append([f,c+1])
                    if (c-1)>=0:
                        list_x_yposNew.append([f,c-1]) 
                    if (f+1)<3:
                        list_x_yposNew.append([f+1,c])
                    if (f-1)>=0:
                        list_x_yposNew.append([f-1,c])
        return list_x_yposNew  

    def crear_hijos(self):
        direciones_De_0 = self.buscar_moviminetos(0)
        x,y = direciones_De_0.pop(0)
        hijos = []
        for f,c in direciones_De_0:
            hijo = copy.deepcopy(self.estado)
            hijo[x][y] = copy.deepcopy(self.estado[f][c])
            hijo[f][c] = copy.deepcopy(self.estado[x][y])
            hijos.append(hijo)
        return hijos

    def hallar_heuristica(self):
        nodo_solcucion = nodo(estado_solucion,None, 0)
        heuristica= 0
        for i in range(15):
            x_nodo,y_nodo = self.buscar_moviminetos(i).pop(0)    
            x_sol,y_sol = nodo_solcucion.buscar_moviminetos(i).pop(0)
            heuristica =  heuristica + sqrt((abs(x_sol - x_nodo ))**2 + (abs(y_sol - y_nodo))**2) 
        self.coste =heuristica      
        return heuristica

estado_inicial = [
    [0 ,6 ,7 ,8 ,9 ],
    [1 ,5 ,2 ,3 ,4 ],
    [10,11,12,13,14]
]
estado_solucion = [
    [0 ,1 ,2 ,3 ,4 ],
    [5 ,6 ,7 ,8 ,9 ],
    [10,11,12,13,14]
]
#nodo_inicial = nodo(estado_inicial, None, None)
'''
print(nodo_inicial.buscar_moviminetos(0))
print(nodo_inicial.crear_hijos())
print(nodo_inicial.hallar_heuristica())
print(nodo_inicial.coste)
'''
def buscar_en_lista(lista1, nodo):
    esta_enlista = False 
    if lista1 != []:
        for nds_enlist in lista1:
            if nds_enlist == nodo:
                esta_enlista = True
    return esta_enlista


def Comparar(nodo):
    return nodo.coste

def busqueda_anchura(estado_inicial1, estado_solucion1):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = nodo(estado_inicial1,None,None)
    nodo_raiz.hallar_heuristica()
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and nodos_frontera != []:
        #en este debes ordenar la frontera osea aplicar la huristica
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.estado == estado_solucion1:
            resuelto = True
            print(nodo_actual.estado)
            return nodo_actual
        else:           
            lista_hijos = copy.deepcopy(nodo_actual.crear_hijos())
            print(lista_hijos)
            for hijo in lista_hijos:
                print(hijo)
                
                nodo_hijo = nodo(hijo, nodo_actual, None)
                nodo_hijo.hallar_heuristica()
                print(nodo_hijo.coste)

                if not buscar_en_lista(nodos_frontera,nodo_hijo) and not buscar_en_lista(nodos_visitados, nodo_hijo):
                    nodos_frontera.append(nodo_hijo)
                    
        

t_inicio = time()
busqueda_anchura(estado_inicial,estado_solucion)
t_final = time()
print(t_final- t_inicio," Segundos ")