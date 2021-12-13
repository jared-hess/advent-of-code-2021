f = open("input", "r")

nodes = {}

class Node():
    def __init__(self, name: str) -> None:
        self.connections = set()
        self.name = name

    def is_big(self):
        return self.name.isupper()
    
    def valid_destinations(self):
        connections = self.connections.copy()
        connections.discard(nodes["start"])
        return connections

    def find_paths(self, destination: str, visited=set(), twice=False):
        local_visited = visited.copy()
        local_visited.add(self)
        # print(f"Checking node: {self.name}")
        # print([x.name for x in self.connections])
        if destination == self.name:
            print("Destination found")
            return [[self]]
        else:
            paths = []
            for connection in self.valid_destinations():
                print(f"{self.name} has connection {connection.name}")
                if connection.is_big() or (connection not in visited or not twice):
                    local_twice = twice or (not connection.is_big() and connection in visited)
                    print(local_twice)
                    connection_paths = connection.find_paths(destination=destination, visited=local_visited, twice=local_twice)
                    if connection_paths:
                        for path in connection_paths:
                            print(path)
                            paths.append([self]+path)
                else:
                    print(f"Connection {connection.name} already visited")
            return paths



    
for line in f.readlines():
    first, second = line.strip().split("-")
    if first not in nodes.keys():
        nodes[first] = Node(name=first)
    if second not in nodes.keys():
        nodes[second] = Node(name=second)
    # Add maps
    nodes[first].connections.add(nodes[second])
    nodes[second].connections.add(nodes[first])

# for key, value in nodes.items():
#     print(f"{key}, {[x.name for x in value.connections]}")
paths = nodes["start"].find_paths("end")
for path in paths:
    print([x.name for x in path])

print(len(paths))