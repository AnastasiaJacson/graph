import re
import networkx as nx

edge_regex = re.compile(r"\[(\d+ \d+)\]")


def parse_match(match: re.Match[str]) -> tuple[int, int]:
    gr = match.groups()[0]
    ints = gr.split(" ")
    return (int(ints[0]), int(ints[1]))


def parse_graph_from_file(file_name: str) -> nx.Graph:
    with open(file_name, "r") as f:
        file_data = " ".join(f.readlines())
    edges = [parse_match(match) for match in re.finditer(edge_regex, file_data)]

    graph = nx.Graph()
    graph.add_edges_from(edges)

    return graph


def main():
    graph = parse_graph_from_file('./data.txt')

    print(graph)


if __name__ == "__main__":
    main()
