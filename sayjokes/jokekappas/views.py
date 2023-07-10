from django.shortcuts import render
import jokekappa

# Create your views here.

def thejoke(request):
    joke = jokekappa.get_joke()
    thisjoke = joke['content']
    return render(request, 'index.html', {"thisjoke": thisjoke})