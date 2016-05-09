from django.contrib.auth.models import User
from movie_lens_online.models import Rater, Movie, Rating, Moviegenre

for rater in Rater.objects.all():
    user1 = User.objects(username='user{}'.format(rater.user_id), email='{}@gmail.com'.format(rater.user_id), password='password')
    user1.save()
    rater.auth_u_id = user1
    rater.save()



for one_user in User.objects.all():
    one_user.set_password('password')
    one_user.save()





for movie in Movie.objects.values():
    mov = Movie.objects.get(movie_id=movie['movie_id'])
    print(mov.movie_id)
    rating = Rating.objects.filter(movie_id=movie['movie_id']).aggregate(Avg('rating'))
    mov.avg_rating = (rating['rating__avg'])
    mov.save()
