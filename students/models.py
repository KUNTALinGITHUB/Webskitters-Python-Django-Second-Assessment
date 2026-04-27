from django.db import models

# This model represents the Student table in SQLite database
class Student(models.Model):
    # base on the question we need to have these fields in our model
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return self.name