class HamiltonianCycle:

	def __init__(self, graph):
		self.__graph = graph

	def find_path(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return path
		if start not in self.__graph.keys():
			return None
		for node in self.__graph[start]:
			if node not in path:
				new_path = self.find_path(node, end, path)
				if new_path:
					return new_path
		return None

	def find_all_paths(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return [path]
		if start not in self.__graph.keys():
			return []
		paths = []
		for node in self.__graph[start]:
			if node not in path:
				new_paths = self.find_all_paths(node, end, path)
				for new_path in new_paths:
					paths.append(new_path)
		return paths

	def find_shortest_path(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return path
		if start not in self.__graph.keys():
			return None
		shortest = None
		for node in self.__graph[start]:
			if node not in path:
				new_path = self.find_shortest_path(node, end, path)
				if new_path:
					if not shortest or len(new_path) < len(shortest):
						shortest = new_path
		return shortest
