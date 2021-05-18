import random
import copy

la_solucion_1 =[1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1]

def crear_poblacion1(): # crea la poblacion inicial
    poblacion_ini =[]
    for f in range(0,32):
        new_ind = [random.choice(range(0,2)) for c in range(0,32)]
        poblacion_ini.append(new_ind)
    return poblacion_ini
    
def crear_fitnees(indiv_inicial,la_solucion_1):
    cont_fit= 0
    for i in range(0,32):
        if indiv_inicial[i] == la_solucion_1[i]:
            cont_fit = cont_fit+1
    return cont_fit

def cruza(pobalcion_seccionada):
    poblacion_cruzada =[]
    for cromosomas, estado_fisico, probailidad_morir in pobalcion_seccionada:
        poblacion_cruzada.append(cromosomas)
    for i in range(0,31):
        l1 = poblacion_cruzada[i]
        l2 = poblacion_cruzada[i+1]
        l3 = l1[:17] + l2[17:32]
        poblacion_cruzada[i] = l3       
    return poblacion_cruzada
def mutar(pobalcion_que_cruzo):
    pobalcion_mutatada = copy.deepcopy(pobalcion_que_cruzo)
    if random.randint(0, 9) == 5:
        for f in range(len(pobalcion_que_cruzo)):
            for c in range(len(pobalcion_que_cruzo)):
                if random.randint(0, 9) == 5:
                    pobalcion_mutatada[f][c] = random.randint(0,1)
    return pobalcion_mutatada           

class poblacion ():
    def __init__(self, estado_pobla):
        self.estado_pobla = estado_pobla
        self.fitness_pobla = []  # [[individio, fisnes,proba_vi],[individio, fisnes, proba_vi],....]
        self.fitness_total = 0
        for i in self.estado_pobla:
            encontar_fit = crear_fitnees(i,la_solucion_1)
            self.fitness_total = self.fitness_total + encontar_fit
            self.fitness_pobla.append([i,encontar_fit])
       
        for num in range(0,32):
            prob_fit_1 = (self.fitness_pobla[num][1])/self.fitness_total
            self.fitness_pobla[num].append(prob_fit_1) 

        self.depues_de_seccion = None

    def seleccionar_mejore_sujetos(self):#Selleccion
        el_master = copy.deepcopy(self.fitness_pobla)
        el_master = sorted(el_master, key = lambda x: x [2]) # ordena tomado e referencia al tercer valor(0,1,2)
        #de la matrz, ordema de menor a mayor
        el_master.pop(0)# quito el menor
        copiar_mejor = copy.deepcopy(el_master[len(el_master)-1])
        el_master.append(copiar_mejor)# agrego el mejor de nuevo
        #----------------------------------      
        cruzamineto = cruza(el_master)
        #----------------------------------
        mutacion_pobla = mutar(cruzamineto)

        self.depues_de_seccion = el_master 
        return mutacion_pobla

def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def principal(poblacio_final):
    poblacion_nn = poblacion(poblacio_final)
    poblacion_gen1 = copy.deepcopy(poblacion_nn.seleccionar_mejore_sujetos())
    print("-----------------------")
    for indiv in poblacion_gen1:
        print(indiv)
        if indiv == la_solucion_1:
            print("elresultado es:",binario_a_decimal(indiv))
            exit()
    principal(poblacion_gen1)
principal(crear_poblacion1())

'''
for i in poblacion1.estado_pobla:
    print(i)

for l,j,h in poblacion1.fitness_pobla:
    print(h, j)
print(poblacion1.fitness_total) 

print(poblacion1.seleccionar_mejore_sujetos())
'''