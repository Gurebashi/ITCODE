from django.urls import path
from friends_app.views import myfriends, recfriends, groupfriends

urlpatterns = [
    path("myfriends/", myfriends),
    path("groupfriends/", groupfriends),
    path("recfriends/", recfriends),
]
