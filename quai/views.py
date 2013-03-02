from django import forms
from django.shortcuts import render
from djangbone.views import BackboneAPIView

from models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person


class PersonView(BackboneAPIView):
    base_queryset = Person.objects.all()
    add_form_class = PersonForm
    edit_form_class = PersonForm


def home(request):
    form = PersonForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    return render(request, "quai/person_list.html", {"persons": Person.objects.all(), "person_form": form})
