from django.db import models
from  .GLOB import COLOR_CHOICES 
from .GLOB import GENDER_CHOICES 

class Post(models.Model):
    item_id = models.IntegerField
    item_name = models.CharField( max_length=50)
    item_size = models.CharField(max_length=3 , choices=[("XS" , "XS") , ("S", "S"), ("M","M"), ("L","L"), ("XL","XL"), ("XXL","XXL")])
    item_color = models.CharField( max_length=10 , choices=COLOR_CHOICES)
    item_gender = models.CharField(max_length=10 , choices=GENDER_CHOICES)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image_url = models.URLField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.item_name