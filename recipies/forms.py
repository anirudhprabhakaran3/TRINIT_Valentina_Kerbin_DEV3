from django import forms
from recipies.models import Recipe


class RecommendInformationForm(forms.Form):
    n = forms.FloatField(help_text="Enter nitrogen concentration of area you live in.")
    p = forms.FloatField(help_text="Enter phosphorus concentration of area you live in.")
    k = forms.FloatField(help_text="Enter potassium concentration of area you live in.")
    temp = forms.FloatField(help_text="Enter temperature of area you live in.")
    humidity = forms.FloatField(help_text="Enter average humidity of area you live in.")
    ph = forms.FloatField(help_text="Enter the pH of the area you in live in.")
    rainfall = forms.FloatField(help_text="Enter the average rainfall in mm.")


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['plant_name', 'n', 'p', 'k', 'temp', 'humidity', 'ph', 'rainfall', 'instructions']
