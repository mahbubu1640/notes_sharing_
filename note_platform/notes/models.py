

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    MEDIA_CHOICES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    media_type = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    media_file = models.FileField(upload_to='media_files/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class NoteShare(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.note} shared with {self.shared_with}"
