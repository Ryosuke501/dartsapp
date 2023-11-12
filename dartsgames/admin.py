from django.contrib import admin
from .models import Game_master
from .models import Game_result

# Register your models here.
admin.site.register(Game_master)
admin.site.register(Game_result)