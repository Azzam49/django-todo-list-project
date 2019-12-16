from django.db import models

# Create your models here.
class TodoModel(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"ID : {self.id} Content : {self.content} \n"