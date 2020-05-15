from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html',{})

def unit1_view(request):
    return render(request,'unit1.html',{})

def unit2_view(request):
    return render(request,'unit2.html',{})

def unit3_view(request):
    return render(request,'unit3.html',{})

def unit4_view(request):
    return render(request,'unit4.html',{})
