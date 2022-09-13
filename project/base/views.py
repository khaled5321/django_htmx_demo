from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Contact
from .forms import ContactForm

def home(request):
    if request.POST:
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name') 
            phone_number = form.cleaned_data.get('phone_number')  
            contact = Contact.objects.create(name=name, phone_number=phone_number)
            return redirect('display_list')

    form = ContactForm()
    contacts = Contact.objects.all()

    return render(request, "base/home.html", {"form":form, 'contacts': contacts})

class ContactList(ListView):
    template_name = 'base/contact_list.html'
    model = Contact
    context_object_name = 'contacts'

def delete(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    contacts = Contact.objects.all()
    return render(request, 'base/contact_list.html', {'contacts': contacts})