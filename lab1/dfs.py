from collections.abc import Callable
from read_edges import parse_graph_from_file
import networkx as nx

def dfs(node: int, graph: nx.Graph, callback: Callable[[int, nx.Graph], None], visited_ids: list[int]=[]) -> None:
    callback(node, graph)
    visited_ids += [node]
    for child in graph[node].keys():
        if child not in visited_ids:
            dfs(child, graph, callback, visited_ids)
            visited_ids.append(child)


def main():
    graph = parse_graph_from_file('./data.txt')

    dfs(1, graph, lambda x, _: print(x))

if __name__ == '__main__':
    main()
