from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from django.template.loader import get_template 
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from forms import ChatForm
from models import Chats
# Create your views here.


def index(request):
    form = ChatForm()
    
    allchats = Chats.objects.all()
    
    
    # render can only take three inputs, if you want to pass multiple inputs you have to combine them into 1, (in this case context)
    
    context = {'chats': allchats, 'form': form}
    return render(request, 'chat.html', context)

    

def postchat(request):
    if request.method == "POST":
        pass