import numpy as np
from django.db import models
from django.db.models import Model
from scipy.spatial import distance

from app.utils import get_descriptor


class Person(Model):
    class Meta:
        verbose_name = 'Работник кафедры'
        verbose_name_plural = 'Работники кафедры'

    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    rank = models.CharField(max_length=255, verbose_name='Учёное звание')
    photo = models.ImageField(upload_to='images', default=None, verbose_name='Фото')
    descriptor = models.TextField(null=True, blank=True, default=None, verbose_name='Дескриптор')

    def save(self, *args, **kwargs):
        image = self.photo
        desc = get_descriptor(image.file)
        if desc:
            self.descriptor = str(desc)
        an = np.fromstring(str(desc), sep='\n')
        a = distance.euclidean(an, an)
        super().save(*args, **kwargs)


class History(Model):
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Посетитель')
    time = models.DateTimeField(verbose_name='Время прихода')
