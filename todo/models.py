from django.db import models

# Create your models here.
from django.db import models

class TodoDB(models.Model):
    todo=models.CharField(max_length=20)
    createdAt=models.DateField(auto_now=True)




# Create your models here.
