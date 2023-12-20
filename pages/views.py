from django.shortcuts import render
from pages.models import *

# Create your views here.


def home_page_viem(request):
    scrollos = MainScrollModel.objects.all().order_by('-pk')
    menu = Menu.objects.all()
    context ={
        'scrolls': scrollos,
        'menu': menu
    }
    return render(request, template_name='index.html', context=context)