from django.contrib.auth.models import User
from django.db import models

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
