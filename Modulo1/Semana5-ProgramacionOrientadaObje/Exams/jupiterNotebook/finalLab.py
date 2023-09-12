#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        if connection_id in self.connections:
            del self.connections[connection_id]
        """Closes a connection on this server."""
        # Remove the connection from the dictionary

    def load(self):
        """Calculates the current load for all connections."""
        total = sum(self.connections.values())
        # Add up the load for each of the connections
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())






#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        if connection_id in self.connections:
            server = self.connections[connection_id]
            server.close_connection(connection_id)
            del self.connections[connection_id]
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        total_load = sum(server.load() for server in self.servers)
        num_servers = len(self.servers)
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        return total_load / num_servers if num_servers > 0 else 0

    def ensure_availability(self):
        if self.avg_load() > 50:
            new_server = Server()
            self.servers.append(new_server)
        """If the average load is higher than 50, spin up a new server"""

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

l = LoadBalancing()
for connection in range(20):
    l.add_connection(connection)
print(l)
print(l.avg_load())




