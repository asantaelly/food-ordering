import graphene

import menu.schema

class Query(menu.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our projects
    pass

schema = graphene.Schema(query=Query)