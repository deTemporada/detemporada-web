import graphene
from graphene_django.types import DjangoObjectType
from api.models import Recipe

class RecipeType(DjangoObjectType):
	class Meta:
		model = Recipe

class Query(object):
	all_recipes = graphene.List(RecipeType)

	def resolve_all_recipes(self, info, **kwargs):
		return Recipe.objects.all()