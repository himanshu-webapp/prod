from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
ActiveInactive = [("Active","Active"),("Inactive","Inactive")]

class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    ssn = models.CharField(default="000",max_length=200)
    # Each Employee Unique Code
    certificateno = models.CharField(max_length=200)
    # Certificate Number
    name = models.CharField(max_length=200, null=True)
    authorizationcode = models.CharField(max_length=200, null=True)
    # Certificate's Authorization code
    role = models.CharField(max_length=200, null=True)
    status = models.CharField(choices=ActiveInactive,default="Active",max_length=50)
    # Certificate Title
    dateofissue = models.DateField(default=timezone.now)
    dateofexpiry = models.DateField(blank=True, null=True)
    # Expiry Date of Certificate (Optional)
    certificate = models.FileField(upload_to='uploads/career/certificates/%Y/%m/%d/')

    class Meta:
        ordering = ["dateofissue",]

class JobApplication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    # Last college/university attended
    course = models.CharField(max_length=100)
    # Highest Degree pursued
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=100)
    profile_applying_for = models.CharField(max_length=100)
    # Profile for which you are applying for job
    tenth_Percent = models.CharField(max_length=100)
    twelfth_Percent = models.CharField(max_length=100)
    Graduation_Percent = models.CharField(max_length=100)
    # Equivalent Percentage in the highest degree mentioned above

    experience = models.CharField(max_length=20, blank=True, null=True)
    # Experience in months/ years/fresher (Optional)
    current_CTC = models.CharField(max_length=20, blank=True, null=True)
    # Annual Package at your present company (for non-freshers)
    expected_CTC = models.CharField(max_length=20, blank=True, null=True)
    # Expected Package for applied position (optional)

    location_city = models.CharField(max_length=50, null=True)
    # City in which you are willing to work
    location_state = models.CharField(max_length=50, null=True)
    # State in which you are willing to work

    skills = models.TextField(null=True)

    present_workplace = models.CharField(max_length=200, blank=True, null=True)
    # Present Company (Optional)
    current_position = models.CharField(max_length=100, blank=True, null=True)
    # Present Position / Profile (Optional)
    other_description = models.TextField(null=True, blank=True)
    availablity_date = models.DateField(null=True)
    # Available from date
    linkedin_profile_link = models.URLField(max_length=500, null=True, blank=True)
    # LinkedIn Profile Link
    resume = models.FileField(upload_to='uploads/career/job-application')
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

class InternshipApplication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=100)
    profile_applying_for = models.CharField(max_length=200, blank=True, null=True)
    # Profile in which you are applying for intern
    tenth_Percent = models.CharField(max_length=100)
    twelfth_Percent = models.CharField(max_length=100)
    Graduation_Percent = models.CharField(max_length=100)
    # Percentage/CGPA till now in graduation

    date_applied = models.DateTimeField(default=timezone.now)
    # Date on which application is filled

    duration_in_weeks = models.CharField(max_length=10, null=True)
    # No of weeks you are seeking intern
    available_from = models.DateField(null=True)
    # Availability Date
    available_to = models.DateField(blank=True, null=True)
    # Available upto which date
    skills = models.TextField(blank=True, null=True)
    # Your skills
    other_description = models.TextField(null=True, blank=True)
    # Any other desciption (optional)
    linkedin_profile_link = models.URLField(max_length=500, null=True, blank=True)
    # LinkedIn Profile url
    resume = models.FileField(upload_to='uploads/career/intern-application')
    experience = models.CharField(max_length=100, null=True)

    # Any previous experience as intern (optional)

    def __str__(self):
        return str(self.id)

