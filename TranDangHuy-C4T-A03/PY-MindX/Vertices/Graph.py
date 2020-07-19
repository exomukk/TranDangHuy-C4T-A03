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

    def DFS(self, v): 
        visited = []
        self.DFSUtil(v, visited)         

    def DFSUtil(self, v, visited): 
        visited.append(v)
  
        for i in self.graph_dict[v]: 
            if i not in visited: 
                self.DFSUtil(i, visited) 
  
    def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 
bfs_shortest_path(graph, 'G', 'D')  # returns ['G', 'C', 'A', 'B', 'D']


g = Graph(graph_dict=graph_sample)

print (g.graph_dict)

print (g.DFS('a'))
print (g.BFS('a'))
