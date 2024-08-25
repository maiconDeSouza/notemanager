from uuid import uuid4
from django.db import models
from django.utils import timezone


# Model definition


class Note(models.Model):
    id = models.UUIDField(verbose_name="id", primary_key=True,
                          default=uuid4, unique=True, blank=False, null=False)
    title = models.CharField(verbose_name="Título",
                             max_length=100, blank=False, null=False)
    description = models.TextField(
        verbose_name="Descrição", blank=False, null=False)
    created_at = models.DateTimeField(
        verbose_name="Criado em", default=timezone.now)
    important = models.BooleanField(verbose_name="Importante", default=False)

    class Meta:
        ordering = ["-important", "created_at"]

    def __str__(self):
        return self.title
