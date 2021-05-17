import random

individuo_perfecto =[1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1]
def decodificar(individui):
    #genera el tablero
    for f in range(0,25,6):
        print(individui[f-6:f])
'''
#decodificar(individuo_perfecto)

def crear_individuo():
    #crea un cromosoma eleaotorio
    new_ind = [random.choice(range(0,2)) for f in range(0,25)]
    return new_ind
   
def crear_poblacion(numero_de_indiv):
    #crea una poblacion aleatoria
    poblacion=[ crear_individuo() for N_ind in range(0,numero_de_indiv+1)]
    return poblacion
#print(crear_poblacion(10))
'''
def crear_fitnees(estado_ini,estado_fin):
    cont_fit= 0
    for i in range(0,25):
        if estado_ini[i]== estado_fin[i]:
            cont_fit = cont_fit +1
    return cont_fit

class clase_individuo():
    def __init__(self,estado):
        self.estado   = estado
        self.fit  = crear_fitnees(self.estado,individuo_perfecto)
        self.prob_vida=  None



nodo_indiv = clase_individuo(crear_individuo())
print(nodo_indiv.estado)
print(nodo_indiv.fitness)






# class clase_poblacion():
#     def __init__(self,estado):
#         self.estado = 



'''

101010
010101
101010
010101
'''