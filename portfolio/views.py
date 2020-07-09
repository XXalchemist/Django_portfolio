from django.shortcuts import render
from portfolio.models import Project


# Create your views here.


#def home_page(request):
#    return render(request,'home.html',{})

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'project_index.html',context)