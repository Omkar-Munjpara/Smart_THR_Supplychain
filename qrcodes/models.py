from django.db import models

# Create your models here.
from django.db import models

class QRCode(models.Model):
    data_list = models.CharField(max_length=255)
    qr_code_image = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return self.data_list
