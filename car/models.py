from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Сокрощеое имя")
    full_name = models.CharField(max_length=60, verbose_name="Полное имя")

    def __str__(self):
        return f"{self.name} - {self.full_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Car(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.IntegerField()
    data = models.DateTimeField()
    is_take_away = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.brand