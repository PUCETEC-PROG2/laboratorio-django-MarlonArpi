from django.contrib import admin
<<<<<<< HEAD
from .models import Pokemon, Trainer

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
=======
from .models import Pokemon 

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
>>>>>>> a978398 (LAB-4 ARPI EN PROCESO)
    pass