class Nodo: # La clase Nodo sirve para representar cada nodo en el grafo
    def __init__(self, valor):
        self.valor = valor # Valor unico
        self.vecinos = set() # Nodos vecinos conectados entre si


def busqueda_a_profundidad(nodos, aristas): # Funcion que toma como parametros los nodos y aristas
    grafo = {valor: Nodo(valor) for valor in nodos} # Crea un diccionario para el valor de los nodos y las instancias de la clase

    for borde in aristas: #Se agregan conexiones entre los nodos correspondientes al diccionario
        nodo1, nodo2 = borde
        grafo[nodo1].vecinos.add(nodo2)
        grafo[nodo2].vecinos.add(nodo1)

    return grafo # Retorna el grafo


def grafos_conexos(grafo): # Toma como entrada el grafo creado con la función anterior
    visitados = set() # Inicializa un conjunto de nodos visitados
    nodos_conexos = [] # Inicializa una lista de listas para almacenar los nodos de cada componente conexo

    def dfs(nodo_actual, componente): # Funcion para encontrar componentes conexos en el grafo
        visitados.add(nodo_actual)
        componente.append(nodo_actual)

        for vecino in grafo[nodo_actual].vecinos: # Itera sobre todos los nodos del grafo
            if vecino not in visitados:
                dfs(vecino, componente)

    for nodo in grafo: # Agrega todos los nodos de su componente conexo al conjunto visitados y a la lista de nodos
        if nodo not in visitados:
            componente_conexa = []
            dfs(nodo, componente_conexa)
            nodos_conexos.append(componente_conexa)

    return nodos_conexos # Retorna nodos están conexos entre si


nodos = list(range(50)) # Nodos dentro de una lista del 0 al 49
# nodos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)
aristas = [ # Aristas
    (0, 29), (0, 46), (0, 21), (0, 14), (0, 38), (0, 31),
    (1, 41), (1, 31), (1, 21), (1, 17), (2, 9), (2, 26),
    (2, 5), (2, 25), (2, 4), (3, 18), (3, 30), (3, 47),
    (4, 28), (4, 9), (4, 8), (5, 44), (5, 12), (6, 37),
    (6, 10), (7, 23), (7, 22), (7, 39), (9, 19), (9, 28),
    (9, 27), (11, 33), (13, 25), (13, 38), (13, 29), (14, 26),
    (14, 28), (14, 39), (15, 22), (15, 31), (15, 19), (15, 41),
    (16, 46), (16, 26), (16, 38), (16, 27), (17, 40), (17, 29),
    (18, 45), (18, 42), (18, 35), (18, 33), (18, 47), (20, 36),
    (20, 49), (20, 42), (22, 26), (22, 34), (23, 31), (23, 32),
    (23, 40), (24, 31), (24, 44), (25, 38), (26, 31), (27, 32),
    (29, 48), (29, 41), (30, 47), (30, 37), (33, 36), (33, 49),
    (34, 48), (35, 45), (36, 45), (37, 49), (37, 45), (37, 47),
    (38, 41), (40, 48), (41, 44), (42, 49), (43, 48), (45, 47)
]

grafo = busqueda_a_profundidad(nodos, aristas) # Construye el grafo

conexos = grafos_conexos(grafo) # Encuentra los nodos conexos en el grafo

print("Grafos No conexos")
for n, componente in enumerate(conexos, 1): # Imprime todos los nodos están conexos entre si
    print("Agrupacion {}: {}".format(n, componente))
