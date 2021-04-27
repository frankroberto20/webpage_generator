from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django import forms

from .models import *

# Form models

class PageForm(forms.ModelForm):
    pass

# Create your views here.

def index(request):
    return render(request, 'webpage_generator/index.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "webpage_generator/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "webpage_generator/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "webpage_generator/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "webpage_generator/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "webpage_generator/register.html")

def create_page(request):
    if request.method == 'GET':
        return render(request, 'webpage_generator/create_page.html')
    elif request.method == 'POST':
        try:
            sections_num = request.POST['section-num']
            title = request.POST['title']
            page = Page(title=title)

            for i in range(sections_num):
                heading = request.POST[f'heading-{i}']
                content = request.POST[f'content-{i}']
                section = Section(page=page, heading=heading, content=content)
                section.save()

            page.save()
        except:
            pass
         