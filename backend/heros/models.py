from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Hero(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    hp = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=5)
    armor = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=5)
    energy = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(1)], default=300) 

    @property
    def crit_hit(self):
        return int((self.hp + self.armor + self.energy/50)/30 * 10)
    
    def get_buff(self):
        return -1
