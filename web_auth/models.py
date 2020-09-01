from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=70, unique=True)
    username = models.CharField(max_length=45, unique=True)
    avatar = models.ImageField(upload_to='users/avatars/', default='defaults/avatars/default_user_avatar.jpg')

    date_joined = models.DateTimeField(default=timezone.now)

    bio = models.TextField(blank=True)
    status = models.CharField(blank=True, max_length=70)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username']

    def __str__(self):
        return self.email


class Pet(models.Model):
    name = models.CharField(max_length=35)
    avatar = models.ImageField(upload_to='pets/avatars/', default='defaults/avatars/default_pet_avatar.png')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products/images', default='defaults/products/default_product_image.png')
    title = models.CharField(max_length=70)
    description = models.TextField()
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery_images')

    def __str__(self):
        return self.product