from django.db import models

# Create your models here.

class Product (models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField
    desc=models.TextField #dicribtion
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def got_total(self):
        price=Product.object.get(id=self.product.id)
        return price.price * self.quantity


    def __str__(self):
        return f'{self.product.name} :  {self.quantity}'