from django.shortcuts import render

def index(request):
    context = {}
    context["title"] = "Say jokes Demo"
    context["name"] = "Jamie Yu"
    return render(request, "index.html", context)