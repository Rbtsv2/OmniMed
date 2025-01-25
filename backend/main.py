from fastapi import FastAPI
from graphene import ObjectType, String, Schema
from starlette.graphql import GraphQLApp

class Query(ObjectType):
    hello = String(name=String(default_value="world"))

    def resolve_hello(root, info, name):
        return f"Hello, {name}!"

schema = Schema(query=Query)

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=schema))

@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur l'API backend."}