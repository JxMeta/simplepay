# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tag, Person

def index(request):
    home_display_tags = Tag.objects.filter(home_display=True)
    nav_display_tags = Tag.objects.filter(nav_display=True)

    return render(request, 'index.html', {
        'home_display_tags': home_display_tags,
        'nav_display_tags' : nav_display_tags,
    })

def tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)

    return render(request, 'persons/tag.html', {'tag': tag})

def person(request, person_name):
    person = Person.objects.get(name=person_name)

    return render(request, 'persons/person.html', {'person': person})


