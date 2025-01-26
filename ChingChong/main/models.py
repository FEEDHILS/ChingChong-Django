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
    
class Restaurant(models.Model):
    adress = models.CharField("Адресс", max_length=256, blank=True, null=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, )

    class Meta:
        verbose_name = "restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.adress
    
    def save(self, *args, **kwargs):
        if not self.adress and self.city:
            self.adress = self.city.adress  # Устанавливаем имя по умолчанию
        super().save(*args, **kwargs)