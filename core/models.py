from django.db import models

class Department(models.Model):
    name = models.TextField('Название отдела', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Position(models.Model):
    name = models.CharField('Название должности', max_length=255)
    depart = models.ForeignKey(Department, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'


class Worker(models.Model):
    name = models.CharField('Имя', max_length=255)
    surname = models.CharField('Второе имя', max_length=255, blank=True)
    phone = models.TextField('Номер телефона', null=True)
    email = models.EmailField('E-mail')
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    depart = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'


class TradeUnion(models.Model):
    name = models.CharField('Название профсоюза', max_length=255)
    members = models.ManyToManyField(Worker)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Trade union'
        verbose_name_plural = 'Trade unions'

