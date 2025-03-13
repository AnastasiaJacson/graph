from collections.abc import Callable
from read_edges import parse_graph_from_file
import networkx as nx


def bfs(
    root_node: int, graph: nx.Graph, callback: Callable[[int, nx.Graph], None]
) -> tuple[dict[int, int], dict[int, int]]:
    queue = [root_node]
    dist = {i: -1 for i in range(1, len(graph.nodes) + 1)}
    parent = {i: -1 for i in range(1, len(graph.nodes) + 1)}
    dist[root_node] = 0

    while any(queue):
        node = queue.pop(0)
        callback(node, graph)

        for neighbor in graph[node].keys():
            if dist[neighbor] != -1:
                continue
            dist[neighbor] = dist[node] + 1
            parent[neighbor] = node
            queue.append(neighbor)

    return dist, parent


def main():
    graph = parse_graph_from_file("./data.txt")

    src = 17
    dest = 19

    dist, parent = bfs(src, graph, lambda x, _: None)

    path = []
    curr = dest
    while curr != src:
        path.append(curr)
        curr = parent[curr]

    path = [src] + list(reversed(path))

    print('dist:', dist[dest], ';', 'path:', path)


if __name__ == "__main__":
    main()
