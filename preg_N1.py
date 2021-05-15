import copy 
from time import time
from typing import Reversible

class nodo():
    def __init__(self, estado, padre, coste):
        self.estado = estado
        self.padre = padre
        self.coste = coste
    def generar_hijos(self):        
        self.hijos = []
        for c in range(len(self.estado)-1):
            hijo = copy.deepcopy(self.estado)
            hijo[c] = self.estado[c+1]
            hijo[c+1]=self.estado[c]
            self.hijos.append(hijo)
        return self.hijos
    


#nodo_inicial = nodo([2,3,5,1,4],None)
estado_inicial = [
    [5 ,6 ,7 ,8 ,9 ],
    [0 ,1 ,2 ,3 ,4 ],
    [10,11,12,13,14]
]
#print(nodo_inicial.generar_hijos())
estado_solucion = [
    [0 ,1 ,2 ,3 ,4 ],
    [5 ,6 ,7 ,8 ,9 ],
    [10,11,12,13,14]
]
'''
def buscar_en_lista(lista1, nodo):
    esta_enlista = False 
    if lista1 != []:
        for nds_enlist in lista1:
            if nds_enlist == nodo:
                esta_enlista = True
    return esta_enlista
'''
ruta_corta = []
def busca_alPadre(nodo1):
    ruta_corta.append(nodo1.estado)
    if nodo1.padre!= None:             
        busca_alPadre(nodo1.padre)
    return ruta_corta

def busqueda_anchura(estado_inicial1, estado_solucion1):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = nodo(estado_inicial1,None)
    nodos_frontera.append(nodo_raiz)
    nodos_desplegados=0
    while (not resuelto) and nodos_frontera != []:
        #en este debes ordenar la frontera osea aplicar la huristica
        nodo_actual = nodos_frontera.pop(0)
        nodos_desplegados = nodos_desplegados+1
        print(nodo_actual.estado, "desplegados =",nodos_desplegados-1)        
        if nodo_actual.estado == estado_solucion1:
            resuelto = True
            print(nodo_actual.estado, "solucion = ",nodos_desplegados-1)
            '''
            camino =list(reversed(busca_alPadre(nodo_actual))) 
            print("Ruta mas corta = ",camino)
            '''
            return nodo_actual
        else:           
            lista_hijos = copy.deepcopy(nodo_actual.generar_hijos())
            for hijo in lista_hijos:
                nodo_hijo = nodo(hijo, nodo_actual)
                if not buscar_en_lista(nodos_frontera,nodo_hijo) and not buscar_en_lista(nodos_visitados, nodo_hijo):
                    nodos_frontera.append(nodo_hijo)

t_inicio = time()
busqueda_anchura(estado_inicial,estado_solucion)
t_final = time()
print(t_final- t_inicio,"Segundos")

