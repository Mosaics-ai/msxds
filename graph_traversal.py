"""
Niklaus Parcell

Graph example from: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

Depth First Search
"""

from ETL_engine import *
import pandas as pd 

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
		self.df = pd.read_csv('superstore_dataset_formattedID.csv')
		self.df = pd.DataFrame(self.df)

		self.graph = {
			"hashing" : ["binner", "null handler", "fill empties", "datepart extractor"],
			"binner" : ["hashing", "null handler", "datepart extractor"],
			"null handler" : ["hashing", "binner", "fill empties", "standardization"],
			"fill empties" : ["hashing", "binner", "null handler", "standardization", "datepart extractor"],
			"standardization" : ["binner", "null handler", "datepart extractor"],
			"datepart extractor" : ["hashing", "binner", "null handler", "standardization"]
		}

		self.graph_funcs : {
			# "hashing" : {           # Implement hashing later, 
			# 	"class" : hashing,
			# 	"func" : bin_columns,
			# },
			"binner" :{
				"class" : binner,
				"func" : bin_columns,
			},
			"null handler" : {
				"class" : null_handler,
				"func" : return_null_list,
			},
			"fill empties" : fill_empties,
			"standardization" : {
				"class" : standardization,
				"func" : normalize,
			},
			"datepart extractor" : {
				"class" : datepart_extractor,
				"func" : return_datepart_cols,
				"args" : [
					"Order Date", 
					"Ship Date",
				],
			},
		}

	def DS_topsort(self):
		"""
		Modified from above
		"""
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

	def DS_topsort_helper_func(self):

		visited[currentNode] = True
		
		for edge in self.graph[currentNode]:
			if visited[edge] == False:
				self.helperFunction(edge, visited, ordered)

		ordered.insert(0, currentNode)

		return 

if __name__ == "__main__":

	# # Standard graph traversal
	# depth_first_search().dfs('A')
	# topological_sort().topsort()

	# Test data science graph traversing
	data_science_graph().DS_sort()