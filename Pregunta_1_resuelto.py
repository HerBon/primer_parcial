import copy 
from time import time
from typing import Reversible
from math import sqrt

estado_solucion = [
    [0 ,1 ,2 ,3 ,4 ],
    [5 ,6 ,7 ,8 ,9 ],
    [10,11,12,13,14]
]
estado_inicial =  [
    [1 ,2 ,3 ,4, 0 ],
    [5 ,6 ,7 ,8 ,9 ],
    [10,11,12,13,14]
]
def encontar_posicion(estado_pos, elemto):
    for f in range(3):
        for c in range(5):
            if estado_pos[f][c] == elemto:
                return f,c

def devolver_majathan(estado_ini, estado_sol):
    contador_mahatan = 0
    for i in range (0,15):
        f_ini,c_ini = encontar_posicion(estado_ini,i)
        f_sol,c_sol = encontar_posicion(estado_sol,i)
        contador_mahatan = contador_mahatan + (abs(f_sol - f_ini) + abs(c_sol - c_ini ))
    return contador_mahatan
        
def hamingb (estado_ini, estado_sol):
    k = 1
    for f in range(3):
        for c in range(5):
            if estado_ini[f][c] != estado_sol[f][c]:
                k = k+1
    return k

class nodo():
    def __init__(self, estado, padre):
        self.estado = estado
        self.padre = padre
        self.costoso = devolver_majathan(self.estado, estado_solucion) + hamingb(self.estado, estado_solucion)
        
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

def buscar_en_lista(lista1, nodo):
    esta_enlista = False 
    if lista1 != []:
        for nds_enlist in lista1:
            if nds_enlist == nodo:
                esta_enlista = True
                return esta_enlista
    

def Comparar(nodo):
    return nodo.costoso

def busqueda_a_star(estado_inicial1, estado_solucion1):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = nodo(estado_inicial1, None)   
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and nodos_frontera != []:
        #en este debes ordenar la frontera osea aplicar la huristica+
        print("frontera sin orden f = g + h =",nodos_frontera[0].costoso)
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        print("frontera con orden f = g + h =",nodos_frontera[0].costoso)
        nodo_actual = nodos_frontera.pop(0)
        print("--------------------")
        for f in nodo_actual.estado:           
            print(f)
        print("--------------------")
        nodos_visitados.append(nodo_actual)
        if nodo_actual.estado == estado_solucion1:
            resuelto = True
            return nodo_actual
        else:           
            lista_hijos = copy.deepcopy(nodo_actual.crear_hijos())
            #print(lista_hijos)
            for hijo in lista_hijos:
                #print(hijo)                
                nodo_hijo = nodo(hijo, nodo_actual)
                #print(nodo_hijo.costoso)
                if not buscar_en_lista(nodos_frontera,nodo_hijo) and not buscar_en_lista(nodos_visitados, nodo_hijo):
                    nodos_frontera.append(nodo_hijo)
                
                                   
t_inicio = time()
busqueda_a_star(estado_inicial,estado_solucion)
t_final = time()
print(t_final- t_inicio," Segundos ")