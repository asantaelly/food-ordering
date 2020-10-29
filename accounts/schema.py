import graphene
from graphene_django import DjangoObjectType

from accounts.models import CustomUser

class CustomerUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name",
        "email", "role", "date_joined")


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomerUserType)
    user_by_id = graphene.Field(CustomerUserType, id=graphene.String())

    def resolve_all_users(root, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_user_by_id(root, info, id):
        return CustomUser.objects.get(pk=id)
