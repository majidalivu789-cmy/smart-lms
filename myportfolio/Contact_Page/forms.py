from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'name','name':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email', 'name':
    'email'}))
    subject = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id':'subject', 'name':'subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'id':'message', 'name':'message'}))
    
    class Meta:
        model = ContactMessage
        fields = ['name','email','subject','message']




    
