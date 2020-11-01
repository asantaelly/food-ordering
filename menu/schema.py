import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from menu.models import Menu
from menu.forms import MenuForm

class MenuType(DjangoObjectType):
    class Meta:
        model = Menu
        fields = ("id", "title", 
        "details", "picture",
        "price", "is_available")

class CreateMenu(DjangoModelFormMutation):
    class Meta:
        form_class = MenuForm
    
    success = graphene.Boolean()

class Query(graphene.ObjectType):
    all_menus = graphene.List(MenuType)
    menu_by_id = graphene.Field(MenuType, id=graphene.String())

    def resolve_all_menus(self, info, **kwargs):
        # Querying a list
        return Menu.objects.all()

    def resolve_menu_by_id(self, info, id):
        # Querying a single menu
        return Menu.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    create_menu = CreateMenu.Field()