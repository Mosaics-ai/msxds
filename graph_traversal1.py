"""
Niklaus Parcell

Graph example from: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

Depth First Search
"""

from ETL_engine import *
import pandas as pd 
import os

class colors:
	RED = "\033[91m"
	BLUE = "\033[94m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	END = "\033[0m"

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
		
		global ordered

		self.graph = {
			"A" : ["D"],
			"B" : ["D"],
			"C" : ["A", "B"],
			"D" : ["G", "H"],
			"E" : ["A", "D", "F"],
			"F" : ["K"],
			"G" : ["I"],
			"H" : ["I", "J"],
			"I" : ["L"],
			"J" : ["L", "M"],
			"K" : ["J"],
			"L" : [],
			"M" : [],
		}
		self.edges = [edge for edge in self.graph]

	def helperFunction(self, currentNode, visited, ordered):
		visited[currentNode] = True
		
		for edge in self.graph[currentNode]:
			if visited[edge] == False:
				self.helperFunction(edge, visited, ordered)

		ordered.insert(0, currentNode)

	def topsort(self):

		N = len(self.graph)
		visited = {}
		for node in self.graph:
			visited[node] = False
		ordered = []

		for node in self.graph:
			if visited[node] == False:
				self.helperFunction(node, visited, ordered)

		print(ordered)
		return ordered

class data_science_graph:

	def __init__(self):

		# commenting data filter out for now because it isn't built
		# "data filter" : ["hashing", "binner", "null handler", "fill_empties", "standardization", "datepart extractor"],

		# What will be used in Mosaics workspace
		# self.df = minio_connect().get_df(
        # 	csvName = 'superstore_dataset_formattedID.csv'
    	# )	

		# Use this block for testing
		self.df = pd.read_csv(os.getcwd() + "/test datasets/" + 'superstore_dataset_formattedID.csv')
		self.df = pd.DataFrame(self.df)

		self.graph = {
			# "hashing" : ["binner", "null handler", "fill empties", "datepart extractor"],
			"binner" : [
				# "hashing", 
				"null handler", "datepart extractor"],
			"null handler" : [
				# "hashing", 
				"binner", "fill empties", "standardization"],
			"fill empties" : [
				# "hashing", 
				"binner", "null handler", "standardization", "datepart extractor"],
			"standardization" : ["binner", "null handler", "datepart extractor"],
			"datepart extractor" : [
				# "hashing", 
				"binner", "null handler", "standardization"]
		}

		# self.graph_funcs = {
		# 	# "hashing" : {           # Implement hashing later, 
		# 	# 	"class" : hashing,
		# 	# 	"func" : bin_columns,
		# 	# },
		# 	"binner" :{
		# 		"class" : binner,
		# 		"func" : bin_columns,
		# 	},
		# 	"null handler" : {
		# 		"class" : null_handler,
		# 		"func" : return_null_list,
		# 	},
		# 	"fill empties" : {
		# 		"class" : fill_empties,
		# 		"func" : iterate_cols,
		# 	},
		# 	"standardization" : {
		# 		"class" : standardization,
		# 		"func" : normalize,
		# 	},
		# 	"datepart extractor" : {
		# 		"class" : datepart_extractor,
		# 		"func" : return_datepart_cols,
		# 		"args" : [
		# 			"Order Date", 
		# 			"Ship Date",
		# 		],
		# 	},
		# }

		# Use something like : https://stackoverflow.com/questions/45710181/how-can-i-check-if-a-class-has-been-instantiated-in-python
		# >> to check if class is instantiated, if it is, then call the function. 
		# This is a new concept for me, so see how it goes

		self.visited = []
		self.N = 0

	def DS_dfs(self, node):

		self.N += 1
		if node not in self.visited:
			self.visited.append(node)
			for neighbor in self.graph[node]:
				self.DS_dfs(node = neighbor)

		return self.visited

	def DS_dfs_w_funcs(self, node):

		self.N += 1
		if node not in self.visited:
			self.visited.append(node)
			noded = self.graph_funcs[node]
			class_name = noded["class"](self.df)
			self.df = class_name.noded["func"](return_type = "data frame")
			for neighbor in self.graph[node]:
				self.DS_dfs_w_funcs(node = neighbor)

		return self.visited

	def DS_bfs(self, start):

		visited, queue = [], [start]
		N = 0
		while queue:
			vertex = queue.pop(0)
			for neighbor in self.graph[vertex]:
				if neighbor not in visited:
					visited.append(neighbor)
					queue.append(neighbor)
			N += 1
		print(N)
		print(visited)
		return visited

	def tests_0(self):
		"""
		Test individual functions on their own
		Test viability of BFS 
		"""
		start = "standardization"
		visited = self.DS_dfs(start)
		print(self.N)
		print(visited)

	def tests_1(self):
		"""
		Seeing how ordering changes in a BFS across different start nodes
		"""
		edges_to_test = [edge for edge in self.graph]
		for edge in edges_to_test:
			self.N = 0
			self.visited = []
			print(colors.BLUE + edge + colors.END)
			# self.DS_bfs(edge)
			visited = self.DS_dfs(edge)
			print(self.N)
			print( visited)

	def tests_2(self):
		"""
		This one tests different starts, and ordering of data cleaning functions
		"""
		edges_to_test = [edge for edge in self.graph]
		for edge in edges_to_test:
			self.N = 0
			self.visited = []
			print(colors.BLUE + edge + colors.END)
			visited = self.DS_dfs_w_funcs(edge)
		return

if __name__ == "__main__":

	# # Standard graph traversal
	# depth_first_search().dfs('A')
	# topological_sort().topsort()

	# Test data science graph traversing
	data_science_graph().tests_1()