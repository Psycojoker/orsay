from django.shortcuts import render

from models import Person

def home(request):
    return render(request, "quai/person_list.html", {"persons": Person.objects.all()})
