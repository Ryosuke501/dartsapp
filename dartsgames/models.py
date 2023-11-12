from django.conf import settings
from django.db import models
from django.utils import timezone

class Game_master(models.Model):

    game_name = models.CharField(verbose_name= "ゲーム名", max_length=128)
    
    def __str__(self):
        return self.game_name
    
class Game_result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, verbose_name= 'ユーザー名')
    game_name = models.ForeignKey(Game_master , on_delete=models.CASCADE)
    score = models.CharField(max_length=50, verbose_name= 'スコア')
    play_time = models.IntegerField(blank= True, null= True, verbose_name= '１ゲームにかかった時間')
    create_at = models.DateTimeField(default= timezone.now, verbose_name= '更新日時')
    
    def __str__(self):
        return self.score
    