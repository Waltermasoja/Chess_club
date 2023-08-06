from django.shortcuts import render
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers':mymembers,
    }
    return render(request,'members.html',context)

def details(request,id):
    mymembers = Member.objects.get(id = id)
    context = {
        'mymembers':mymembers,
    }
    return render(request,'details.html',context)
def main(request):
    return render(request,'main.html')