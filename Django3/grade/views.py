from django.shortcuts import render

# Create your views here.


def showGrades(request):

    return render(request, 'showgrades.html')


def showpage(request):

    return render(request, 'index.html')