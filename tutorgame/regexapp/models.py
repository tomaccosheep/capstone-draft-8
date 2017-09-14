from django.db import models

# Create your models here.

from django.utils.crypto import get_random_string

class Game_Num(models.Model):
    def_id = get_random_string(length=32)
    unique_id = models.CharField(max_length=32, primary_key=True, default=def_id)
    initial = models.BooleanField(default=True)
    well_being = models.BigIntegerField(null=True)
    money = models.BigIntegerField(null=True)
    popularity = models.BigIntegerField(null=True)
    veg = models.BigIntegerField(null=True)
    pizza = models.BigIntegerField(null=True)
    pizzar = models.BigIntegerField(null=True)
    shoe = models.BigIntegerField(null=True)
    partner = models.BooleanField(default=False)
    partner_gift = models.BigIntegerField(null=True)
    veg_cost_money = models.BigIntegerField(null=True)
    pizza_cost_money = models.BigIntegerField(null=True)
    pizzar_cost_money = models.BigIntegerField(null=True)
    shoes_cost_money = models.BigIntegerField(null=True)
    partner_cost_pop = models.BigIntegerField(null=True)
    gift_cost_money = models.BigIntegerField(null=True)
    cs_demand = models.BigIntegerField(null=True)
    repeat_me = models.CharField(max_length=256, null=True)
    select_me = models.CharField(max_length=256, null=True)
    full_string = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.unique_id

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
