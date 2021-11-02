from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

from .models import Contact


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent and we will be response shortly.')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'Contact request failed. Please ensure the form is valid!')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


@login_required
def view_contact(request):
    """ View contacts made by customers """
    contacts = Contact.objects.all()

    if not request.user.is_superuser:

        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    else:
        context = {'contacts': contacts, }

    return render(request, 'contact/view_contact.html', context)
