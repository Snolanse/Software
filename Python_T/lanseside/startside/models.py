from django.db import models

class Lanse(models.Model):
    lanse_nr = models.IntegerField()
    ant_steg = models.IntegerField()
    ant_akt = models.IntegerField()
    auto_man = models.IntegerField()
    man_steg = models.IntegerField()
    trykk = models.IntegerField()
