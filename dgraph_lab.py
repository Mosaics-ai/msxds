"""
Niklaus Parcell
Mosaics.ai

Objective here is to connect data to dgraph, and trigger commands from ETL external from a Python file
"""

import pydgraph

class dgraph:

    def __init__(self):

        dgraph_source = 'dgraph.mosaics.ai'
        self.client_stub = pydgraph.DgraphClientStub(dgraph_source)
        self.client = pydgraph.DgraphClient(self.client_stub)
        print("")

    def post_schema(self):
        """
        Post schema to dgraph
        """
        return

    def fetch_schema(self):
        """
        Fetch schema from dgraph
        """
        return

    def transform_schema(self):
        """
        Transfrom schema from dgraph to pandas data frame 
        """
        return

if __name__ == "__main__":

    a = dgraph()