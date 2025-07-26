from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import MotherForm, ChildForm, AnketaResponseForm
from .models import Mother, Child, AnketaResponse

def index(request):
    return render(request, 'index.html')

def create_mother(request):
    if request.method == 'POST':
        form = MotherForm(request.POST)
        if form.is_valid():
            mother = form.save()
            return redirect('create_child', mother_id=mother.id)
    else:
        form = MotherForm()
    return render(request, 'create_mother.html', {'form': form})


def create_child(request, mother_id):
    mother = Mother.objects.get(id=mother_id)
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.mother = mother
            child.save()
            return redirect('create_anketa_response', child_id=child.id)
    else:
        form = ChildForm()
    return render(request, 'create_child.html', {'form': form, 'mother': mother})


def create_anketa_response(request, child_id):
    child = Child.objects.get(id=child_id)
    mother = child.mother
    if request.method == 'POST':
        form = AnketaResponseForm(request.POST)
        if form.is_valid():
            anketa = form.save(commit=False)
            anketa.child = child
            anketa.mother = mother
            anketa.save()
            return redirect('anketa_result', anketa_id=anketa.id)
    else:
        form = AnketaResponseForm()
    return render(request, 'create_anketa.html', {'form': form, 'mother': mother, 'child': child})
from .models import AnketaResponse

def anketa_result_view(request, anketa_id):
    anketa = AnketaResponse.objects.get(id=anketa_id)
    return render(request, 'result.html', {
        'anketa': anketa,
        'score': anketa.score,
        'risk': anketa.risk_category,
    })

