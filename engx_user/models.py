from django.db import models
from django.db.models.signals import pre_save
from mezzanine_agenda.models import Event
import os
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User",related_name='profile')
    cv = models.FileField(null=True,upload_to='cvs')
    img = models.ImageField(null=True,upload_to='pics')
    age = models.IntegerField

    # date_of_birth = models.DateField(null=True)
    # first_name = models.CharField(max_length=35)
    # last_name = models.CharField(max_length=35)
    # user_name = models.CharField
    # mail = models.CharField
    # faculty = models.CharField


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            old = UserProfile.objects.get(pk = self.pk)
            if old.img != self.img:
                os.remove(old.img.path)
            if old.cv != self.cv:
                os.remove(old.cv.path)
        except:
            pass

        super(UserProfile,self).save(force_insert,force_update,using,update_fields)

class Instructor(models.Model):
    user = models.ForeignKey("auth.User", related_name='instructor')
    events = models.ManyToManyField(Event, related_name='instructor')

    def __str__(self):
        return self.user.get_full_name()
