from django.db import models
from datetime import datetime
# Create your models here.

# admin info

class Admin(models.Model):
    name = models.CharField(max_length=30, default="username")
    image = models.ImageField(upload_to="admin", default="/static/image/user.png")
    admin_bio = models.TextField(max_length=200, default="Bio")
    phone_num = models.IntegerField(default=0 ,null=True, blank=True)
    face_url = models.URLField(default=0, null=True, blank=True)
    insta_url = models.URLField(default=0, null=True, blank=True)
    tiktok_url = models.URLField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

# posts

class PostsAdd(models.Model):
    post = models.CharField(max_length=60)
    time = models.DateTimeField(default=datetime.now, null=True , blank=True)
    image = models.ImageField(upload_to="posts-photo",null=True , blank=True)
    post_views  = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.post


class PostEdit(models.Model):
    new_post = models.CharField(max_length=100)
    new_time = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.new_post



# zapayn

class Zapayn(models.Model):
    name = models.CharField(max_length=30, default="zapayn-now", null=True, blank=True)
    members = models.IntegerField(null=True, blank=True, default=0)
    time = models.DateTimeField(default=datetime.now)


class ShopActivate(models.Model):
    name = models.CharField(max_length=30, default="activetion")
    active = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name



# product

class Product(models.Model):
    x = {
        ("حمام كريم","حمام كريم"),
        ("كريم","كريم"),
        ("جل","جل"),
        ("ماكينات حلاقة","ماكينات حلاقة"),
        ("شامبو","شامبو"),
        ("مستحضرات","مستحضرات"),
    }
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pieces = models.IntegerField(null=True, blank=True, default=0)
    category = models.CharField(max_length=30, choices=x)
    image = models.ImageField(null=False, blank=False, upload_to="pro_image/%y/%m/%d")
    
    def __str__(self):
        return self.name
    
    
    
# checks

class Checkin(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.IntegerField(default=0 ,null=True, blank=True)
    time = models.DateTimeField(default=datetime.now)
    user_views  = models.IntegerField(default=0, null=True, blank=True)


# offers

class Offer(models.Model):
    title = models.CharField(max_length=50)
    offer = models.TextField(max_length=300)
    time = models.DateTimeField(default=datetime.now)
    range_continue = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=8,default=0)