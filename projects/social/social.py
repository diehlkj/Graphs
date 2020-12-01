import random
from collections import deque

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    
    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]
            
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0        # Number of users in total
        self.users = {}         # users names, attributes, etc.
        self.friendships = {}   # adjacency list

        # ? Add users
        for user in range(num_users):
            self.add_user(user)
            
        # ? Create friendships
        total_friendships = avg_friendships * num_users
        
        # ? friendship must be index 1 > index 0. Not the other way around because both directions are connected by default.
        friendship_combos = []

        # ? Create all friendship combos without redundants
        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))
        
        # ? shiffle list
        self.fisher_yates_shuffle(friendship_combos)
        
        # ? Grab first N elements of shuffled list
        friendships_to_make = friendship_combos[:(total_friendships // 2)]
        
        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])
    
    def get_friends(self, current_friend):
        return self.friendships[current_friend]
    
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        # * Hint 1: What kind of graph search guarantees you a shortest path?
        
        
        # * Hint 2: Instead of using a `set` to mark users as visited, you could use a `dictionary`.
        # * Similar to sets, checking if something is in a dictionary runs in O(1) time.
        # * If the visited user is the key, what would the value be?
        
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        q = Queue()
        visited = {}
        
        q.enqueue([user_id])

        while q.size() > 0:
            # ? get next person in line
            current_path = q.dequeue()
            current_person = current_path[-1]
                    
            # ? check if we have visited them yet
            if current_person not in visited:
                # ? if not, add it our visited set
                visited[current_person] = current_path
                
                # ? Get their friends
                friends = self.get_friends(current_person)

                for friend in friends:
                    friend_path = [*current_path] # * [*'list name'] unpacks 'list name' into a new list making a copy
                    
                    friend_path.append(friend)
                    
                    q.enqueue(friend_path)
                    
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
