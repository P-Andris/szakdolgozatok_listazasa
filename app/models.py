from django.db import models

class Szakdoga(models.Model):
    szakdoga_neve = models.CharField(max_length = 50, unique = True, verbose_name = 'Szakdolgozat neve')
    githublink = models.CharField(max_length = 200, unique = True, verbose_name = 'GitHub link')
    oldallink = models.CharField(max_length = 200, unique = True, verbose_name = 'Oldal link')
    tagokneve = models.CharField(max_length = 300, verbose_name = 'Tagok neve')