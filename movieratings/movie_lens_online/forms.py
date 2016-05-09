from django import forms
from django.template import RequestContext
from .models import Rater, Movie, Rating

class AddRatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=128, help_text="Please enter your rating:")

    # rater_id =


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        # movie = movie_id
        model = Rating
        fields = ('rating', )
