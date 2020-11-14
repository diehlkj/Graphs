from util import Stack, Queue  # * These may come in handy

# ? Simple graph implementation


class Graph:

    # ! Represent a graph as a dictionary of vertices mapping labels to edges.

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # TODO      Add a vertex to the graph.

        # ? Create a new key with its value being an empty set
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # TODO      Add a directed edge to the graph.

        # ? Add v2 to v1's set of neighbors
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # TODO      Get all neighbors (edges) of a vertex.

        # ? return the set of neighbors
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # TODO      Print each vertex in breadth-first order
        # TODO      beginning from starting_vertex.

        # ? make a queue
        q = Queue()

        # ? make a set to track which nodes we have visited
        visited = set()

        # ? enqueue the starting node
        q.enqueue(starting_vertex)

        # ? loop while the queue isn't empty
        while q.size() > 0:
            # ? dequeue, this is our current node
            current_node = q.dequeue()

            # ? check if we've yet visited
            if current_node not in visited:
                print(current_node)
            # ? if not, we go to the node
            # ? mark as visited == add to visited set
                visited.add(current_node)

            # ? get the neighbors
                neighbors = self.get_neighbors(current_node)
            # ? iterate over the neighbors, enqueue them
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # TODO      Print each vertex in depth-first order
        # TODO      beginning from starting_vertex.
                
        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            # ? pop off the top of the stack, this is our current node
            current_node = s.pop()
            
            # ? check if we have visited this node yet
            if current_node not in visited:
                print(current_node)
                # ? if not, add it our visited set
                visited.add(current_node)

                # ? and add each of its neighbors to our stack
                neighbors = self.get_neighbors(current_node)

                # ? iterate over the neighbors, stack them
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        # TODO      Print each vertex in depth-first order
        # TODO      beginning from starting_vertex.
        # TODO      This should be done using recursion.
        
        print(starting_vertex)
        visited.add(starting_vertex)
        
        neighbors = self.get_neighbors(starting_vertex)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # TODO      Return a list containing the shortest path from
        # TODO      starting_vertex to destination_vertex in
        # TODO      breath-first order.
        
        q = Queue()
        visited = set()
        # * Instead of adding the node we queue the path taken
        q.enqueue([starting_vertex])

        while q.size() > 0:
            # ? pop off the top of the stack, this is our current node
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
                    
            # ? check if we have visited this node yet
            if current_node not in visited:
                # ? if not, add it our visited set
                visited.add(current_node)
                
                # ? get its neighbors
                neighbors = self.get_neighbors(current_node)

                # ? iterate over the neighbors, enqueue path to them
                for neighbor in neighbors:
                    new_path = list(current_path) # ? Make copy of path
                    new_path.append(neighbor) # ? Append the neighbor
                    q.enqueue(new_path) # ? Add it to the queue

    def dfs(self, starting_vertex, destination_vertex):
        # TODO      Return a list containing a path from
        # TODO      starting_vertex to destination_vertex in
        # TODO      depth-first order.
        
        s = Stack()
        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:
            # ? pop off the top of the stack, this is our current node
            current_path = s.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
            
            # ? check if we have visited this node yet
            if current_node not in visited:
                # ? if not, add it our visited set
                visited.add(current_node)
                
                # ? get its neighbors
                neighbors = self.get_neighbors(current_node)

                # ? iterate over the neighbors, add them to stack if not target
                for neighbor in neighbors:
                    new_path = list(current_path) # ? Make copy of path
                    new_path.append(neighbor) # ? Append the neighbor
                    s.push(new_path) # ? Add it to the queue
                    
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        # TODO      Return a list containing a path from
        # TODO      starting_vertex to destination_vertex in
        # TODO      depth-first order.
        # TODO      This should be done using recursion.
        
        current_path = []
        
        if type(starting_vertex) is not list:
            current_path.append(starting_vertex)
        else:
            current_path.extend(starting_vertex)
            
        current_node = current_path[-1]
        
        if current_node == destination_vertex:
            print(current_path)
            return current_path
        
        elif current_node in visited:
            return
        
        else:
            visited.add(current_node)
            neighbors = self.get_neighbors(current_node)
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(current_path) # ? Make copy of path
                    new_path.append(neighbor) # ? Append the neighbor
                    
                    self.dfs_recursive(new_path, destination_vertex, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("\n\nBFT")
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n\nDFT")
    graph.dft(1)
    
    print("\n\nDFT - Recursive")
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\n\nBFS")
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\n\nDFS")
    print(graph.dfs(1, 6))
    # * print(graph.dfs_recursive(1, 6))




