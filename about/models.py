from django.db import models

# Create your models here.
class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_misson  = models.TextField(max_length=1000)
    our_goals = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)


class FAQ(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.title
        



