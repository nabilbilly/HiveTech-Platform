import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Team(models.Model):
    """
    Represents a team that can have up to 5 members.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teams_created")
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.unique_id:
            self.unique_id = uuid.uuid4()
        super().save(*args, **kwargs)

    def members_count(self):
        """
        Returns the count of members in the team.
        """
        return self.members.count()

    def can_add_member(self):
        """
        Checks if a new member can be added (limit is 5).
        """
        return self.members_count() < 5

    def __str__(self):
        return f"{self.name} - {self.unique_id}"

class TeamMembership(models.Model):
    """
    Represents membership of a user in a team.
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_memberships")
    description = models.TextField(blank=True)
    SpecifyRole = models.CharField(max_length=100, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('member', 'Member')])

    class Meta:
        unique_together = ('team', 'user')  # Prevent a user from joining the same team multiple times
        
    

    def save(self, *args, **kwargs):
        if not self.pk and not self.team.can_add_member():
            raise ValidationError("This team already has the maximum of 5 members.")
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} in {self.team.name}"


