from django.db import models


# Create your models here.
class User(models.Model):
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.eid
