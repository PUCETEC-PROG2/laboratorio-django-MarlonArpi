from rest_framework import serializers
from pokedex.models import Pokemon, Trainer


class PokemonSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Pokemon
        fields = '__all__'
        

class TrainerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'age', 'level', 'birthday', 'picture']
        