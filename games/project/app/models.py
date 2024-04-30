from django.db import models

# Create your models here.
class GameInfo(models.Model):
    game=models.CharField(max_length=250)
    date=models.IntegerField()
    description=models.TextField()


    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
