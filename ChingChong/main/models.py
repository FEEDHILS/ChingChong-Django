from django.db import models

# Таблица с городами РФ
class Cities(models.Model):
    city = models.CharField("Город", max_length=256, blank=True)
    adress = models.CharField("Адресс", max_length=256, blank=True)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.adress