from django.shortcuts import render, redirect  
from grzyby.forms import GrzybForm  
from grzyby.models import grzyb  
# Create your views here.


def insert(request):  
    if request.method == "POST":  
        form = GrzybForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = GrzybForm()  


    return render(request,'index.html',{'form':form})  


def show(request):  
    grzyby = grzyb.objects.all()  
    return render(request,'show.html',{'grzyby':grzyby})  


def edit(request, id):  
    grzyby = grzyb.objects.get(id=id)  
    return render(request,'edit.html', {'grzyby':grzyby})  


def update(request, id):  
    grzyby = grzyb.objects.get(id=id)  
    form = GrzybForm(request.POST, instance = grzyby)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'grzyby': grzyby})  


def delete(request, id):  
    grzyby = grzyb.objects.get(id=id)  
    grzyby.delete()  
    return redirect("/show")  

def move(request):
    return redirect("/show")
