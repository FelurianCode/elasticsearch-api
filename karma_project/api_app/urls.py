from django.urls import include, path

from . import views, search

urlpatterns = [
    path('tweets/', views.get_tweets, name='tweets'),
    path('elastic/', search.bulk_indexing, name='elastic'),
    path('tweets-date/', search.search_by_date, name='tweetsdate'),
    path('tweets-user/', search.search_by_user, name='tweetsuser'),
]