# Graph structure with simulated probability edge weights
weighted_graph = {
    'db1' : {
        'db2' : 0.1,
        'db3' : 0.5,
        'db4' : 0.2,
    },
    'db2' : {
        'db1' : 0.1,
        'db3' : 0.8,
        'db4' : 0,
    },
    'db3' : {
        'db1' : 0.5,
        'db2' : 0.8,
        'db4' : 0.1,
    },
    'db4' : {
        'db1' : 0.2,
        'db2' : 0,
        'db3' : 0.1,
    }
}

# Traversal
def traverse(graph, start):
    
    # Return path
    return_path = []
    
    print(max(graph[start], key = graph.get))
    
    # return sorted list of possible db nodes
    return 


    
if __name__ == "__main__":
    
    traverse(graph, 'db1')

