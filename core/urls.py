from django.urls import path

from .views import home_view, tweet_detail_view, tweet_list_view

app_name = "core"
urlpatterns = [
    path("", home_view, name="home"),
    path("tweets/", tweet_list_view, name="list"),
    path("tweets/<str:tweet_id>", tweet_detail_view, name="details")
]
