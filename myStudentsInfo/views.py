from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentsInformation
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form = StudentsInformation(request.POST)
        if form.is_valid():

            form.save()
            form = StudentsInformation()

    else:
        form = StudentsInformation()
    students = User.objects.all()
    return render(request,'myStudentsInfo/addandshow.html',{'form': form,'students':students})


def delete_sutdents(request,id):
    if request.method=='POST':
        de=User.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method=='POST':
        de = User.objects.get(pk=id)
        form = StudentsInformation(request.POST,instance=de)
        if form.is_valid():
            form.save()
    else:
        de = User.objects.get(pk=id)
        form = StudentsInformation(instance=de)
    return render(request,'myStudentsInfo/updatestudent.html',{'form':form})
