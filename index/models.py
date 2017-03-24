from django.db import models

# Create your models here.


class Translation(models.Model):
    ru = models.TextField(default='', max_length=10000)
    en = models.TextField(default='', max_length=10000)

    def as_dict(self):
        return {
            "ru": self.ru,
            "en": self.en,
        }

    def __str__(self):
        return self.ru
