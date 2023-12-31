from django.db import models
from datetime import date, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Subject(models.Model):
    COLOR_OPTIONS = [
        ("vermelho", "🔴 Vermelho"),
        ("laranja", "🟠 Laranja"),
        ("amarelo", "🟡 Amarelo"),
        ("verde", "🟢 Verde"),
        ("azul", "🔵 Azul"),
        ("roxo", "🟣 Roxo"),
        ("branco", "⚪ Branco"),
    ]

    description = models.CharField(max_length=130, null=False, blank=False)
    color = models.CharField(max_length=100, choices=COLOR_OPTIONS, default='')
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_subject"
    )

    def __str__(self):
        return f"{self.description}, {self.color}"
    

class Study(models.Model):
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="subject"
    )
    revisions_cycles = models.IntegerField(
        default=3,
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    date = models.DateField(default=date.today, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_study"
    )

    def __str__(self):
        return f"Study [Subject={self.subject.description}, User={self.user}]"

class Revision(models.Model):
    study = models.ForeignKey(
        to=Study,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="study_revision"
    )
    date = models.DateField(default=None, null=False, blank=False)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_revision"
    )

    def __str__(self):
        return f"Revision [study={self.study.id}, date={self.date}]"