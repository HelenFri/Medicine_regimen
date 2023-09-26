from django.shortcuts import render


def index(request):
    name = 'Helen'
    context = {'name': name}
    return render(request, 'mainapp/index.html', context)


def about(request):
    return render(request, 'mainapp/about.html')