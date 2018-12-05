from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование организации')
    registered_address = models.CharField(max_length=200, verbose_name='Юридический адрес', blank=True)
    reality_address = models.CharField(max_length=200, verbose_name='Почтовый адрес', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
    
    def __str__(self):
        return '{s.name} ({s.registered_address})'.format(s=self)


class Person(models.Model):
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    email_address = models.CharField(max_length=120, verbose_name='e-mail', blank=True)
    staff = models.CharField(max_length=120, verbose_name='Должность', blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Компания', blank=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ('fio',)
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'
    
    def __str__(self):
        return '{s.fio} - {s.company.name}'.format(s=self)



class Phone(models.Model):
    number = models.CharField(max_length=11, verbose_name='Номер телефона', unique=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='Контактное лицо', blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Компания', blank=True)
    class Meta:
        ordering = ('number',)
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Телефонные номера'
    
    def __str__(self):
        return '{s.number}'.format(s=self)

