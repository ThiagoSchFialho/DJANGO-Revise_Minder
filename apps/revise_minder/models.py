from django.db import models

class Subject(models.Model):

    COLOR_OPTIONS = [
        ("red", "🔴 Vermelho"),
        ("orange", "🟠 Laranja"),
        ("yellow", "🟡 Amarelo"),
        ("green", "🟢 Verde"),
        ("blue", "🔵 Azul"),
        ("purple", "🟣 Roxo"),
        ("white", "⚪ Branco"),
    ]

    description = models.CharField(max_length=130, null=False, blank=False)
    color = models.CharField(max_length=100, choices=COLOR_OPTIONS, default='')

    def __str__(self):
        return f"Subject [{self.description}]"