from django.db import models


class Members(models.Model):

    class Meta:
        verbose_name_plural = "Members"

    full_name = models.CharField(max_length=254, null=False, blank=False)
    email_address = models.CharField(max_length=254, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.full_name
