import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from accounts.models import CustomUser
from accounts.forms import RegisterForm

class CustomerUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name",
        "email", "role", "date_joined")


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomerUserType)
    user_by_id = graphene.Field(CustomerUserType, id=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_user_by_id(self, info, id):
        return CustomUser.objects.get(pk=id)


class CreateUser(DjangoModelFormMutation):
    class Meta:
        form_class = RegisterForm


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()