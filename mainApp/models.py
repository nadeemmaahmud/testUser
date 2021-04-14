from django.db import models
from django.contrib.auth.models import User
    
class dataDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    data = models.TextField()
    
    def __str__(self) -> str:
        return self.data
