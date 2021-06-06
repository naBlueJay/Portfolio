from django.db import models

# this sets up the structure of the database
class URLData(models.Model):
    # every time something needs to be writen to the database, write it as a text field
    URLID = models.CharField(max_length = 1000)
    ShortURL = models.CharField(max_length = 1000)

    def __str__(self):
        template = '{0.URLID}, {0.ShortURL}'

        return template.format(self)
