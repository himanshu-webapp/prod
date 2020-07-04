from django import forms
from .models import JobApplication,InternshipApplication

class CertificateVerificationForm(forms.Form):
    certificateNo = forms.CharField(label="Certificate Number",max_length=16)
    dateofissue = forms.DateField(label="Date of Issue")

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = "__all__"

class InternshipApplicationForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        fields = "__all__"