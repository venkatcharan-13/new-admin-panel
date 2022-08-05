from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def resources(request):
    return render(request,'resources.html')

def raiseticket(request):
    return render(request,'raiseticket.html')
    