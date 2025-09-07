from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/',views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit/',views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>/delete/',views.delete_tweet, name='delete_tweet'),
    path('register/', views.register, name='register'),
    path('my_tweets/', views.my_tweets, name='my_tweets'),
    path('<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
]
