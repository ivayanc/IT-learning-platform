from django.db import models

from users.models import SystemUser


class Olympiad(models.Model):
    PUBLIC = 1
    PRIVATE = 2
    TYPE_CHOICES      = [
        (PUBLIC, ('Відкрита')),
        (PRIVATE, ('За запрошенням')),
    ]
    start_time      = models.DateTimeField(verbose_name="Дата почтку")
    title           = models.CharField(verbose_name="Назва олімпіади", max_length=256)
    duration        = models.DurationField(verbose_name="Час проведення")
    description     = models.TextField(verbose_name="Опис олімпіади")
    olymp_type      = models.PositiveSmallIntegerField(verbose_name="Тип проведення",
                            choices = TYPE_CHOICES,
                            default = PUBLIC,
    )
    participants    = models.ManyToManyField(SystemUser,verbose_name="Зареєстровані для участі", blank=True)
    is_ended        = models.BooleanField(verbose_name="Завершена олімпіада", default=False)
    def __str__(self):
        return self.title

class Task(models.Model):
    EXCEL = 1
    ACCESS = 2
    WORD = 3
    POWERPOINT = 4
    OTHER = 5
    TYPE_CHOICES    = [
        (EXCEL, ('Excel')),
        (ACCESS, ('Access')),
        (WORD, ('Word')),
        (POWERPOINT, ('PowerPoint')),
        (OTHER, ('Інше')),
    ]

    olympiad        = models.ForeignKey(Olympiad,on_delete=models.CASCADE, verbose_name="Олімпіада")
    title           = models.CharField(verbose_name="Назва задачі", max_length=256)
    description     = models.TextField(verbose_name="Опис задачі")
    files           = models.FileField(verbose_name="Додаткові матеріали", blank=True)
    task_type       = models.PositiveSmallIntegerField(verbose_name="Розділ задачі",
                            choices = TYPE_CHOICES,
                            default = OTHER,
    )

    def __str__(self):
        return self.title


class Solution(models.Model):
    user            = models.ForeignKey(SystemUser, on_delete=models.CASCADE, verbose_name="Відправник", related_name='sender')
    task            = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    solution_file   = models.FileField(verbose_name="Файл розв'язок")
    reviewer        = models.ForeignKey(SystemUser, on_delete=models.CASCADE, blank=True, related_name='reviewer')

class Criteria(models.Model):
    task            = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    descrition      = models.CharField(verbose_name="Опис критерія", max_length=256)
    max_value       = models.IntegerField(verbose_name="Максимальний бал")
    step            = models.FloatField(verbose_name="Крок оцінки")
