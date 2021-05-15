from django.db import models

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
