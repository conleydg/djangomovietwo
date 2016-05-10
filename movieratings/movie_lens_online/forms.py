from django import forms
from django.template import RequestContext
from .models import Rater, Movie, Rating
import re
from django.core.validators import RegexValidator

class AddRatingForm(forms.ModelForm):
    rating = forms.IntegerField(help_text="Please enter your rating:")

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating > 5 or rating < 0:
            raise forms.ValidationError('Rating must be 1-5')
        return rating


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        # movie = movie_id
        model = Rating
        fields = ('rating', )
