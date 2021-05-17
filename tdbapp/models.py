from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Leads(models.Model):

    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    company = models.CharField(max_length=20)
    inquiry_type = models.CharField(max_length=50)
    helping = models.TextField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    uid = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=75)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog_images/', null=True)
    content = models.TextField()

    def __str__(self):
        return str(self.title) + ' ' + str(self.author)

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
