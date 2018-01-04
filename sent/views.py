from .inferwiki import ClassifySentences
from django.shortcuts import (render, redirect,)
from django.db import models
from sent.models import Posting
from .forms import PostingForm

def index(request):
    form = PostingForm(request.POST or None)
    
    # classify sentences if infer_button is pressed
    if 'infer_button' in request.POST:
        if request.method == 'POST':
            sent = ClassifySentences()
            d2v = sent.load_model()

            postlist = []
            ps = Posting.objects.all()
            for k in ps:
                postlist.append(k.message + ',')

            # classify sentences
            list = sent.infer_sent(d2v,postlist)

            inc = 0
            for k in ps:
                k.group = list[inc]
                k.save()
                inc+=1
            return redirect('sent:index')

    # post new sentence if submit_button is pressed
    elif 'submit_button' in request.POST:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('sent:index')

    new_text = Posting.objects.all().order_by('-id')
    contexts = {
        'form':form,
        'new_text':new_text,
    }
    return render(request, 'index.html', contexts)

