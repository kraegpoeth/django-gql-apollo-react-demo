import graphene

import simple_app.schema
import user_profile.schema


class Queries(
    simple_app.schema.Query,
    user_profile.schema.Query,
    graphene.ObjectType
):
    dummy = graphene.String()


class Mutations(
    simple_app.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
