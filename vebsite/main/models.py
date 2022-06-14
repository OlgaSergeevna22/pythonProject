from django.db import models

class Task(models.Model):
    title=models.CharField('Название', max_length=50)
    task=models.TextField('Описание')
    technology = models.CharField('Технологии', max_length=50)
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title
