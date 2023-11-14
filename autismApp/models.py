from django.db import models

# Create your models here.

class Result(models.Model):
    age = models.PositiveBigIntegerField()
    sex = models.PositiveBigIntegerField()
    a1 = models.PositiveIntegerField()
    a2 = models.PositiveIntegerField()
    a3 = models.PositiveIntegerField()
    a4 = models.PositiveIntegerField()
    a5 = models.PositiveIntegerField()
    a6 = models.PositiveIntegerField()
    a7 = models.PositiveIntegerField()
    a8 = models.PositiveIntegerField()
    a9 = models.PositiveIntegerField()
    a10 = models.PositiveIntegerField()
    jaundice = models.PositiveIntegerField()
    asd_history = models.PositiveIntegerField()
    test_completed_by = models.PositiveIntegerField()
    outcome = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.outcome
