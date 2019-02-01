from django.shortcuts import render 
from .models import POST
def home(request):
    context = {
        'posts':POST.objects.all()


    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

# Create your views here.


