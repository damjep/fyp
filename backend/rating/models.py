from django.db import models

class Rating(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(choices=[(i, f"{i} stars") for i in range(1, 6)])
    comment = models.TextField(blank=True)
    
    