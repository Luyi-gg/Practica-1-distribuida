import queue

grafica = {
  'A' : ['B','C', 'D', 'E'],
  'B' : ['A', 'C', 'G'],
  'C' : ['A', 'B', 'D'],
  'D' : ['H', 'E', 'A', 'C'],
  'E' : ['A', 'D', 'F'],
  'F' : ['G', 'E', 'H', 'I'],
  'G' : ['F', 'B'],
  'H' : ['F', 'D'],
  'I' : ['F']
}

#Inicialización de cola y lista de visitados y resultado.
cola = queue.Queue()
visitados = []
bfs_resultado = []

# Funcion que indica si el elemento ya fue visitado
def visitado(nodo):
    return nodo in visitados
    

# BFS algorithm
def bfs(grafica, nodo_inicio):
    cola.put(nodo_inicio)                 
    visitados.append(nodo_inicio)          
    
    while not cola.empty():
        nodo_actual = cola.get()           
        bfs_resultado.append(nodo_actual)
        
        for vecino in grafica[nodo_actual]:
            if not visitado(vecino):
                cola.put(vecino)     
                visitados.append(vecino) 

    return bfs_resultado
    

# Llamamos a la funcion bfs
resultado = bfs(grafica, 'A')
print(resultado)
