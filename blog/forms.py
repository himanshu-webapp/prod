from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name','email','content']
        labels = {"name":"Name","email":"E-mail","content":"Comment"}
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Name"}),
            "email": forms.EmailInput(attrs={"placeholder":"example@xyz.com"}),
            "content": forms.Textarea(attrs={"placeholder":"Your Comment"}),
        }