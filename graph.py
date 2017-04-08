import random

class Node(object):
    def __init__(self, node_id, weight, ebola_infected = False, vaccinated = False):
        self.id = node_id;
        self.weight = weight
        self.ebola_infected = ebola_infected
        self.vaccinated = vaccinated
        self.neighbors = set()

    def add_neighbor(self, node_id):
        self.neighbors.add(node_id)

    def is_infected(self):
        return self.ebola_infected

    def is_vaccinated(self):
        return self.vaccinated

    def make_infected(self):
        if self.ebola_infected or self.vaccinated: 
            print "node already infected or vaccinated"
        else:
            self.ebola_infected = True

    def get_neighbor_node_ids(self):
        return self.neighbors

    def vaccinate_node(self):
        if self.vaccinated or self.ebola_infected:
            print "node already vaccinated or infected"
        else:
            self.vaccinated = True


class Graph(object):
    def __init__(self, node_ids, weights):
        # structure of graph {node_id: node_object, ...}
        self.graph = {}
        self.vaccinated_node_ids = []
        self.add_nodes(node_ids, weights)
        first_infected_node_id = random.choice(self.graph.keys())
        self.graph[first_infected_node_id].make_infected()
        self.infected_node_ids = [first_infected_node_id]

    def add_nodes(self, node_ids, weights):
        for node_id, weight in zip(node_ids, weights):
            self.add_node(node_id, weight)

    def add_node(self, node_id, weight):
        if node_id in self.graph:
            print "node already exists"
        else:
            new_node = Node(node_id, weight)
            self.graph[node_id] = new_node

    def get_infected_nodes(self):
        return self.infected_node_ids

    def add_connections(self, connections):
        for node_1_id, node_2_id in connections:
            self.add_connection(node_1_id, node_2_id)

    def add_connection(self, node_1_id, node_2_id):
        if node_1_id not in self.graph or node_2_id not in self.graph:
            print "one of the nodes does not exist"
        else:
            self.graph[node_1_id].add_neighbor(node_2_id)
            self.graph[node_2_id].add_neighbor(node_1_id)

    def get_neighbors_and_weights_of_a_node(self, node_id):
        neighbor_and_weights = {}
        if node_id not in self.graph:
            print "node does not exist"
        else:
            for neighbor_node_id in self.graph[node_id].get_neighbor_node_ids():
                neighbor_and_weights[neighbor_node_id] = self.graph[neighbor_node_id].weight

            return neighbor_and_weights

    def get_neighbor_objects_of_a_node(self, node_id):
        neighbor_objects = []
        if node_id not in self.graph:
            print "node does not exist"
        else:
            for neighbor_node_id in self.graph[node_id].get_neighbor_node_ids():
                neighbor_objects.append(self.graph[neighbor_node_id])

            return neighbor_objects

    def get_neutral_neighbor_ids_of_a_node(self, node_id):
        neutral_neighbor_ids = []
        if node_id not in self.graph:
            print "node does not exist"
        else:
            for neighbor_node_id in self.graph[node_id].get_neighbor_node_ids():
                if not self.graph[neighbor_node_id].is_infected() and not self.graph[neighbor_node_id].is_vaccinated():
                    neutral_neighbor_ids.append(neighbor_node_id)

            return neutral_neighbor_ids

    def vaccinate_node(self, node_id):
        if node_id not in self.graph:
            print "node does not exist"
        else:
            self.vaccinated_node_ids.append(node_id)
            self.graph[node_id].vaccinate_node()

    def get_nodes_that_will_be_infected_in_next_step(self):
        """Gets the node objects to which the infection will spread in the next
        round. We have to select one node out of these to vaccinate."""

        nodes_that_will_be_infected = {}
        for infected_node_id in self.infected_node_ids:
            neighbor_ids_of_infected_node = self.get_neutral_neighbor_ids_of_a_node(infected_node_id)
            for neighbor_id in neighbor_ids_of_infected_node:
                if neighbor_id not in nodes_that_will_be_infected:
                    nodes_that_will_be_infected[neighbor_id] = self.graph[neighbor_id]

        return nodes_that_will_be_infected

    def play_one_step(self, vaccinate_node_id):
        """One step of the game proceeds. The node id given is vaccinated
        and the infection spreads to all the neighboring nodes."""
        nodes_about_to_be_infected = []
        self.vaccinate_node(vaccinate_node_id)
        for infected_node_id in self.infected_node_ids:
            neutral_neighbor_ids = self.get_neutral_neighbor_ids_of_a_node(infected_node_id)
            for neutral_neighbor_node_id in neutral_neighbor_ids:
                if neutral_neighbor_node_id not in nodes_about_to_be_infected:
                    nodes_about_to_be_infected.append(neutral_neighbor_node_id)

        for node_id in nodes_about_to_be_infected:
            if node_id not in self.infected_node_ids:
                self.infected_node_ids.append(node_id)
                self.graph[node_id].make_infected()


# Tutorial
node_ids = [1, 2, 3, 4, 5]
weights = [10, 20, 30, 40, 50]

# initialize a graph - the first infected node is randomly chosen.
graph = Graph(node_ids, weights)

# get the id of the first infected node.
first_infected_node = graph.get_infected_nodes()[0]
print first_infected_node

# connections between nodes
connections = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 5), (2, 5)]

# create connections
graph.add_connections(connections)

# get the ids of the nodes which will be infected in the next turn
# graph.get_nodes_that_will_be_infected_in_next_step() returns the objects
# of the nodes that will be infected.
print [node_id for node_id in graph.get_nodes_that_will_be_infected_in_next_step()]

# out of the list of node ids returned above, we choose one node to vaccinate.
# Chinu, Darshan will write the algo here.
# For now choosing 1 if it is not the first infected node. If it is, choosing 2.
# play_one_step will first vaccinate the given node id and then the infection will
# spread to the neighboring nodes.
if first_infected_node != 1:
    graph.play_one_step(1)
else:
    graph.play_one_step(2)

# get the nodes infected after above step.
print graph.get_infected_nodes()

# now which nodes will be effected. We have to choose one out of these to vaccinate.
print [node_id for node_id in graph.get_nodes_that_will_be_infected_in_next_step()]
