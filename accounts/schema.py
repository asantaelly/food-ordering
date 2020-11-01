import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
import graphql_jwt

from accounts.models import CustomUser
from accounts.forms import RegisterForm

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name",
        "email", "role", "is_active", "date_joined")
        USERNAME_FIELD = 'email'


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    user_by_id = graphene.Field(CustomUserType, id=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_user_by_id(self, info, id):
        return CustomUser.objects.get(pk=id)


class CreateUser(DjangoModelFormMutation):
    class Meta:
        form_class = RegisterForm


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(CustomUserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Mutation(graphene.ObjectType):
    # Mutation variables for authentication
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    veriry_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


    # Mutation for creating a user
    create_user = CreateUser.Field()
