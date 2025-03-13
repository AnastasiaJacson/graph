import networkx as nx
import numpy as np
from node_degrees import get_degrees

def get_matrix(graph: nx.Graph) -> np.ndarray:
    A = np.zeros((len(graph.nodes), len(graph.nodes)))
    for edge in graph.edges:
        A[edge[0] - 1, edge[1] - 1] = 1
        A[edge[1] - 1, edge[0] - 1] = 1

    return A


def get_laplacian(graph: nx.Graph) -> np.ndarray:
    A = get_matrix(graph)
    D = get_degrees(graph)

    L = D - A

    return L

def get_sym_laplacian(graph: nx.Graph) -> np.ndarray:
    D = get_degrees(graph)
    L = get_laplacian(graph)

    D_sqrt_inv = np.diag(1.0 / np.sqrt(np.diag(D)))
    L_sym = D_sqrt_inv @ L @ D_sqrt_inv

    return L_sym

def get_rw_laplacian(graph: nx.Graph) -> np.ndarray:
    D = get_degrees(graph)
    L = get_laplacian(graph)

    D_inv = np.diag(1.0 / np.diag(D))
    L_rw = D_inv @ L

    return L_rw
