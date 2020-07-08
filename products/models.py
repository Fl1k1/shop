from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField()
    is_active = models.BooleanField(default=True)  # проверка на активность
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар %s" % self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")
    is_active = models.BooleanField(default=True)   # проверка на активность
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Изображение %s" % self.id

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

