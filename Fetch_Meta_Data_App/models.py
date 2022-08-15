from django.db import models
from xml.dom import ValidationErr
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class UserPost(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file_field = models.FileField()

    def __str__(self):
        return f'{self.user}=> {self.title}'


def validate_file(file_upload):
    file_size = file_upload.file.size
    limit_kb = 100000
    if file_size > limit_kb * 1024:
        raise ValidationErr("Max size of file is %s KB" % limit_kb)


class Files(models.Model):
    '''File model'''
    #file_name = models.CharField(max_length=300)
    #file_type = models.CharField(max_length=10)
    #file_size = models.IntegerField()
    # file_owner = models.ForeignKey(
    # settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_uploaded = models.FileField(
        blank=True, null=True, validators=[validate_file])

    class Meta:
        db_table = 'file'

    def __str__(self) -> str:
        return self.file_name


class Metadata(models.Model):
    meta_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meta_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.meta_data


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserFiles(models.Model):
    name = models.CharField(max_length=200)
    metadata = models.TextField(null=True)
    file_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
