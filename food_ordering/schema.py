import graphene

import menu.schema
import accounts.schema

class Query(
    menu.schema.Query, accounts.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    menu.schema.Mutation, accounts.schema.Mutation, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)