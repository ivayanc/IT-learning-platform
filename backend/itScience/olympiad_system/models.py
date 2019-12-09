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
    olymp_type      = models.PositiveSmallIntegerField(
                            choices = TYPE_CHOICES,
                            default = PUBLIC,
    )
    
class Task(models.Model):
    olympiad        = models.ForeignKey(Olympiad,on_delete=models.CASCADE, verbose_name="Олімпіада")
    description     = models.TextField(verbose_name="Опис задачі")
    files           = models.FileField(verbose_name="Додаткові матеріали", blank=True)

class Solution(models.Model):
    user            = models.ForeignKey(SystemUser, on_delete=models.CASCADE, verbose_name="Відправник", related_name='sender')
    task            = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    solution_file   = models.FileField(verbose_name="Файл розв'язок")
    reviewer        = models.ForeignKey(SystemUser, on_delete=models.CASCADE, blank=True, related_name='reviewer')

class Criteria(models.Model):
    descrition      = models.CharField(verbose_name="Опис критерія", max_length=256)
    max_value       = models.IntegerField(verbose_name="Максимальний бал")
    step            = models.FloatField(verbose_name="Крок оцінки")

class TaskCriterias(models.Model):
    task            = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    criteria        = models.ForeignKey(Criteria, on_delete=models.CASCADE, verbose_name="Критерій")


