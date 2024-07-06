from django.db import models

# Create your models here.


class Home(models.Model):
    back_image = models.ImageField(upload_to="photos/about_me",blank=True)
    name = models.CharField(max_length=250)
    tag1 = models.CharField(max_length=250)
    tag2 = models.CharField(max_length=250)
    tag3 = models.CharField(max_length=250)
    facebook = models.CharField(max_length=255)
    linkdin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    
class About(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="photos/about_me",blank=True)
    birth = models.CharField(max_length=250)
    age = models.IntegerField()
    website = models.CharField(max_length=255)
    degree = models.CharField(max_length=250)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=255)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    

class Skill(models.Model):
    sk1 = models.CharField(max_length=255)
    sk2 = models.CharField(max_length=255)
    sk3 = models.CharField(max_length=255)
    sk4 = models.CharField(max_length=255)
    sk5 = models.CharField(max_length=255)
    sk6 = models.CharField(max_length=255)
    sk7 = models.CharField(max_length=255)
    sk8 = models.CharField(max_length=255)
    sk9 = models.CharField(max_length=255)

    def __str__(self):
        return self.sk1
