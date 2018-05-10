class HamiltonianCycle:

	def find_path(self, graph, start, end, path=[]):
		path = path + [start]
		if start == end:
			return path
		if start not in graph.keys():
			return None
		for node in graph[start]:
			if node not in path:
				new_path = self.find_path(graph, node, end, path)
				if new_path:
					return new_path
		return None

	def find_all_paths(self, graph, start, end, path=[]):
		path = path + [start]
		if start == end:
			return [path]
		if start not in graph.keys():
			return []
		paths = []
		for node in graph[start]:
			if node not in path:
				new_paths = self.find_all_paths(graph, node, end, path)
				for new_path in new_paths:
					paths.append(new_path)
		return paths
