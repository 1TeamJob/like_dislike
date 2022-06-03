from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def image_upload(instance, filename):
    imagename, extension = filename.split('.')
    return 'profiles/%s.%s'%(instance.user, extension)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    profile_image = models.ImageField(upload_to=image_upload, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)
    
    

@receiver(post_save, sender=User)
def _post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
