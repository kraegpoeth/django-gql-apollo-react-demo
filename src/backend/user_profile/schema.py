import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (graphene.Node, )


class Query(graphene.AbstractType):
    current_user = graphene.Field(UserType)

    def resolve_current_user(self, args, context, info):
        if not context.user.is_authenticated():
            return None
        return context.user
