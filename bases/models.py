from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from PIL import Image

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creacion = UserForeignKey(auto_user_add=True, related_name='+')
    usuario_modificacion = UserForeignKey(auto_user=True, related_name='+')

    class Meta:
        abstract = True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'sample.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        image = Image.open(self.image.path)
        #To resize the profile image
        if image.height > 400 or image.width > 400:
            output_size = (400, 400)
            image.thumbnail(output_size)
            image.save(self.image.path)