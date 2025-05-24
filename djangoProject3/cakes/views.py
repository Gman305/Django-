from django.shortcuts import render, redirect

from cakes.forms import CakeForm
from cakes.models import Cake, Baker


# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    return render(request,'index.html',{'cakes':cakes})

def add_cakes(request):
    if request.method == 'POST':
        form = CakeForm(request.POST,request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker=Baker.objects.filter(user=request.user).first()
            cake.save()
        return redirect('index')

    return render(request,'add.html',{'form':CakeForm()})