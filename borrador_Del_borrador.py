'''
l1 = [(1,2,3), (3,1,1), (8,5,3), (3,4,2)] 

# Encontrar el elemento más grande / más pequeño basado en el segundo elemento de la tupla. 
# La función lambda devuelve el segundo elemento en la tupla
print(l1)
print (sorted(l1, key = lambda x: x [1])) 
#Output: (3, 1, 1)
'''
li = ["a","b","c","d","g"]
l2 = ["a","f","h","t","k","a"]
l3 = li[:2] + l2[:7]

print(l3)
