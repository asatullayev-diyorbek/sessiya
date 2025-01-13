from django.db import models

class Note(models.Model):
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return f"Note {self.pk}"

    def file_url(self):
        return self.file.url if self.file else None

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['-pk']