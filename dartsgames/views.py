from django.shortcuts import render

# Create your views here.

def game_list(request):
    return render(request, 'dartsgames/game_list.html', {})