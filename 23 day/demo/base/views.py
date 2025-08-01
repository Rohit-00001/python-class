from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    superheros= {
        "names": [
            "ironman",
            "spiderman",
            "hulk",
            "thor",
            "captain america",
        ],
        "values": [1,2,34,5,6,7,8,9,10],
    }
    return render(request, "index.html", superheros)
def navbar(request):
    return render(request, "navbar.html")

def todo(request):
    return render(request, "todo.html")


def add(request):
    num2 = int(request.POST.get("num2"))
    num1 = int(request.POST.get("num1"))
    result = num1 + num2
    return render(request, "output.html", {"result": result})
   