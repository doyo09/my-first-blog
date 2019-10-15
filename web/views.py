from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html', {})

def index(request):
    return render(request, 'index_full.html', {})

def about(request):
    return render(request, 'about.html', {})

def howtouse(request):
    return render(request, 'how_to_use.html', {})

def howtouse_video(request):
    return render(request, 'how_to_use_with_video.html', {})

def refund(request):
    return render(request, 'refund.html', {})

