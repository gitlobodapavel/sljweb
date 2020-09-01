from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import PetCreationForm, EditUserForm, PlaceProductForm, EditProductForm
from django.http import HttpResponse
from web_auth.models import Pet, Product
from django.db.models import Q

# Create your views here.


@login_required(login_url='/auth/login/')
def profile(request):
    user = request.user
    pets = Pet.objects.filter(owner=user)
    products = Product.objects.filter(seller=user)

    return render(request, 'profile.html', {
        'user': user,
        'pets': pets,
        'products': products,
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
    pet = Pet.objects.get(pk=pk)
    if pet.owner == request.user:
        if request.method == 'POST':
            instance = get_object_or_404(Pet, pk=pk)
            form = PetCreationForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/web_interface/profile')
        else:
            instance = get_object_or_404(Pet, pk=pk)
            form = PetCreationForm(instance=instance)
            pet = Pet.objects.get(pk=pk)
            return render(request, 'edit_pet.html', {
                'form': form,
                'pet': pet,
            })
    else:
        return HttpResponse("You have no access to edit this pet !")


def delete_pet_profile(request, pk):
    user = request.user
    pet = Pet.objects.get(pk=pk)

    if pet.owner == user:
        pet.delete()
        return redirect('/web_interface/profile')
    else:
        return HttpResponse("You can not delete this pet profile !")


def edit_user_profile(request, pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)

    if user == request.user:
        if request.method == 'POST':
            User = get_user_model()
            instance = get_object_or_404(User, pk=pk)
            form = EditUserForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/web_interface/profile')
        else:
            User = get_user_model()
            instance = get_object_or_404(User, pk=pk)
            form = EditUserForm(instance=instance)
            return render(request, 'edit_user_profile.html', {
                'form': form,
            })
    else:
        return HttpResponse("You have no access to edit this profile !")


def newpoduct(request):
    if request.method == 'POST':
        user = request.user
        form = PlaceProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = user
            product.save()
            return redirect('/web_interface/profile')
    else:
        form = PlaceProductForm
        return render(request, 'newproduct.html', {
            'form': form
        })


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if product.seller == request.user:
        if request.method == 'POST':
            instance = get_object_or_404(Product, pk=pk)
            form = EditProductForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/web_interface/profile')
        else:
            instance = get_object_or_404(Product, pk=pk)
            form = EditProductForm(instance=instance)
            return render(request, 'edit_product.html', {
                'form': form
            })
    else:
        return HttpResponse('You have no access to edit this product !')



def delete_product(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    if product.seller == user:
        product.delete()
        return redirect('/web_interface/profile')
    else:
        return HttpResponse('You have no access to delete this product !')


def view_product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_view.html', {
        'product': product,
    })


def search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        user = get_user_model()
        users = user.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query))
        products = Product.objects.filter(Q(title__icontains=query))
        return render(request, 'search_results.html', {
            'users': users,
            'products': products,
        })
    else:
        query = 'You submitted an empty form ('
    return HttpResponse(query)


def profile_view(request, pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    pets = Pet.objects.filter(owner=user)
    products = Product.objects.filter(seller=user)
    return render(request, 'profile_view.html', {
        'user': user,
        'products': products,
        'pets': pets,
    })