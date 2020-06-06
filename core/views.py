from django.http import JsonResponse
from django.shortcuts import render

from .models import Tweet


def home_view(request):
    return render(request, "core/home.html")


def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweets_list = [{"id": tweet.id, "content": tweet.content, "likes": 14} for tweet in tweets]
    data = {
        "idUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except Tweet.DoesNotExist:
        data["message"] = "Not found"
        status = 400
    return JsonResponse(data, status=status)
