from django.db import models
import datetime as dt
from django .contrib.auth.models import User
from tinymce.modes import HTMLField
from django.db.models.signals import post save
from django.dispatch import receiver


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    user = models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to'images/' , default='image/')



    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    @classmethod
    def update_name(cls,id,new_First_Name):
        cls.objects.filter(user_id = id).update(First_name=new_first_Name)
        new_title_object = cls.objects.get(First_Name=new_first_Name)
        new_name = new_title_object.first_Name 
        return new_name

    @classmethod
    def get_user_profile(cls,id):
        profile = cls.objects.get(user_id=id)
        return profile




@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if           