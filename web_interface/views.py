from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import PetCreationForm
from django.http import HttpResponse
from web_auth.models import Pet

# Create your views here.


@login_required(login_url='/auth/login/')
def profile(request):
    user = request.user
    pets = Pet.objects.filter(owner=user)

    return render(request, 'profile.html', {
        'user': user,
        'pets': pets,
    })


@login_required(login_url='/auth/login/')
def newpet(request):
    if request.method == 'POST':
        form = PetCreationForm(request.POST)
        print('Trying to validate the form')
        if form.is_valid():
            print('Form is Valid!')
            pet = form.save(commit=False)
            pet.owner = request.user
            print(pet.avatar)
            pet.save()
            return redirect('/web_interface/profile')
        else:
            return HttpResponse('Opps it looks like error happened.. Please, try again !')
    else:
        form = PetCreationForm
        return render(request, 'newpet.html', {
            'form': form
        })


def pet_profile(request, pk):
    pet = Pet.objects.get(pk=pk)
    return render(request, 'pet_profile.html', {
        'pet': pet
    })


def edit_pet_profile(request, pk):
    if request.method == 'POST':
        instance = get_object_or_404(Pet, pk=pk)
        form = PetCreationForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/web_interface/profile')
    else:
        form = PetCreationForm
        pet = Pet.objects.get(pk=pk)
        return render(request, 'edit_pet.html', {
            'form': form,
            'pet': pet,
        })


def delete_pet_profile(request, pk):
    user = request.user
    pet = Pet.objects.get(pk=pk)

    if pet.owner == user:
        pet.delete()
        return redirect('/web_interface/profile')
    else:
        return HttpResponse("You can not delete this pet profile !")