class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # ? Create a new key with its value being an empty set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # ? Add v2 to v1's set of neighbors
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # ? return the set of neighbors
        return self.vertices[vertex_id]

    def dft_recursive(self, node, depth=0, ancestors=()):

        parents = self.get_neighbors(node)

        if len(parents) == 0:
            return (node, depth)

        eldest_vertex = (node, depth)

        for parent in parents:
            node_pair = self.dft_recursive(parent, depth + 1, eldest_vertex)

            if node_pair[1] > depth:
                if node_pair[1] > eldest_vertex[1]:
                    eldest_vertex = node_pair
                elif node_pair[1] == eldest_vertex[1]:
                    if node_pair[0] < eldest_vertex[0]:
                        eldest_vertex = node_pair

        return eldest_vertex


def earliest_ancestor(ancestors, starting_node):
    aGraph = Graph()

    for rel in ancestors:
        aGraph.add_vertex(rel[0])
        aGraph.add_vertex(rel[1])

    for rel in ancestors:
        aGraph.add_edge(rel[1], rel[0])

    eldest = aGraph.dft_recursive(starting_node)
    if eldest[1] == 0:
        return -1
    else:
        return eldest[0]

    # ? Find starting node in list of ancestors
    # ? Find its parent
    # ? Repeat until there are no more parents
    # queue = []
    # previous_parent = None
    # earliest = -1

    # for ancestor in ancestors:
    #     if ancestor[1] == starting_node:
    #         queue.append(ancestor)

    # print("queue before loop:", queue)

    # while len(queue) > 0:
    #     print("\nqueue in loop:", queue)

    #     current_tup = queue.pop(0)
    #     print("current_tup", current_tup)

    #     previous_parent = earliest
    #     earliest = current_tup[0]
    #     print("earliest", earliest)

    #     #

    #     for ancestor in ancestors:
    #         if ancestor[1] == current_tup[0]:
    #             queue.append(ancestor)

    #     print("queue len after pop", len(queue))

    #     if len(queue) == 0:
    #         if current_tup[0] > previous_parent and previous_parent >= 0:
    #             earliest = previous_parent
    #             print("I FLIPPED", earliest)

    # print("END:", earliest)
    # return earliest

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 6)
