from django.db import models
from django.contrib.auth.models import User 
from Accounts.models import Skill



class Workspace(models.Model):
    name = models.CharField(max_length=255, unique=True) # Workspace name, must be unique
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workspaces') # User who created the workspace
    description = models.TextField(blank=True) # Optional description
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets creation timestamp
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True) # To enable deactivation


    def __str__(self):
        return self.name
    
    
class WorkspaceMember(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workspace_memberships')
    role = models.CharField(max_length=50, choices=[('member', 'Member'), ('admin', 'Admin')], default='member') #Example roles
    description = models.TextField(blank=True, null=True) # Optional description of the role
    is_active = models.BooleanField(default=True) # For deactivation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role_description = models.TextField(blank=True) #Optional description of the role
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True) #Allows for deactivation of members

    class Meta:
        unique_together = ('workspace', 'user') #Prevent duplicate members in the same workspace

    def __str__(self):
        return f"{self.user.username} in {self.workspace.name} ({self.role})"


class WorkspaceImage(models.Model): #for profile pictures.
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='workspace_images/') #Adjust upload path as needed

    def __str__(self):
        return f"Image for {self.workspace.name}"


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)  # Optional state
    country = models.CharField(max_length=100, blank=True, null=True) #Optional country

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Job(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='jobs') # Links job to a workspace
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    # Consider using a more robust solution like GeoDjango for location data
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    #Consider adding a salary currency field.
    #salary_currency = models.CharField(max_length=3, default='USD')
    is_remote = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    min_salary = models.IntegerField(null=True, blank=True)  # Allow null for salary range flexibility
    max_salary = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')])
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField(null=True, blank=True)
    skills = models.ManyToManyField('Accounts.Skill', related_name='jobs')  # String reference
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # experience_level = models.CharField(max_length=50, choices=[('entry', 'Entry Level'), ('mid', 'Mid Level'), ('senior', 'Senior Level')])
    # application_deadline = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title
    

class JobSearchPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One set of preferences per user
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=100000) # Set a reasonable default

    def __str__(self):
        return f"Preferences for {self.user.username}"
    

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255) # Or a ForeignKey to a Company model if you have one
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full Time'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('volunteer', 'Volunteer'),
    ])
    experience_level = models.CharField(max_length=100) # e.g., "Entry-level", "Mid-level", "Senior"
    salary_min = models.FloatField() #Consider using a range field if you have a database that supports it.
    salary_max = models.FloatField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)  # Reflects the "active" icon in your HTML
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job') # Ensure a user can only apply once per job

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"
    

<<<<<<< HEAD
# class Skill(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     def __str__(self):
#         return self.name
=======
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
>>>>>>> 771c30136a2e2e1f4690d8a86dbff6d2c77ea7e8

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('job', 'skill')


class JobReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # User who reported (can be anonymous)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report on {self.job.title} by {self.user.username if self.user else 'Anonymous'}"


class Company(models.Model):
    """Represents a company posting jobs."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #Connect to Django User
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.company_name


class File(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='files')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    file = models.FileField(upload_to='workspace_files/')  # Adjust upload path as needed
    filename = models.CharField(max_length=255) #Store original filename
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filetype = models.CharField(max_length=50) #Example: 'video', 'image', 'document'

class Message(models.Model): #Simplified message model
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

