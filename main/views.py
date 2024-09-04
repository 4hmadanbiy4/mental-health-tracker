from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152046',
        'name': 'Ahmad Nizar Sauki',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
