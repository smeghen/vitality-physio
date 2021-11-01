from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=80,
                             null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1500, 
                             null=False, blank=False)

    def __str__(self):
        return self.email
