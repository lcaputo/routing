from django.shortcuts import render


# Create your views here.
def RoutesView(request):
    if request.method == 'POST':
        print(request.POST)