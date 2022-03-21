from django.db import models


class Employ(models.Model):
    title = models.CharField('Заголовок сотрудника для списка', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    staff_name = models.CharField('Должность', max_length=25)
    age = models.IntegerField('Возраст')
    staff_exp = models.IntegerField('Стаж')
    wages = models.IntegerField('ЗП')
    education = models.CharField('Образование', max_length=25)
    duties = models.TextField('Обязанности')


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return f'/staff/{self.id}'


    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'