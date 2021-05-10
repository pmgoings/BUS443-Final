from django.shortcuts import render
from django.http import HttpResponse
from Finalapp.models import Studentdetails
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    context = {'name':'Patrick Goings'}
    return render(request, 'Finalapp/home.html', context)
    
    
def Student(request):
    Students = Studentdetails.objects.all()
    paginator = Paginator(Students, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'Finalapp/Studentdetails.html', context)

def Coursedetails(request):
    return render(request, 'Finalapp/Courses.html')