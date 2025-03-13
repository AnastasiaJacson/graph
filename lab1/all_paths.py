from read_edges import parse_graph_from_file
import networkx as nx
from copy import copy


def find_all_paths(
    src: int, dest: int, length: int, graph: nx.Graph
) -> list[list[int]]:
    result: list[list[int]] = []

    def dfs(node: int, graph: nx.Graph, path: list[int]):
        if len(path) == length + 1:
            if node == dest:
                result.append(copy(path))
            return

        for neighbor in graph[node].keys():
            if len(path) < length + 1:
                path.append(neighbor)
                dfs(neighbor, graph, path)
                path.pop(-1)

    dfs(src, graph, [src])

    return result


def main():
    graph = parse_graph_from_file("./data.txt")

    src = 1
    dest = 19
    length = 3

    paths = find_all_paths(src, dest, length, graph)
    print(paths)


if __name__ == "__main__":
    main()
