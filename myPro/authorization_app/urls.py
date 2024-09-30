from django.urls import path
from authorization_app.views import login, register, passwordrecover

urlpatterns = [
    path("login/", login),
    path("register/", register),
    path("passwordrecover/", passwordrecover),
]
