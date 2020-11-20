from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# ? map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# ? map_file = "maps/test_loop.txt"
# ? map_file = "maps/test_loop_fork.txt"
# ! map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n', 's', 's', 'w', 'w', 'e', 'e', 'e', 'e', 'w', 'w', 's', 's']
traversal_path = []

# * Code Project Here

# ? STACK & QUEUE UTILITY CLASSES
class Queue():
    def __init__(self):
        self.queue = deque()
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.popleft()
        else:
            return None
    def size(self):
        return len(self.queue)
    
class Stack():
    def __init__(self):
        self.stack = deque()
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# ? ALL ROOMS GRAPH CLASS
class AllRooms:
    def __init__(self):
        self.room = {}
    
    # * 
    def add_room(self, room_id):
        if room_id not in self.room:
            # ? Creates Key for Room ID
            self.room[room_id] = {}
            
            # ? Populate Room ID's possible exits as 'cardnial': None (until explored)
            for cardinal in player.current_room.get_exits():
                self.room[room_id][cardinal] = None
    
    def update_exit(self, room_id, cardinal, connection_id):
        if self.room[room_id][cardinal] is None:
            self.room[room_id][cardinal] = connection_id
    
    # * DFT until no exits other than previous room
    # * Append the direction moved to traversal path each time
    def dft(self, room_id, cardinal, target_mode = False, path = []):
        # ? if self.room.length != world.room_graph.length:
            # ? if not target_mode:

            # ? if target_mode:
        
        pass
    # * DFT (with n > e > s > w priority) until dead end, return the route taken and append it to traversal_path.
    # * THEN
    # * DFT (with n > e > s > w priority) in 'target mode' to first node with an unexplored cardinal.
        # ? In 'target mode', the DFT may explore multiple routes that lead to a target. Because of this, the paths taken must be returned and compared before final return and appending to traversal_path.
        # ? Once target node is found, repeat loop until graph len is equal to 'world len(room_graph)'            

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


player.current_room.print_room_description(player)
print(player.current_room.id)
print(player.current_room.get_exits())
# ? player.travel('n', True)
player.travel('n', True)


#######!
#! UNCOMMENT TO WALK AROUND
#######!

# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
