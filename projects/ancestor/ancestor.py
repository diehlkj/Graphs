
def earliest_ancestor(ancestors, starting_node):
    # ? Find starting node in list of ancestors
    # ? Find its parent
    # ? Repeat until there are no more parents
    queue = []
    previous_parent = None
    earliest = -1
    
    for ancestor in ancestors:
        if ancestor[1] == starting_node:
            queue.append(ancestor)
    
    # print("queue before loop:", queue)
    
    while len(queue) > 0:
        print("\nqueue in loop:", queue)
        
        current_tup = queue.pop(0)
        print("current_tup", current_tup)
        
        previous_parent = earliest
        earliest = current_tup[0]
        print("earliest", earliest)
        
        
        
        for ancestor in ancestors:
            if ancestor[1] == current_tup[0]:
                queue.append(ancestor)
        
        print("queue len after pop", len(queue))
        
        if len(queue) == 0:
            if current_tup[0] > previous_parent and previous_parent >= 0:
                earliest = previous_parent
                print("I FLIPPED", earliest)
        
    print("END:", earliest)
    return earliest

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 6)
