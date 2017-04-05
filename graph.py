class Node(object):
	def __init__(self, node_id, weight, ebola_infected = False):
		self.id = node_id;
		self.weight = weight
		self.ebola_infected = ebola_infected
		self.neighbors = set()

	def add_neighbor(self, node_id):
		self.neighbors.add(node_id)


class Graph(object):
	def __init__(self, node_ids, weights):
		self.graph = {}
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
		for node_1, node_2 in connections:
			self.add_connection(node_1, node_2)

	def add_connection(self, node_1, node_2):
		if node_1 not in self.graph or node_2 not in self.graph:
			print "one of the nodes does not exist"
		else:
			self.graph[node_1].add_neighbor(node_2)
			self.graph[node_2].add_neighbor(node_1)

	def get_neighbors_and_weights_of_a_node(self, node_id):
		neighbor_and_weights = {}
		if node_id not in self.graph:
			print "node does not exist"
		else:
			for neighbor_node_id in self.graph[node_id].neighbors:
				neighbor_and_weights[neighbor_node_id] = self.graph[neighbor_node_id].weight

			return neighbor_and_weights

	def get_neighbor_objects_of_a_node(self, node_id):
		neighbor_objects = []
		if node_id not in self.graph:
			print "node does not exist"
		else:
			for neighbor_node_id in self.graph[node_id].neighbors:
				neighbor_objects.append(self.graph[neighbor_node_id])

			return neighbor_objects
