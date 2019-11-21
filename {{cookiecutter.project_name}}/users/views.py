from django.shortcuts import render, redirect
from .forms import RegisterForm


# View for registering new users
def register(response):

    if response.method == "POST":

        form = RegisterForm(response.POST)

        if form.is_valid():
                
            form.save()

        return redirect("/")

    else:

        form = RegisterForm()

    return render(response, "users/register.html", {"form":form})