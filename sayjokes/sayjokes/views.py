from django.shortcuts import render

def index(request):
    context = {}
    context["title"] = "Say jokes Demo"
    context["Copyright"] = "Jamie Yu. Copyright © 2023 Say jokes Demo"
    return render(request, "index.html", context)