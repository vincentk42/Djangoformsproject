from django import forms
from django.core import validators


def must_be_empty(value):  # validators ALWAYS get a value, the value that's in the field that they're validating
    if value:
        raise forms.ValidationError('is not empty')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput,
                               label="leave empty",
                               validators=[must_be_empty],
                               )

    def clean(self):   # this is a clean method for the ENTIRE form, making sure all requirements are met
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )

#    def clean_honeypot(self):  # this will be the method that's called.  first it will look and now that it exists, will run
#        honeypot = self.clean_honeypot['honeypot']
#        if len(honeypot):  # if anything is in the honeypot field, it will raise an error
#            raise forms.ValidationError(
#                "honeypot should be left empty.  Bad Bot!")
#        return honeypot



"""

copied and pasted directly from master file
from django import forms


class SuggestionForm(forms.Form):
    name = forms.Charfield()    # pycharm did not autocomplete Charfield or Emailfield
    email = forms.EmailField()
    suggestion = forms.Charfield(widget=forms.Textarea)
"""