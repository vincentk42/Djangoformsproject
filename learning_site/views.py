from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from . import forms


def hello_world(request):
    return render(request, 'home.html')


def suggestion_view(request):
    form = forms.SuggestionForm()  # this line instantiates a copy of the form
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():   # checks to see if form is valid
            send_mail(
                'Suggestion from {}'. format(form.cleaned_data['name']),
                # data that comes back after the form has been validated

                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                # format can be fed a dictionary and then it will use the dictionary keys to fill in the forms

                ['kuneen@gmail.com']  # who the email actually goes to.


            )
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})
