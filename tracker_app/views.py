from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
import os
from dotenv import load_dotenv
import tweepy
from pprint import pprint

load_dotenv()
# Create your views here.
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)
class Get_Followers_Count_View(APIView):

    def get(self, request):
        user = api.get_user(screen_name="AkhmatovichUz")
        pprint(user._json)
        return Response(user._json)
