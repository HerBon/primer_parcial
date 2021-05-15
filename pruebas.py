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

nodo_inicial = nodo(estado_inicial, None, None)
'''
print(nodo_inicial.buscar_moviminetos(0))
print(nodo_inicial.crear_hijos())
print(nodo_inicial.hallar_heuristica())
print(nodo_inicial.coste)
'''
'''
[0, 0], [0, 1], [1, 0]]

[[ 6, 0, 7, 8, 9],
 [ 1, 5, 2, 3, 4], 
 [10,11,12,13,14]]
 ----------------
 [[ 1, 6, 7, 8, 9],
  [ 0, 5, 2, 3, 4], 
  [10,11,12,13,14]]
'''