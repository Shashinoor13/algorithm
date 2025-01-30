class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight

    def print_graph(self):
        for row in self.graph:
            print(row)


def travelling_salesman():
    pass

def main():
    graph = Graph()
    graph.add_edge(1,2)
    graph.add_edge(1,5)
    graph.add_edge(2,4)
    graph.add_edge(2,5)

    graph.print_graph()

main()