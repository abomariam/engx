from django.db import models
from django.db.models.signals import pre_save
import os
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User",related_name='profile')
    # date_of_birth = models.DateField(null=True)
    cv = models.FileField(null=True,upload_to='cvs')
    img = models.ImageField(null=True,upload_to='pics')

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


