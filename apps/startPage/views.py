from django.shortcuts import render

def start_page_view(request):
    return render(request, 'startPage/startPage.html')