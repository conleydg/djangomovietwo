from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Sum

from .models import Rater, Movie, Rating, Moviegenre
from .forms import AddRatingForm


def index(request):
    top_twenty_list = Movie.objects.order_by('-avg_rating')[:20]
    context = {'top_twenty_list': top_twenty_list}
    return render(request, 'movies/index.html', context)


def movie(request, movie_id):
    if request.method == 'POST':
        form = AddRatingForm(request.POST)
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.movie_id = movie_id
            user = request.user.username
            username = User.objects.get(username=user)
            new_rating.rater_id = username.rater.user_id
            new_rating.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)
    else:
        form = AddRatingForm()
    try:
        current_id = username.rater.user_id
    except:
        current_id = None
    rating_list = Rating.objects.filter(movie_id=movie_id)
    rater_queries = rating_list.values_list('rater_id', flat=True)
    grabber = (Movie.objects.get(movie_id=movie_id))
    name_finder = grabber.movie_title
    avg_rating = grabber.avg_rating
    context = {'rating_list': rating_list, 'movie_id': movie_id,
                'name_finder': name_finder, 'avg_rating': avg_rating, 'form':form,
                'rater_queries':rater_queries, 'current_id':current_id}
    return render(request, 'movies/movie.html', context)


def raterer(request, user_id):
    rated_movies_list = Rating.objects.filter(rater_id=user_id)
    grabber = (Rater.objects.get(user_id=user_id))
    age = grabber.age
    sex = grabber.sex
    occupation = grabber.occupation
    movie_obj_list = []
    for movie in rated_movies_list:
        movie = Movie.objects.get(pk=movie.movie_id)
        movie_obj_list.append(movie)
    context = {'rated_movies_list': rated_movies_list, 'user_id': user_id,
    'age':age, 'sex':sex, 'occupation': occupation, 'movie_obj_list':movie_obj_list}
    return render(request, 'movies/raterer.html', context)



def top_by_genre(request, genre):
        genre_find='moviegenre__{}'.format(genre)
        sig_sample = Movie.objects.annotate(count = Count('rating')).filter(count__gt = 10)
        sig_sample = sig_sample.filter(**{genre_find:1})
        sorted_movies = sig_sample.annotate(aveg_rating = Avg('rating__rating')).order_by('-aveg_rating')
        sorted_movies = sorted_movies[:20]
        context = {'sorted_movies':sorted_movies, 'genre':genre}
        return render(request, 'movies/tops.html', context)
