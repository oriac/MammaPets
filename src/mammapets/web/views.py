from django.http import HttpResponse

from .forms import ContractForm
from .models import Pet
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404


def index(request):
    latest_pet_list = Pet.objects.order_by('name')[:5]
    context = {'latest_pet_list': latest_pet_list}
    return render(request, 'pets/index.html', context)


def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/detail.html', {'pet': pet})


def results(request, pet_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % pet_id)


def vote(request, pet_id):
    return HttpResponse("You're voting on question %s." % pet_id)


def contract(request):
    form = ContractForm()
    return render(request, 'pets/contract.html', {'form': form})


def new_contract(request):
    form = ContractForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponse("contract saved")
    return HttpResponse("contract not saved")
