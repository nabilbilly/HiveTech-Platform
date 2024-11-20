from django.contrib import admin
from .models import Team, TeamMembership

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Team model.
    """
    list_display = ('name', 'created_by', 'slug', 'members_count', 'created_at')
    search_fields = ('name', 'created_by__username')
    readonly_fields = ('slug', 'unique_id', 'created_at')
    list_filter = ('created_at',)

    def members_count(self, obj):
        """
        Display the number of members in the team.
        """
        return obj.members_count()
    members_count.short_description = 'Number of Members'

@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TeamMembership model.
    """
    list_display = ('user', 'team', 'role' , 'SpecifyRole', 'description','joined_at')
    search_fields = ('user__username', 'team__name', 'SpecifyRole')
    list_filter = ('role', 'joined_at')
    autocomplete_fields = ('user', 'team')
    readonly_fields = ('joined_at',)

    class Meta:
        verbose_name_plural = "Team Memberships"




