from django.db import models

class DrinkOrder(models.Model):
    id = models.AutoField(primary_key=True)
    drink_type = models.CharField(max_length=255)
    number_of_sugars = models.IntegerField()
    is_extra_hot = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        extra_hot = ", extra Hot " if self.is_extra_hot else ""
        sugars = f" with {self.number_of_sugars} sugar{'s' if self.number_of_sugars > 1 else ''}" if self.number_of_sugars > 0 else " with no sugar"
        return f"{self.drink_type}{extra_hot}{sugars}"