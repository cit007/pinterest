from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def hello_world(request):
    if request.method == "POST":
        input_msg = request.POST.get("hello_world_input")

        return render(request, 'accountapp/hello_world.html', context={'text': input_msg})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})
