from django.urls import path, include
from .views import Get_Followers_Count_View

urlpatterns = [
    path("get-count-followers", Get_Followers_Count_View.as_view(), name="get-count-followers")
]
