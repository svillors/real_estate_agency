from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', null=True, blank=True,
                                      default=None, db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField('Новостройка-ли', null=True,
                                       blank=True, default=None)
    liked_by = models.ManyToManyField(User, verbose_name='Кто лайкнул',
                                      blank=True, related_name='liked_flats')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Кто жаловался',
                             related_name='complaints')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE,
                             verbose_name='Кваритра, на которую жаловались',
                             related_name='complaints')
    text = models.TextField('текст жалобы')

    def __str__(self):
        return f'{self.user}, {self.flat}'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phonenumber = models.CharField('Номер владельца', max_length=20,
                                   db_index=True)
    pure_phonenumber = PhoneNumberField(
        'Нормализованный номер владельца', blank=True, db_index=True)
    flats = models.ManyToManyField(
        Flat, verbose_name='Кваритры в собственности',
        related_name='owners', db_index=True)

    def __str__(self):
        return self.name
