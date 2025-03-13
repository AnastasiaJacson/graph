import networkx as nx
import numpy as np

def sorenson(graph: nx.Graph) -> np.ndarray:
    sorenson: list[list[float]] = [[0.0] * len(graph.nodes) for _ in range(len(graph.nodes))]
    for i in range(1, len(graph.nodes) + 1):
        for j in range(i+1, len(graph.nodes) + 1):
            intersection = len(set(graph[i].keys()).intersection(set(graph[j].keys())))
            sorenson[i-1][j-1] = 2 * intersection / (len(graph[i]) + len(graph[j]))

    for i in range(len(graph.nodes)):
        for j in range(i):
            sorenson[i][j] = sorenson[j][i]

    return np.array(sorenson)

def salton(graph: nx.Graph) -> np.ndarray:
    salton: list[list[float]] = [[0.0] * len(graph.nodes) for _ in range(len(graph.nodes))]
    for i in range(1, len(graph.nodes) + 1):
        for j in range(i+1, len(graph.nodes) + 1):
            intersection = len(set(graph[i].keys()).intersection(set(graph[j].keys())))
            salton[i-1][j-1] = 2 * intersection / np.sqrt(len(graph[i]) * len(graph[j]))

    for i in range(len(graph.nodes)):
        for j in range(i):
            salton[i][j] = salton[j][i]

    return np.array(salton)

def jaccard(graph: nx.Graph) -> np.ndarray:
    jaccard: list[list[float]] = [[0.0] * len(graph.nodes) for _ in range(len(graph.nodes))]
    for i in range(1, len(graph.nodes) + 1):
        for j in range(i+1, len(graph.nodes) + 1):
            intersection = len(set(graph[i].keys()).intersection(set(graph[j].keys())))
            union = len(set(list(graph[i].keys()) + list(graph[j].keys())))
            jaccard[i-1][j-1] = intersection / union

    for i in range(len(graph.nodes)):
        for j in range(i):
            jaccard[i][j] = jaccard[j][i]

    return np.array(jaccard)
