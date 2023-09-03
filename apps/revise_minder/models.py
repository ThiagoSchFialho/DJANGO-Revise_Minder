from django.db import models

class Subject(models.Model):

    COLOR_OPTIONS = [
        ("#CC2936", "🔴 Vermelho"),
        ("#F4743B", "🟠 Laranja"),
        ("#e9c46a", "🟡 Amarelo"),
        ("#2a9d8f", "🟢 Verde"),
        ("#3483FA", "🔵 Azul"),
        ("#9448BC", "🟣 Roxo"),
        ("#141414", "⚫ Preto"),
        ("#FFF9F5", "⚪ Branco"),
    ]

    description = models.CharField(max_length=130, null=False, blank=False)
    color = models.CharField(max_length=100, choices=COLOR_OPTIONS, default='')

    def __str__(self):
        return f"Subject [{self.description}]"