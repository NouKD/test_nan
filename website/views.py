from django.shortcuts import render, redirect
from.models import Contact, NewsLetter, Presentation, SiteInfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm

# Create your views here.

def index(request):
    datas = {

    }
    return render(request, 'pages/index.html', datas)

def about(request):

    presentations = Presentation.objects.filter(status=True)

    datas = {

        'presentations': presentations

    }
    return render(request, 'pages/about.html', datas)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()

    data = {
        'contact_form': contact_form
    }
    
    return render(request, 'pages/contact.html', data)
    
#API MOBILE
@csrf_exempt
def connexion(request):
    message = ""
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(username=name,password=password)
        if user is not None and user.is_active:
            login(request,user)
            
            #### redirection si les infos sont correctes
            return redirect('index')
        else:
            print("login échoué")
            message = "Merci de vérifiez vos informations"

    datas = {
      'message': message
    }
    return JsonResponse(datas, safe=False)


