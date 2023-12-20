from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client name: {self.name}, email: {self.email}, tel: {self.tel}, registration date: {self.reg_date}'


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'Item: {self.name}, prise: {self.price}, count: {self.count}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)