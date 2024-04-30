from django.db import models
from customise.models import customer
from games. models import games

# data model for downloaded.
class history(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,';live')),(DELETE,'delete')
    DOWNLOAD_STAGE=0
    DOWNLOAD=1
    ERROR=3
    HISTORY=2
    
    STATUS_CHOICE=((DOWNLOAD,'download')),((ERROR,'error')),((HISTORY,'history'))
    download_status=models.IntegerField(choices=STATUS_CHOICE,default =DOWNLOAD_STAGE)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='downloads')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    #model for downloded items
class Downloaded_Items(models.Model):
    games=models.ForeignKey(games,related_name='downloaded_history',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(history,on_delete=models.CASCADE,related_name='downloaded_items')

