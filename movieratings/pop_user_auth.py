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









<link rel="stylesheet" type="text/css" href="{% static 'movie_lens_online/style.css' %}" />

<html lang="en">

<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

<head>
    <title>{% block title %}Movie Ratings{% endblock %}</title>
</head>

<body>

    <div id="header">
    {% block header %}
    <a href="{% url 'movie_lens_online:index' %}">{% trans "Home" %}</a> |

    {% if user.is_authenticated %}
      {% trans "Logged in" %}: {{ user.username }}
      (<a href="{% url 'auth_logout' %}">{% trans "Log out" %}</a> |
      <a href="{% url 'auth_password_change' %}">{% trans "Change password" %}</a>)
    {% else %}
       <a href="{% url 'auth_login' %}">{% trans "Log in" %}</a>
    {% endif %}
    <br><br>

      <div class="dropdown">
        <button class="dropbtn">Top Tenty Movies by Genre</button>
        <div class="dropdown-content">
          <a href="/movie_lens_online/top/Action">{% trans "Action" %}</a> |
          <a href="/movie_lens_online/top/Adventure">{% trans "Adventure" %}</a> |
          <a href="/movie_lens_online/top/Animation">{% trans "Crime" %}</a> |
          <a href="/movie_lens_online/top/Childrens">{% trans "Childrens" %}</a> |
          <a href="/movie_lens_online/top/Comedy">{% trans "Comedy" %}</a> |
          <a href="/movie_lens_online/top/Crime">{% trans "Crime" %}</a> |
          <a href="/movie_lens_online/top/Documentary">{% trans "Documentary" %}</a> |
          <a href="/movie_lens_online/top/Drama">{% trans "Drama" %}</a> |
          <a href="/movie_lens_online/top/Fantasy">{% trans "Fantasy" %}</a> |
          <a href="/movie_lens_online/top/FilmNoir">{% trans "FilmNoir" %}</a> |
          <a href="/movie_lens_online/top/Horror">{% trans "Horror" %}</a> |
          <a href="/movie_lens_online/top/Musical">{% trans "Musical" %}</a> |
          <a href="/movie_lens_online/top/Mystery">{% trans "Mystery" %}</a> |
          <a href="/movie_lens_online/top/Romance">{% trans "Romance" %}</a> |
          <a href="/movie_lens_online/top/SciFi">{% trans "SciFi" %}</a> |
          <a href="/movie_lens_online/top/Thriller">{% trans "Thriller" %}</a> |
          <a href="/movie_lens_online/top/War">{% trans "War" %}</a> |
          <a href="/movie_lens_online/top/Western">{% trans "Western" %}</a> |
        </div>
      </div>



    <hr />
    {% endblock %}
    </div>

    <div id="content">
    {% block content %}{% endblock %}
    </div>

    <div id="footer">
    {% block footer %}
        <hr />
    {% endblock %}
    </div>
</body>

</html>










<style>
/* Style The Dropdown Button */
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: right;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

/* Links inside the dropdown */
.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #f1f1f1}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
    display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
</style>


.right {
     text-align: center;
}








/*
 * Base structure
 */

/* Move down content because we have a fixed navbar that is 50px tall */
body {
  padding-top: 50px;
}


/*
 * Global add-ons
 */

.sub-header {
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

/*
 * Top navigation
 * Hide default border to remove 1px line.
 */
.navbar-fixed-top {
  border: 0;
}

/*
 * Sidebar
 */

/* Hide for mobile, show later */
.sidebar {
  display: none;
}
@media (min-width: 768px) {
  .sidebar {
    position: fixed;
    top: 51px;
    bottom: 0;
    left: 0;
    z-index: 1000;
    display: block;
    padding: 20px;
    overflow-x: hidden;
    overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
    background-color: #f5f5f5;
    border-right: 1px solid #eee;
  }
}

/* Sidebar navigation */
.nav-sidebar {
  margin-right: -21px; /* 20px padding + 1px border */
  margin-bottom: 20px;
  margin-left: -20px;
}
.nav-sidebar > li > a {
  padding-right: 20px;
  padding-left: 20px;
}
.nav-sidebar > .active > a,
.nav-sidebar > .active > a:hover,
.nav-sidebar > .active > a:focus {
  color: #fff;
  background-color: #428bca;
}


/*
 * Main content
 */

.main {
  padding: 20px;
}
@media (min-width: 768px) {
  .main {
    padding-right: 40px;
    padding-left: 40px;
  }
}
.main .page-header {
  margin-top: 0;
}


/*
 * Placeholder dashboard ideas
 */

.placeholders {
  margin-bottom: 30px;
  text-align: center;
}
.placeholders h4 {
  margin-bottom: 0;
}
.placeholder {
  margin-bottom: 20px;
}
.placeholder img {
  display: inline-block;
  border-radius: 50%;
}



















<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
<h1 class="page-header">Dashboard</h1>

<div class="row placeholders">
<div class="col-xs-6 col-sm-3 placeholder">
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
<h4>Label</h4>
<span class="text-muted">Something else</span>
</div>
<div class="col-xs-6 col-sm-3 placeholder">
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
<h4>Label</h4>
<span class="text-muted">Something else</span>
</div>
<div class="col-xs-6 col-sm-3 placeholder">
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
<h4>Label</h4>
<span class="text-muted">Something else</span>
</div>
<div class="col-xs-6 col-sm-3 placeholder">
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" width="200" height="200" class="img-responsive" alt="Generic placeholder thumbnail">
<h4>Label</h4>
<span class="text-muted">Something else</span>
</div>
</div>

<h2 class="sub-header">Section title</h2>
<div class="table-responsive">
<table class="table table-striped">
<thead>
<tr>
  <th>#</th>
  <th>Header</th>
  <th>Header</th>
  <th>Header</th>
  <th>Header</th>
</tr>
</thead>
<tbody>
<tr>
  <td>1,001</td>
  <td>Lorem</td>
  <td>ipsum</td>
  <td>dolor</td>
  <td>sit</td>
</tr>
<tr>
  <td>1,002</td>
  <td>amet</td>
  <td>consectetur</td>
  <td>adipiscing</td>
  <td>elit</td>
</tr>
<tr>
  <td>1,003</td>
  <td>Integer</td>
  <td>nec</td>
  <td>odio</td>
  <td>Praesent</td>
</tr>
<tr>
  <td>1,003</td>
  <td>libero</td>
  <td>Sed</td>
  <td>cursus</td>
  <td>ante</td>
</tr>
<tr>
  <td>1,004</td>
  <td>dapibus</td>
  <td>diam</td>
  <td>Sed</td>
  <td>nisi</td>
</tr>
<tr>
  <td>1,005</td>
  <td>Nulla</td>
  <td>quis</td>
  <td>sem</td>
  <td>at</td>
</tr>
<tr>
  <td>1,006</td>
  <td>nibh</td>
  <td>elementum</td>
  <td>imperdiet</td>
  <td>Duis</td>
</tr>
<tr>
  <td>1,007</td>
  <td>sagittis</td>
  <td>ipsum</td>
  <td>Praesent</td>
  <td>mauris</td>
</tr>
<tr>
  <td>1,008</td>
  <td>Fusce</td>
  <td>nec</td>
  <td>tellus</td>
  <td>sed</td>
</tr>
<tr>
  <td>1,009</td>
  <td>augue</td>
  <td>semper</td>
  <td>porta</td>
  <td>Mauris</td>
</tr>
<tr>
  <td>1,010</td>
  <td>massa</td>
  <td>Vestibulum</td>
  <td>lacinia</td>
  <td>arcu</td>
</tr>
<tr>
  <td>1,011</td>
  <td>eget</td>
  <td>nulla</td>
  <td>Class</td>
  <td>aptent</td>
</tr>
<tr>
  <td>1,012</td>
  <td>taciti</td>
  <td>sociosqu</td>
  <td>ad</td>
  <td>litora</td>
</tr>
<tr>
  <td>1,013</td>
  <td>torquent</td>
  <td>per</td>
  <td>conubia</td>
  <td>nostra</td>
</tr>
<tr>
  <td>1,014</td>
  <td>per</td>
  <td>inceptos</td>
  <td>himenaeos</td>
  <td>Curabitur</td>
</tr>
<tr>
  <td>1,015</td>
  <td>sodales</td>
  <td>ligula</td>
  <td>in</td>
  <td>libero</td>
</tr>
</tbody>
</table>
</div>
</div>





    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Movie Lens Project</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="{% url 'movie_lens_online:index' %}">{% trans "Home" %}</a></li>
              {% if user.is_authenticated %}
            <li>{% trans "Logged in" %}: {{ user.username }}</li>
            <li><a href="{% url 'auth_logout' %}">{% trans "Log out" %}</a></li>
            <li><a href="{% url 'auth_password_change' %}">{% trans "Change password" %}</a></li>
            {% else %}
            <li><a href="{% url 'auth_login' %}">{% trans "Log in" %}</a></li>
            {% endif %}
          </ul>
        </div>
      </div>
    </nav>
