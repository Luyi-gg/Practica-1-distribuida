## Alumnos
- Ana Lilia Carballido Camacateco 315314601
- Emilio Romero Concha 112001065
- Luis Angel Santiago Cruz 318243038

## Instrucciones 
Puedes modificar el archivo *arbol.txt* para cambiar la estructura del arbol.

La estrura es la siguiente: el primer numero es el nodo padre, los siguientes son sus hijos.

Para correr el algoritmo, ejecutar _BFSE.py_; te pedirá que ingreses el nodo por el que quieres emepezar, y el programa imprime los nodos visitados 
    
## Reporte

### Nuestro código para el algoritmo BFS se divide en las siguientes partes:
* El paquete _queue_ viene importado, ya que usamos colas en la ejecución del algoritmo.
* Función **leer_grafica(nombre_archivo)**, que sirve para leer un archivo de texto e interpretarlo como una gráfica, tal que:
  * Cada línea de texto es un vértice.
  * El primer caracter de la línea es el índice o nombre del vértice
  * Los siguientes, separados por espacios, representan su lista de vecinos.
  * El archivo que nuestro código busca se llama "arbol.txt", y se encuentra en la carpeta superior a _BFSE.py_.
* La función **bfs(grafica, nodo_inicio)**, que ejecuta bfs dada una gráfica y un vértice inicial que le damos en la ejecución.
* La definición de _nodo_inicio_, _resultado_, y una línea para imprimir el el resultado de la ejecución. Estas son como tomamos el vértice inicial durante la ejecución, llamamos a bfs con esta entrada, y le mostramos al usuario el fin del algoritmo.
    
### El algoritmo BFS lo definimos de la siguiente manera:
Primeramente, definimos como variables de la función la cola, llamada _cola_, de BFS, que mantiene el orden en que exploramos las ramas de la gráfica para explorar los vecinos exhaustivamente, la lista "visitados" de vértices que mantiene dónde hemos terminado para asegurarnos de no continuar la ejecución sobre un vértice que ya habíamos pasado, y una lista _bfs_resultado_, donde guardamos la lista de vértices que forman el camino más corto desde la raíz hasta las hojas, que es lo que se devuelve al final de la ejecución.

El algoritmo se puede implementar recursivamente sobre los vértices para no requerir una cola, pero decidimos que sería mejor hacerlo iterativo porque las estructuras outplace nos ayudan mucho a guardar información que no queríamos tener que vigilar en llamadas recursivas.

Obviamente, antes que nada, agregamos el vértice inicial sobre _cola_ y _visitados_.

El resto del algoritmo se ejecuta sobre un ciclo while que itera sobre los elementos de la cola; de esta forma podemos agregar vértices conforme vayamos encontrando hijos no explorados, y quitar los padres cuando hayamos concluido de explorar sus hijos. Por ser una cola, siempre trabajamos con el orden en que agregamos los elementos y nos aseguramos de que no se regrese a los padres hasta que hayamos finalizado con todos sus niveles inferiores, y concluímos la ejecución ya que hayamos eliminado (o sea, explorado), cada vértice en la gráfica.

Mientras _cola_ sea no vacía:

* Tomamos el elemento actual de la cola, que denotamos _nodo_actual_ y lo agregamos a la lista _bfs_resultado_, porque es el siguiente vértice en el camino desde la raíz.
* Hacemos un barrido de todos los vecinos de _nodo_actual_, y corroboramos con nuestra lista _visitados_ cuáles de ellos ya hemos explorado.
  * Si un vecino ya lo hemos explorado, lo saltamos.
  * Si un vecino no ha sido explorado, lo agregamos a _cola_, para que este se explore en una siguiente iteración del while, y lo agregamos a _visitados_, para no volver a él.
  
  Al concluír el ciclo, ya hemos agregado todos los vértices de la gráfica a nuestra lista _bfs_resultado_ tal que están en orden de camino más corto de la raíz a las hojas. Como nuestro código _BFSE_ ejecuta el algoritmo sobre un print, devuelve en terminal el resultado.