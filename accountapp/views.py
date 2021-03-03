from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse


def hello_world(request):
    if request.method == "POST":
        input_msg = request.POST.get("hello_world_input")

        # save to database
        new_hello_world = HelloWorld()
        new_hello_world.text = input_msg
        new_hello_world.save()

        # redirect account/hello_world using accountapp of urls.py
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
