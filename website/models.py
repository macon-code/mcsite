from django.db import models


class ProjectRequest(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    contact_email = models.EmailField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
