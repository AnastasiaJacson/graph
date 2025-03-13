import networkx as nx


def main():
    with open("./matrix.txt", "r") as f:
        matrix = eval(f.readline())

    graph = nx.Graph()

    for i, row in enumerate(matrix, 1):
        connections = [(i, j) for j, elem in enumerate(row, 1) if elem]
        graph.add_edges_from(connections)

    print(graph)


if __name__ == "__main__":
    main()
