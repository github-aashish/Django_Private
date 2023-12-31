from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'index.html')

def infocustomer(request):
    if request.method == 'POST':
        uname = request.POST.get("name")
        uemail = request.POST.get("email")
        uphone_no = request.POST.get("phone_no")
        UMessage = request.POST.get("message")

        query = info_customer(name=uname,email=uemail,phone_no=uphone_no,message=UMessage)
        query.save()
        messages.success(request,"Information Saved successfully")
        return redirect(index)
    else:
        messages.error(request, "Error occured")
        return render(request, "index.html")
   # return render(request,"index.html")