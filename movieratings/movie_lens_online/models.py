
from django.db import models
from django.contrib.auth.models import User


class Rater(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    age = models.CharField(max_length=255)
    sex = models.CharField(max_length=255, default ='')
    occupation = models.CharField(max_length=255)
    auth_u = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Movie(models.Model):
    movie_id = models.CharField(max_length=255, primary_key=True)
    movie_title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    avg_rating = models.FloatField(default=0)

class Rating(models.Model):
    # movie_id = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now=True, null=True)

    def find_username(self):
        rater_id = self.rater_id
        rater_obj = Rater.objects.get(user_id=rater_id)
        auth_id = rater_obj.auth_u_id
        user_obj = User.objects.get(id=auth_id)
        return user_obj.username

class Moviegenre(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, null=True)
    unknown = models.IntegerField(default=0)
    Action = models.IntegerField(default=0)
    Adventure = models.IntegerField(default=0)
    Animation = models.IntegerField(default=0)
    Childrens = models.IntegerField(default=0)
    Comedy = models.IntegerField(default=0)
    Crime = models.IntegerField(default=0)
    Documentary = models.IntegerField(default=0)
    Drama = models.IntegerField(default=0)
    Fantasy = models.IntegerField(default=0)
    FilmNoir = models.IntegerField(default=0)
    Horror = models.IntegerField(default=0)
    Musical = models.IntegerField(default=0)
    Mystery = models.IntegerField(default=0)
    Romance = models.IntegerField(default=0)
    SciFi = models.IntegerField(default=0)
    Thriller = models.IntegerField(default=0)
    War = models.IntegerField(default=0)
    Western = models.IntegerField(default=0)
