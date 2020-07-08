from django.db import models

class Landing(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    msg = models.TextField()

    def __str__(self):
        return '%s' % (self.email)

