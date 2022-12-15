from django.http import HttpResponse
from django.shortcuts import render
from . models import place

# Create your views here.
def demo(request):
    obj=place.objects.all()
    return  render(request,"index.html",{'result':obj})

#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    addres=x+y
#    subres=x-y
#    mulres=x*y
#    divres=x/y
 #   return render(request,"result.html",{'add':addres,'sub':subres,'mul':mulres,'div':divres})

#def substraction(request):
#    return render(request,"result.html")

#def multiplication(request):
 #   return render(request,"result.html")

#def division(request):
 #   return render(request,"result.html")