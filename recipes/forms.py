from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length = 100)
    description = forms.CharField(label='Description', max_length = 400)
    ingredients = forms.CharField(label='Ingredients', max_length = 400)
    image = forms.ImageField(label='Add an Image')