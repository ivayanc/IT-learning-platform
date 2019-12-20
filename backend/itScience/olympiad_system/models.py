from django.db import models
from django.conf import settings
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
    participants    = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name="Зареєстровані для участі", blank=True)
    reviewers       = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="reviewers", verbose_name="Члени жюрі", blank=True)
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

    description     = models.TextField(verbose_name="Умова задачі")
    task_alias      = models.CharField(verbose_name="Id задачі", max_length=15)
    olympiad        = models.ForeignKey(Olympiad,on_delete=models.CASCADE, verbose_name="Олімпіада")
    title           = models.CharField(verbose_name="Назва задачі", max_length=256)
    files           = models.FileField(verbose_name="Додаткові матеріали", blank=True)
    task_type       = models.PositiveSmallIntegerField(verbose_name="Розділ задачі",
                            choices = TYPE_CHOICES,
                            default = OTHER,
    )

    def __str__(self):
        return self.title


class Solution(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Відправник", related_name='sender')
    task            = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    solution_file   = models.FileField(verbose_name="Файл розв'язок", upload_to='solutions/',max_length='500')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    reviewer        = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True, blank=True, related_name='reviewer')

class Criteria(models.Model):
    task            = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    descrition      = models.CharField(verbose_name="Опис критерія", max_length=256)
    max_value       = models.IntegerField(verbose_name="Максимальний бал")
    step            = models.FloatField(verbose_name="Крок оцінки")
