from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=123)
    price = models.TextField()
    image = models.ImageField(upload_to='items/')
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class ItemImage(models.Model):
    image = models.ImageField(upload_to='items/detail/')
    recept = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.recept.title}'
