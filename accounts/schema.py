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

    custom_user = graphene.Field(CustomerUserType)

    # def mutate(self, info, form_class=None):
    #     custom_user = CustomUser(
    #         first_name=form_class.first_name,
    #         last_name=form_class.last_name,
    #         email=form_class.email,
    #     )


        # return CreateUser(custom_user=custom_user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()