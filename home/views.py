from django.shortcuts import render
from.forms import student

# Create your views here.
def add(request):
    if request.method == 'POST':
        fm=student(request._post)
        if fm.is_valid():
            fm.save()
    else:
        fm=student()
    return render(request,'add.html',{'forms':fm})