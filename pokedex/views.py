from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from.models import Pokemon, Trainer
from pokedex.forms import PokemonForm, TrainerForm

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
        },
          request))

def pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, id:int):
    trainer = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance = pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance = pokemon)

    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    pokemon.delete()
    return redirect('pokedex:index')

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()

    return render(request, 'trainer_form.html', {'form': form})


def edit_trainer(request, id:int):
    trainer = Trainer.objects.get(id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'trainer_form.html', {'form': form})


def delete_trainer(request, id:int):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = "login_Form.html"