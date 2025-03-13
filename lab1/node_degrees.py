import networkx as nx
import numpy as np

def get_degrees(graph: nx.Graph) -> np.ndarray:
    degrees = {node: len(graph[node]) for node in graph.nodes}
    D = np.zeros(((len(graph.nodes)), len(graph.nodes)), dtype=np.int32)
    for k, v in degrees.items():
        D[k-1,k-1] = v

    return D
