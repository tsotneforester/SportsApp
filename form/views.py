from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import uuid


# Create your views here.
data  = {
    "1": ["Tsotne", "football"],
}

SPORTS = ["football", "snooker", "boxing", "cycling"]

def index(request):

    return render(request, "form/index.html",{
      "names": data.items()
    })
  
def task(request, entry):
    result = {}
    for id, list in data.items():
      if list[0] == entry:
        result[id] = list


    
    return render(request, "form/task.html",{
      "names":result
    })

def edit(request, entry):

    print(entry)
    if request.method == "POST":
      result = {}
      for id, list in data.items():
        if list[0] == entry:
          result[id] = list


      return render(request, "form/edit.html", {
      "names":result,
       "sports": SPORTS
      })
    else:

      idnum = request.POST.get('id')
      name = request.POST.get('name')
      sport = request.POST.get('sport')

      temp = [name, sport]
     

      data[idnum] = temp
  


      return HttpResponseRedirect(reverse("index"))
 


def add(request):

    if request.method == "POST":
      name = request.POST.get('name')
      sport = request.POST.get('sport')
  
      if sport in SPORTS:
        data[str(uuid.uuid4())] = [name, sport ]
        
        return HttpResponseRedirect(reverse("index"))
      else:
        return HttpResponseRedirect(reverse("error"))



    return render(request, "form/add.html", {
      "sports": SPORTS
    })

def delete(request):
    if request.method == "POST":
      idnum = request.POST.get('id')
      data.pop(idnum)
      return HttpResponseRedirect(reverse("index"))

def update(request):
    if request.method == "POST":
      idnum = request.POST.get('id')
      name = request.POST.get('name')
      sport = request.POST.get('sport')
      data[idnum] = [name, sport] 
      return HttpResponseRedirect(reverse("index"))

def error(request):
  return render(request, "form/error.html", {
  "error": "No such option, Please avoid changing select options."
  })