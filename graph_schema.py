"""
Niklaus Parcell

example graph schema
"""

graph = {
	"db1" : {
		"connections" : {
			"db2" : {
				"weight" : 0.8,
				"direction" : "both",
				"added" : "",
				"modified" : "",
			},
			"db3" : {
				"weight" : 0.1,
				"direction" : "to",
				"added" : "",
				"modified" : "",
			},
		},
	},
	"db2" : {
		"connections" : {
			"db1" : {
				"weight" : 0.8,
				"direction" : "both",
				"added" : "",
				"modified" : "",
			},
		},	
	},
	"db3" : {
		"connections" : {
			"db1" : {
				"weight" : 0.8,
				"direction" : "from",
				"added" : "",
				"modified" : "",
			}
		},
	}
}