from django.db import models
from helpers.models import CustomModel


class test(CustomModel):
    name = models.CharField(max_length=50)
    test_score = models.IntegerField()


class results(CustomModel):
    test = models.ForeignKey(test, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)