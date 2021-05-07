"""
Niklaus Parcell

Define user example schema for meta-data 
"""

user = {
	"user info" : {
		"first name" : "Nik",
		"last name" : "Parcell",
		"company" : "mosaics.ai",
		"title" : "chief yeet officer and director of ML engineering",
		"sign up date" : {
			"month" : 1,
			"day" : 1,
			"year" : 2021,
		},
		"security" : "Advanced",
		"storage" : "100GB",
	},
	"account info" : {
		"tier" : "enterprise", 
		"add ons" : {
			"upgrade 1" : {
				"price" : 100,
			},
			"upgrade 2" : {
				"price" : 1000,
			},
		},
		"collaborators" : [
			"George Patterson",
		]
	},
	"graph info" : {
		"graph_1" : {
			"graph type" : "DAG",
			"traversal" : [
				"topological sorting",
				"other"
			]
		},
		"graph_2" : {
			"graph type" : "unweighted",
			"traversal" : [
				"DFS",
			],
		}
	},
}