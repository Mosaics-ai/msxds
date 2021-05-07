"""
Niklaus Parcell


Some notes and goals:
1) Want to use ariadne to be able to query graphql from a python script.
2) Maybe use graphene to be able to save pandas dataframe -> graphql structure
"""

class colors:
	RED = "\033[91m"
	BLUE = "\033[94m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	END = "\033[0m"

# from ariadne import QueryType, gql, make_executable_schema
# from ariadne.asgi import GraphQL

# type_defs = gql("""
#     type Query {
#         hello: String!
#     }
# """)

# # Create type instance for Query type defined in our schema...
# query = QueryType()

# # ...and assign our resolver function to its "hello" field.
# @query.field("hello")
# def resolve_hello(_, info):
#     request = info.context["request"]
#     user_agent = request.headers.get("user-agent", "guest")
#     return "Hello, %s!" % user_agent

# schema = make_executable_schema(type_defs, query)
# app = GraphQL(schema, debug=True)

"""
Make executable schema
"""
from ariadne import QueryType, make_executable_schema

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()

@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"

schema = make_executable_schema(type_defs, query)
print("")


"""
In this section, testing file uploads
"""
# import pandas as pd  

# class colors:
# 	RED = "\033[91m"
# 	BLUE = "\033[94m"
# 	BOLD = "\033[1m"
# 	UNDERLINE = "\033[4m"
# 	GREEN = "\033[92m"
# 	YELLOW = "\033[93m"
# 	END = "\033[0m"

# df = pd.read_csv("superstore_dataset_formattedID.csv")
# df = pd.DataFrame(df)

