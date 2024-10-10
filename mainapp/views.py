from django.shortcuts import render, HttpResponse
from .models import TodoItem


# Create your views here.
def home(request):
    # return HttpResponse("Hello World!")
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()  # gets all objects that exist in database field
    return render(
        request, "todos.html", {"todos": items}
    )  # pass data to template as dictionary
