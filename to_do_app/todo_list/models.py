from django.db import models


class List(models.Model):
    item = models.CharField(max_length=200)
    item_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.item_completed)