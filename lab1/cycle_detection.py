from typing import Optional
from read_edges import parse_graph_from_file
import networkx as nx

def dfs(node: int, graph: nx.Graph, path: list[int]) -> Optional[list[int]]:
    for neighbor in graph[node].keys():
        if neighbor in path and len(path) > 2:
            return path + [neighbor]

        if neighbor not in path:
            path.append(neighbor)
            return dfs(neighbor, graph, path)
        
    return None


def main():
    graph = parse_graph_from_file('./data.txt')

    src = 1

    path = dfs(src, graph, [src])

    print(path)

if __name__ == '__main__':
    main()
