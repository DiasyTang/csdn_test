from django.shortcuts import render
from django.http import HttpResponse
import pdb


# Create your views here.
def home_page(request):
    return render(request, 'home.html',
                  {'new_item_text': request.POST.get("item_text", "")})
