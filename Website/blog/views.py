from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request, 'blog/home.html',{})


def index(request):
    return render(request,'blog/index.html',{})

def shop(request):
    return render(request,'blog/shop.html',{})
