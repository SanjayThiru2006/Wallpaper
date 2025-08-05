from django.shortcuts import render
from django.http import HttpResponse
from .models import Walpaper
# Create your views here.
def home(request):
    return render(request,'index.html')

def admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Type = request.POST.get('Type')
        Walpaper.objects.create(name=name,img_type=Type)
    return render(request,'admin.html')