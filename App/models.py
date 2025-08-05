from django.db import models

class Walpaper(models.Model):
    name = models.CharField(max_length =100)
    img = models.ImageField(upload_to = 'pics')
    img_type = models.CharField(max_length=50)
