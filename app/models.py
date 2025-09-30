from django.db import models

# Create your models here.
class UploadForm(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.IntegerField()
    Image = models.ImageField(upload_to='images/')
    Documents = models.FileField(upload_to='documents/')
    Video = models.FileField(upload_to='video/')
    Password = models.CharField(max_length=50)

    class Meta:
        db_table = 'Form_Data'
    
    def __str__(self):
        return self.Name + ' ' + self.Email + " " +self.Password

class UserQuery(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Query = models.CharField(max_length=100)

    class Meta:
        db_table = 'UserQuery'
    
    def __str__(self):
        return self.Name + " " + self.Email + " " + self.Query
