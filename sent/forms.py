from sent.models import Posting
from django.db import models
from django import forms

class PostingForm(forms.ModelForm):

   class Meta:
       model = Posting
       fields = ('message','title')
       widgets = {
           'message': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
       }
