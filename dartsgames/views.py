from django.shortcuts import render
from django.utils import timezone
from .models import Game_result

# Create your views here.

def game_list(request):
    results = Game_result.objects.filter(create_at__lte = timezone.now()).order_by('create_at')
    return render(request, 'dartsgames/game_list.html', {'results' : results})