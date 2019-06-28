from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import PersonEditForm
from .models import Person
from django.shortcuts import HttpResponseRedirect
import calendar


def main_page(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    month = calendar.month_name[person.date_of_birth.month]
    context = {"person": person,
               "month": month}
    return render(request, 'index.html', context)


def model_form_edit(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == 'POST':
        form = PersonEditForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            person.last_name = form.cleaned_data["last_name"]
            person.first_name = form.cleaned_data["first_name"]
            person.sex = form.cleaned_data["sex"]
            person.current_city = form.cleaned_data["current_city"]
            person.date_of_birth = form.cleaned_data["date_of_birth"]
            if request.FILES.get('ava_photo'):
                person.image = form.files["ava_photo"]
            person.save()
            return HttpResponseRedirect("/{0}".format(person.id))
        context = {"form": form,
                   "person": person}
        return render(request, 'form.html', context)
    form = PersonEditForm(initial={'first_name': person.first_name,
                                   'last_name': person.last_name,
                                   'sex': person.sex,
                                   'date_of_birth': person.date_of_birth,
                                   'current_city': person.current_city,
                                   'ava_photo': person.image})
    context = {"form": form,
               "person": person}
    return render(request, 'form.html', context)

# Create your views here.
