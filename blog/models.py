from django.db import models


class Blog(models.Model):
    author = models.CharField(max_length=80,
                              null=True, blank=False)
    subject = models.CharField(max_length=255,
                               null=False, blank=False)
    content = models.TextField(max_length=2000,
                               null=False, blank=False)

    def __str__(self):
        return self.subject
