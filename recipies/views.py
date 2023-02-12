from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

import numpy as np
import pickle
import os

from recipies.models import Recipe
from recipies.forms import RecommendInformationForm, NewRecipeForm
from greenery.settings import BASE_DIR


# Create your views here.

@login_required
def index(request):
    recipes = Recipe.objects.all().order_by('-id')
    print(recipes)

    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(plant_name__icontains=query)
        )

    args = {
        'recipes': recipes
    }
    return render(request, 'recipes/index.html', args)


@login_required
def show(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    args = {
        'recipe': recipe
    }

    return render(request, 'recipes/show.html', args)

@login_required
def create(request):
    if request.method == "POST":
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            return redirect('recipes_show', data.id)
    else:
        form = NewRecipeForm()
    args = {
        'form': form
    }
    return render(request, 'recipes/create.html', args)



@login_required
def recommend(request):
    output = None
    if request.method == 'POST':
        form = RecommendInformationForm(request.POST)
        if form.is_valid():
            values = [
                form.cleaned_data.get('n'),
                form.cleaned_data.get('p'),
                form.cleaned_data.get('k'),
                form.cleaned_data.get('temp'),
                form.cleaned_data.get('humidity'),
                form.cleaned_data.get('ph'),
                form.cleaned_data.get('rainfall'),
            ]
            rel_path = "recipies/crop_model.pkl"
            path = os.path.join(BASE_DIR, rel_path)
            model = pickle.load(open(path, 'rb'))
            features = [np.array(values)]
            prediction = model.predict(features)
            output = prediction[0]
    else:
        form = RecommendInformationForm()
    args = {
        'form': form,
        'output': output
    }
    return render(request, 'recipes/predict.html', args)
