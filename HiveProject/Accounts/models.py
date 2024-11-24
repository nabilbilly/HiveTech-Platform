from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime


 #New changes User Account


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Category name (e.g., "Data Scientist")

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    """Model for different education levels."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)  # ISO 3166-1 alpha-2 code
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)  #From Form
    last_name = models.CharField(max_length=100, blank=True) #From Form
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True) # Email field from your form
    newsletter_signup = models.BooleanField(default=False) #From Checkbox
    bio = models.TextField(blank=True)  #Allows empty bio
    portfolio_url = models.URLField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True) #Allows empty location
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True) #Optional image upload
    education_levels = models.ManyToManyField(EducationLevel, blank=True)  #Allows for multiple selections or none
    preferred_countries = models.ManyToManyField(Country, blank=True, related_name='users')
    include_work_location = models.BooleanField(default=False)
    include_work_anywhere = models.BooleanField(default=False)
 
    employment_options = models.ManyToManyField(
        'EmploymentOption', 
        blank=True,  # Allow no options selected
        limit_choices_to={'active': True}, # Optional: Filter by active options 
        related_name='users'
    )

    english_proficiency = models.CharField(
        max_length=25,  # Adjust length as needed
        choices=[
            ('A1 Beginner', 'A1 Beginner'),
            ('A2 Elementary', 'A2 Elementary'),
            ('B1 Intermediate', 'B1 Intermediate'),
            ('B2 Upper Intermediate', 'B2 Upper Intermediate'),
            ('C1 Advanced', 'C1 Advanced'),
            ('C2 Proficient', 'C2 Proficient'),
            ('Native Speaker', 'Native Speaker'),
        ],
        blank=True,  # Allow leaving it blank if not needed
        null=True, # Allow null values in the database if not needed
    )

    EXPERIENCE_LEVEL_CHOICES = [
        ('Entry Level', 'Entry Level'),
        ('Junior', 'Junior'),
        ('Mid-Level', 'Mid-Level'),
        ('Senior', 'Senior'),
        ('Lead/Principal', 'Lead/Principal'),
        ('Manager/Director', 'Manager/Director'),
        ('Executive/C-suite', 'Executive/C-suite'),
    ]

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVEL_CHOICES,
        blank=True,  # Allow leaving it blank if needed
        null=True,   # Allow NULL in the database if needed
    )

    preferred_work_style = models.CharField(
        max_length=20,
        choices=[
            ('Fully Remote', 'Fully Remote'),
            ('Hybrid', 'Hybrid'),
            ('On-site', 'On-site'),
        ],
        blank=True,  # Allow users to skip this for now
        null=True,   # Allow NULL values in the database
    )
    team_setup = models.CharField(max_length=20, choices=[
        ("big", "Big teams"),
        ("small", "Small teams"),
        ("independent", "Independent"),
        ("none", "None Selected") #add a default option
    ], default="none")

    years_of_experience = models.IntegerField(null=True, blank=True) # Allows for null/blank input for this field, as it's not required.
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=0)
    salary_type = models.CharField(max_length=10, choices=[('yearly', 'Yearly'), ('hourly', 'Hourly'), ('salary', 'Salary')], default='yearly') # Add choices for salary type
    selected_categories = models.ManyToManyField(Category, blank=True) # Many-to-many relationship
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, null=True, blank=True)  #For email verification


    has_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile for {self.user.username}"

User.add_to_class('first_login', models.BooleanField(default=True))



class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)  # Assuming a 6-digit OTP
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        """Checks if the OTP is still valid (within 10 minutes)."""
        time_elapsed = timezone.now() - self.created_at
        return time_elapsed <= datetime.timedelta(minutes=10)


class OTPVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)  # Store the OTP as a string
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user.username}"


class Skill(models.Model):
    user_profile = models.ForeignKey(
        'Accounts.UserProfile',  # Ensure correct string reference
        on_delete=models.CASCADE,
        related_name='user_skills'  # Use a unique related_name
    )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class UserProfileSkill(models.Model):
    user_profile = models.ForeignKey('Accounts.UserProfile', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_profile', 'skill')

    #New changes User Account


    #New changes Introduction

class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)


class EmploymentOption(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)  # Allows for disabling options

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    step1_completed = models.BooleanField(default=False)
    step2_completed = models.BooleanField(default=False)
    step3_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Progress for {self.user.username}"


class Community(models.Model):
    name = models.CharField(max_length=255)  #e.g., "Front-end Developer"
    description = models.TextField(blank=True, null=True) #Optional longer description
    location = models.CharField(max_length=255, blank=True, null=True) #e.g., "California"
    image = models.ImageField(upload_to='community_images/', blank=True, null=True) #Path to community image
    category = models.CharField(max_length=50, choices=[("Training", "Training"), ("University", "University"), ("Teams", "Teams")]) #This field is based on buttons in HTML


    def __str__(self):
        return self.name
    

class WorkSchedulePreferences(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Links to the Django User model
    flexible_hours = models.BooleanField(default=False)
    nine_to_five = models.BooleanField(default=False)
    # Add other schedule preferences as needed (e.g., part-time, full-time, specific days, etc.)


    def __str__(self):
        return f"Schedule Preferences for {self.user.username}"

    #New changes Introduction

