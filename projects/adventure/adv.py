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
# ? map_file = "maps/test_cross.txt"
# ? map_file = "maps/test_loop.txt"
# ? map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# * ==================================================== Code Project Here vv

# ? ALL ROOMS GRAPH CLASS
class AllRooms:
    def __init__(self):
        self.room = {}
        self.path = []

    # * add_room() adds rooms and creates available unvisited exits
    def add_room(self, room_id):
        if room_id not in self.room:
            # ? Creates Key for Room ID
            self.room[room_id] = {}

            # ? Populate Room ID's possible exits as 'cardnial': None (until explored)
            for cardinal in player.current_room.get_exits():
                self.room[room_id][cardinal] = None
                
    # * update_exits() handles connections between rooms
    def update_exits(self, curr_room_id, cardinal, prev_room_id):
        # ? Sets connection for room we traveled from
        if self.room[prev_room_id][cardinal] is None:
            self.room[prev_room_id][cardinal] = curr_room_id

        # ? Sets connection for room we advanced to. Checks directions because the link will be opposite the cardinal
        if cardinal == "n":
            if self.room[curr_room_id]["s"] is None:
                self.room[curr_room_id]["s"] = prev_room_id

        if cardinal == "e":
            if self.room[curr_room_id]["w"] is None:
                self.room[curr_room_id]["w"] = prev_room_id

        if cardinal == "s":
            if self.room[curr_room_id]["n"] is None:
                self.room[curr_room_id]["n"] = prev_room_id

        if cardinal == "w":
            if self.room[curr_room_id]["e"] is None:
                self.room[curr_room_id]["e"] = prev_room_id

    # * get_complete_path() is a somewhat unique approach to recursive DFT
    # * Instead of recursing at every connected edge, it continue to explore
    # * with a directional priority, keeping track of movement along the way, and
    # * stops when it encounters the end of a branching. This is where it 
    # * calls on find_unvisited() to do a DFS for
    # * a path to a vert with an unexplored edge.

    def get_complete_path(self, prev_room_id=None, cardinal=None, path=[]):

        # ! prev_room_id: ID of the room traveled from
        # ! cardinal: Direction traveled from previous room to current
        # ! path: Cumulative path from initial room to current.
        # ! This gets appened to self.path when a dead end is encountered

        if len(self.room) != len(room_graph):
            inner_path = [*path]
            curr_room_id = player.current_room.id
            # ? Add current room to graph
            self.add_room(curr_room_id)

            # ? If previous room, update it and current room connections
            if prev_room_id is not None:
                self.update_exits(curr_room_id, cardinal, prev_room_id)

            # ? exits will be gotten in self.add_room(), check them here for status and existance
            # ? if exits:
                # ? Travel in clockwise priority unless already visited
                # ? append movement to path
                # ? recurse
            # ? else:
                # ? return path and begin search for incomplete links

            if "n" in self.room[curr_room_id] and self.room[curr_room_id]["n"] is None:
                player.travel("n")
                inner_path.append("n")
                self.get_complete_path(curr_room_id, "n", inner_path)

            elif "e" in self.room[curr_room_id] and self.room[curr_room_id]["e"] is None:
                player.travel("e")
                inner_path.append("e")
                self.get_complete_path(curr_room_id, "e", inner_path)

            elif "s" in self.room[curr_room_id] and self.room[curr_room_id]["s"] is None:
                player.travel("s")
                inner_path.append("s")
                self.get_complete_path(curr_room_id, "s", inner_path)

            elif "w" in self.room[curr_room_id] and self.room[curr_room_id]["w"] is None:
                player.travel("w")
                inner_path.append("w")
                self.get_complete_path(curr_room_id, "w", inner_path)
            # ? If all exits are visited, return path and search for unvisited.
            else:
                if len(self.room) == len(room_graph):
                    self.path.extend(path)
                    return path
                else:
                    next_unvisited = self.find_unvisited(
                        player.current_room, set(), [])
                    if next_unvisited:
                        inner_path.extend(next_unvisited)
                        self.get_complete_path(None, None, inner_path)

        else:
            # ? Returns self.path if all rooms have been fully explored
            self.path.extend(path)
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", self.path)
            return path

    def find_unvisited(self, starting_room, visited=set(), path=[]):
        inner_path = [*path]
        curr_room = starting_room
        curr_room_id = curr_room.id

        if curr_room_id in visited:
            return

        else:
            visited.add(curr_room_id)
            # ? Checks if room has unexplored exits
            for cardinal in self.room[curr_room_id]:
                if self.room[curr_room_id][cardinal] is None:
                    # ? Sets player location to room with unvisited
                    player.current_room = starting_room
                    return path

            for cardinal in self.room[curr_room_id]:
                updated_inner_path = [*inner_path]      # ? Make copy of path

                next_room = curr_room.get_room_in_direction(
                    cardinal)  # ? Get next room

                # ? Update the path for movement
                updated_inner_path.append(cardinal)

                recursion = self.find_unvisited(
                    next_room, visited, updated_inner_path)

                if recursion:
                    return recursion                # ? Returns the movement path taken


# * Get the complete, walkable path to all rooms
complete_path = AllRooms()
complete_path.get_complete_path()
traversal_path = complete_path.path

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


player.current_room.print_room_description(player)


# !
# ! UNCOMMENT TO WALK AROUND
# !

# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
