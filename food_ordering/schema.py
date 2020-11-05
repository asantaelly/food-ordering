import graphene

import menu.schema
import database.schema

class Query(
    menu.schema.Query, database.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    database.schema.Mutation, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)