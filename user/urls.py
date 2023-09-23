from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.Logout.as_view(), name="logout"),
]
