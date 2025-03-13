from collections.abc import Callable
from read_edges import parse_graph_from_file
import networkx as nx


def bfs(root_node: int, graph: nx.Graph, callback: Callable[[int, nx.Graph], None]) -> None:
    visited_ids = [root_node]
    queue = [root_node]

    while any(queue):
        node = queue.pop(0)
        callback(node, graph)

        non_visited_children = [c for c in graph[node].keys() if c not in visited_ids]
        visited_ids += non_visited_children
        queue += non_visited_children


def main():
    graph = parse_graph_from_file("./data.txt")

    bfs(1, graph, lambda x, _: print(x))


if __name__ == "__main__":
    main()
