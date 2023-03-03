from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


def add(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    result = int(a) + int(b)
    return JsonResponse({"result": result})
def map(request):
    return render (request, "SEND/map.html")
  
