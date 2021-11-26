from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=80,
                              null=True, blank=False)
    subject = models.CharField(max_length=255,
                               null=False, blank=False)
    message = models.TextField(max_length=1500,
                               null=False, blank=False)

    def __str__(self):
        return self.subject
