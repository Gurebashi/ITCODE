from django.urls import path
from Feed_app.views import feed_entrance,persona,group


urlpatterns = [
    path('',feed_entrance),
    path('personal/',persona),
    path('group/',group)
]

