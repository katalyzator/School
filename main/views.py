from django.shortcuts import render

from .models import *


def index_view(request):
    context = {}
    template = 'main/index.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'About.html'

    return render(request, template, context)


def contacts_view(request):
    context = {}
    template = 'Contacts.html'

    return render(request, template, context)


def information_view(request):
    info = Publication.objects.all()
    context = {"info": info}
    template = 'Information.html'

    return render(request, template, context)


def profile_view(request):
    context = {}
    template = 'Profile.html'

    return render(request, template, context)


def teachers_view(request):
    teacher = Teachers.objects.all()
    context = {"teacher": teacher}
    template = 'Teachers.html'

    return render(request, template, context)


def single_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    context = {"item": teacher}
    template = "Profile.html"

    return render(request, template, context)
