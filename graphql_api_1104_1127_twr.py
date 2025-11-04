# 代码生成时间: 2025-11-04 11:27:40
from bottle import Bottle, request, response
from graphene import ObjectType, String, Schema, Field
from graphene_bottle import GraphQLPlugin


# Define the Query class for GraphQL
class Query(ObjectType):
    hello = String(description="A simple type for getting started.")

    def resolve_hello(self, info):
        """
        Resolver for the 'hello' field.
        """
        return "World"


# Create the application instance
app = Bottle()

# Create a GraphQL schema
schema = Schema(query=Query)

# Add the GraphQLPlugin to the Bottle app
app.install(GraphQLPlugin(schema=schema))

# Define routes for GraphQL
@app.route("/graphql", method="POST")
def graphql():
    "