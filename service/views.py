from django.shortcuts import render

# Create your views here.

def fashion(request):
    datas = {

    }
    return render(request, 'pages/fashion.html', datas)

def single(request):
    datas = {

    }
    return render(request, 'pages/single.html', datas)

def travel(request):
    datas = {

    }
    return render(request, 'pages/travel.html', datas)
