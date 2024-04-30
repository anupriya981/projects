from django.db import models 
# from django.contrib.auth.models import User

# model for games.
class games(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    game=models.CharField(max_length=250)
    date=models.IntegerField()
    description=models.TextField()
    img=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def __str__(self) -> str:
    return self.title
