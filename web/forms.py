from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        labels = {"name":"","email":"","subject":"","message":""}
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Name","style":""}),
            "email":forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"E-Mail","style":""}),
            "subject":forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"Subject","style":""}),
            "message":forms.Textarea(attrs={"class":"form-control mb-2","placeholder":"Message ...","style":"resize:none;height:150px"})
        }