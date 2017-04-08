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
		if self.ebola_infected == True:
			print "node already infected"
		else:
			self.ebola_infected = True

	def get_neighbor_node_ids(self):
		return self.neighbors

	def vaccinate_node(self):
		if self.vaccinated == True:
			print "node already vaccinated"
		else:
			self.vaccinated = True


class Graph(object):
	def __init__(self, node_ids, weights):
		# structure of graph {node_id: node_object, ...}
		self.graph = {}
		self.infected_node_ids = []
		self.vaccinated_node_ids = []
		self.add_nodes(node_ids, weights)

	def add_nodes(self, node_ids, weights):
		for node_id, weight in zip(node_ids, weights):
			self.add_node(node_id, weight)

	def add_node(self, node_id, weight):
		if node_id in self.graph:
			print "node already exists"
		else:
			new_node = Node(node_id, weight)
			self.graph[node_id] = new_node

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

	def vaccinate_node(self, node_id):
		if node_id not in self.graph:
			print "node does not exist"
		else:
			graph[node_id].vaccinate_node()



# Tutorial
node_ids = [1, 2, 3, 4]
weights = [10, 20, 30, 40]

# initialize a graph
graph = Graph(node_ids, weights)

# connections given
connections = [(1, 2), (2, 3), (3, 4), (1, 3)]

# create connections
graph.add_connections(connections)

# get the neighbors of node 1 along with weights
# returns {2: 20, 3: 30}
print graph.get_neighbors_and_weights_of_a_node(1)

# get the neighbor objects of node 2
neighbor_objects = graph.get_neighbor_objects_of_a_node(2)

# print the ids of the nodes connected to 2
# returns [1, 3]
print [x.id for x in neighbor_objects]
