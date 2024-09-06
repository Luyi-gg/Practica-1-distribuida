# practica 1
import queue

# Función para leer la gráfica desde un archivo
def leer_grafica(nombre_archivo):
    # Inicializar la gráfica vacia 
    grafica = {}
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer cada linea del archivo
        for linea in archivo:
            # Separar el nodo de los vecinos
            nodo, *vecinos = linea.strip().split()
            # Convertir los vecinos a una lista
            grafica[nodo] = vecinos

    return grafica

#Nombre del archivo en donde esta el arbol 
nombre_archivo = "arbol.txt"

# creamos una grafica con la funcion leer_grafica
grafica = leer_grafica(nombre_archivo)

# Funcion BFS
def bfs(grafica, nodo_inicio):
    # Inicialización de cola y lista de visitados y resultado.
    cola = queue.Queue()
    visitados = set()
    bfs_resultado = []
    
    # Encolamos el nodo de inicio
    cola.put(nodo_inicio)
    # Marcamos el nodo de inicio como visitado
    visitados.add(nodo_inicio)

    # Mientras la cola no este vacia
    while not cola.empty():
        # Obtenemos el nodo actual
        nodo_actual = cola.get()
        # Agregamos el nodo actual al resultado
        bfs_resultado.append(nodo_actual)
        # Recorremos los vecinos del nodo actual
        for vecino in grafica.get(nodo_actual, []):
            # Si el vecino no ha sido visitado
            if vecino not in visitados:
                # Encolamos el vecino
                cola.put(vecino)
                # Marcamos el vecino como visitado
                visitados.add(vecino)
    # regresamos el resultado
    return bfs_resultado

# Ingresar el nodo de inicio
nodo_inicio = input("Ingrese el nodo de inicio para el BFS: ")

# Realizar el BFS
resultado = bfs(grafica, nodo_inicio)

# Imprimir el resultado
print("Resultado del BFS:", resultado)