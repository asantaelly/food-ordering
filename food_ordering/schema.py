import graphene

import menu.schema
import frontend.schema

class Query(
    menu.schema.Query, frontend.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    frontend.schema.Mutation, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)