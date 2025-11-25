from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
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

@login_required
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

@login_required
def delete_pokemon(request, id:int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()

    return render(request, 'trainer_form.html', {'form': form})

@login_required
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

@login_required
def delete_trainer(request, id:int):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('pokedex:index')

def list_trainers(request):
    q = request.GET.get('q', '').strip()
    trainers = Trainer.objects.all()

    if q:
        trainers = trainers.filter(
            Q(name__icontains=q) |
            Q(region__icontains=q)
        )

    paginator = Paginator(trainers.order_by('name'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'trainers': page_obj,
        'page_obj': page_obj,
        'q': q,
    }
    return render(request, 'list_trainers.html', context)


def list_pokemons(request):
    q = request.GET.get('q', '').strip()
    type_filter = request.GET.get('type', '').strip()
    trainer_filter = request.GET.get('trainer', '').strip()

    pokemons = Pokemon.objects.all()

    if q:
        pokemons = pokemons.filter(
            Q(name__icontains=q) |
            Q(trainer__name__icontains=q)
        )

    if type_filter:
        pokemons = pokemons.filter(type=type_filter)

    if trainer_filter:
        pokemons = pokemons.filter(trainer__id=trainer_filter)

    paginator = Paginator(pokemons.order_by('name'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    trainers_for_filter = Trainer.objects.all()

    try:
        type_choices = Pokemon.TYPE_CHOICES
    except Exception:
        type_choices = []

    context = {
        'pokemons': page_obj,
        'page_obj': page_obj,
        'q': q,
        'type_filter': type_filter,
        'trainer_filter': trainer_filter,
        'trainers_for_filter': trainers_for_filter,
        'type_choices': type_choices,
    }
    return render(request, 'list_pokemons.html', context)




class CustomLoginView(LoginView):
    template_name = "login_form.html"