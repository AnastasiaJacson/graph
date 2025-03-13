import re
from read_edges import parse_match, edge_regex


def main():
    with open("./data.txt", "r") as f:
        file_data = " ".join(f.readlines())

    edges = [parse_match(match) for match in re.finditer(edge_regex, file_data)]

    all_nodes = set([e[0] for e in edges] + [e[1] for e in edges])
    n = len(all_nodes)

    matrix = [[False] * n for _ in range(n)]

    for edge in edges:
        matrix[edge[0] - 1][edge[1] - 1] = True
        matrix[edge[1] - 1][edge[0] - 1] = True

    print(matrix)


if __name__ == "__main__":
    main()
