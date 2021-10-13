from django.shortcuts import render
from . models import ContactMessage, ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team Will reach you soon.")
            return HttpResponseRedirect('#contact')

    form = ContactForm

    context = {
        'form':form,
    }
    return render(request, 'index.html', context)

