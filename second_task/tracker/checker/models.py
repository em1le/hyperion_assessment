from django.db import models


class FileData(models.Model):
    """ File data model """

    file_id = models.CharField(primary_key=True, unique=True, max_length=64)
    name = models.CharField(max_length=255)
    modification_date = models.DateTimeField()
    occurence = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
