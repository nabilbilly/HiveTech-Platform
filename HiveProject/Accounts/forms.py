from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'w-full p-2 border-2 border-black rounded'})
        self.fields['last_name'].widget.attrs.update({'class': 'w-full p-2 border-2 border-black rounded'})
        self.fields['email'].widget.attrs.update({'class': 'w-full p-2 border-2 border-black rounded'})
        self.fields['password1'].widget.attrs.update({'class': 'w-full p-2 border-2 border-black rounded'})
        self.fields['password2'].widget.attrs.update({'class': 'w-full p-2 border-2 border-black rounded'})

        for fieldname in ['first_name', 'last_name', 'email', 'password1', 'password2']:
            self.fields[fieldname].label_tag = lambda cls: forms.BoundField.label_tag(self.fields[fieldname], attrs={'class': 'block font-bold text-black-300'})

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
