from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    des1 = Destination.objects.all()
    return render(request,'index.html',{'des1':des1})
