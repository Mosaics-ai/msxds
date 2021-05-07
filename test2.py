"""
Niklaus Parcell

Graph example from: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

Depth First Search
"""

class depth_first_search:
	
	def __init__(self):
		self.graph = {
			'A' : ['B','C'],
			'B' : ['D', 'E'],
			'C' : ['F'],
			'D' : [],
			'E' : ['F'],
			'F' : []
		}

		self.visited = set() # Set to keep track of visited nodes.

	def dfs(self, node):
		if node not in self.visited:
			print (node)
			self.visited.add(node)
			for neighbour in self.graph[node]:
				self.dfs(neighbour)

class topological_sort:
	
	def __init__(self):

		self.graph = {}

if __name == "__main__":
	depth_first_search().dfs('A')