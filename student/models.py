from django.db import models
import uuid

class Student(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    stud_name = models.CharField(max_length=200, verbose_name="Full Name")
    stud_email = models.EmailField(verbose_name="E-Mail Address")
    stud_contact = models.CharField(max_length=20,verbose_name="Phone Number")
    stud_course = models.CharField(max_length=200, verbose_name="Course")
    stud_stud_id = models.IntegerField(verbose_name="Student ID")
    
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.stud_name

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        
        return url