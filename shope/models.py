from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length= 120)
    email = models.EmailField(max_length = 120)
    subject = models.TextField(max_length = 200)
    message = models.TextField(max_length = 1000)



class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True)
    availability = models.CharField(max_length=50)
    warranty = models.IntegerField()
    display_description = models.TextField()
    price = models.IntegerField()
    original_price = models.IntegerField()
    product_description = models.TextField()
    first_image = models.ImageField(upload_to='shop/images', default="")
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="parent_category", null=True, blank=True)

    def __str__(self):
        if self.parent and self.category:
            return f"{self.parent}>{self.category}"

        elif self.category:
            return self.category
        else:
            return ""

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "product_image")
    image = models.ImageField(upload_to='shop/images', default="")
