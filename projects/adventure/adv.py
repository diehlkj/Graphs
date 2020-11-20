from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
    def dft(self, room_id):
        pass
    
    # * BFT back to first room with an unexplored exit
    # ? For the traversl paths, check previous graph project for how to return the path taken from starting node to target. Use this to append the whole path taken instead of one move at a time.
    # ? The 'target' of the BFT will be the first room found with a 'None' value on a cardinal key
    def bft(self, room_id):
        pass
            



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
