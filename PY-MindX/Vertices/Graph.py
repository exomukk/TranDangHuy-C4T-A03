graph_sample = {"a":["c"],
                "b": ["c", "e"],
                "c": ["a", "b", "d", "e"],
                "d": ["c"],
                "e": ["c", "b"],
                "f": []
                }

class Graph:
    def __init__(self, graph_dict={}):
        self.graph_dict = graph_dict
    
    def vertices(self):
        return list(self.graph_dict.keys())

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)

        else:
            self.graph_dict[vertex1]= [vertex2]

g = Graph(graph_dict=graph_sample)

print (g.graph_dict)
