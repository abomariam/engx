from django.db import models
import os
from uuid import uuid4

# Create your models here.

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper



# class MyImageField(models.ImageField):
#
#     def pre_save(self, model_instance, add):
#         try:
#             old = type(model_instance).objects.get(pk = model_instance.pk)
#             if getattr(old,self.attname) != getattr(model_instance,self.attname):
#                 os.remove(getattr(old,self.attname).path)
#         except:
#             pass
#         return super(MyImageField,self).pre_save(model_instance,add)
#
#     def delete(self):
#         try:
#             os.remove(self.path)
#         except:
#             pass
#         return super(MyImageField,self).delete()

class Slider (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=path_and_rename('slider_img'),help_text="The image should be 851*315 pixels")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
