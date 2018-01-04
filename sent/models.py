from django.db import models
from django.utils import timezone

class Posting(models.Model):
    title = models.CharField(
        max_length = 64,
        verbose_name = 'title',
    )
    
    message = models.CharField(
        max_length = 512,
        verbose_name = 'description',
    )

    group = models.CharField(
       max_length = 2,
       verbose_name = 'group',
   )

    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name= 'date',
    )


