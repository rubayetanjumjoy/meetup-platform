from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  # Import the User model
from django.contrib import messages  # Import messages framework
from django.shortcuts import redirect
from django.contrib.auth import logout


class Login(View):
    template_name = "user/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid login credentials. Please try again.")
            return render(request, self.template_name)


class SignUp(View):
    template_name = "user/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["signup-username"]
        email = request.POST["signup-email"]
        password = request.POST["signup-password"]

        # Check if the username or email is already in use
        if (
            User.objects.filter(username=username).exists()
            or User.objects.filter(email=email).exists()
        ):
            messages.error(
                request, "Username already in use. Please choose a different one."
            )
            return render(request, self.template_name)
        else:
            # Create a new user
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            login(request, user)
            return redirect("home")


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("home")
