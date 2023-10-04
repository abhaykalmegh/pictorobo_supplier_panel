from django.db import models
from django.utils.html import mark_safe


class Product(models.Model):                  # Product Model
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="product_imgs/")
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # brand=models.ForeignKey(Brand,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '1. products'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.title + " " + self.description

