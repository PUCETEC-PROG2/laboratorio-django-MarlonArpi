from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, TrainerViewSet

router = DefaultRouter()

router.register('pokemons', PokemonViewSet, basename='pokemon')
router.register('trainers', TrainerViewSet, basename='trainer')

urlpatterns = [
    path('', include(router.urls)),
]
