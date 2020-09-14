from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from shop.models import Ingredient, Toastie
from shop.forms import ImageFileUploadForm
import json
import requests

# Create your views here.
@login_required(login_url='/user/login')
def home(request):
    return render(request, 'home.html')  # , {'items':items})


def setup(request):
    return render(request, 'setup.html')

    # if request.method == 'POST':
    # Grab data from post request
    # Return success

def get_ingredients(request):
    ings = list(Ingredient.objects.all())
    return JsonResponse(ings, safe=False)


def add_img(request):
    form=ImageForm(request.POST,request.FILES)
    if(form.is_valid()):
        form.save()
        return HttpResponse("success")


def add_ingredient(request):
    '''body_unicode = request.body.decode('UTF-8')
    print(body_unicode)
    data = json.loads(body_unicode)
    ing = Ingredient(name=data['name'],
                     price=data['price'],
                     description=data['desc'],
                     image=data['img'],
                     category=data['cat'],
                     allergens=data['allergens'])'''

    if request.method == 'POST':
       form = ImageFileUploadForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})

    #ing.save()

def remove_ingredient(request):
    ing = Ingredient.objects.filter(pk=request.ingid)
    ing.delete()
