from django import forms
from django.shortcuts import render

from models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person


def home(request):
    form = PersonForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    return render(request, "quai/person_list.html", {"persons": Person.objects.all(), "person_form": form})
