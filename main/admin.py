from django.contrib import admin
from .models import (
    AboutMe,
    Partners,
    Education,
    Experience,
    Awards,
    Skills,
    # Categories,
    Services,
    Projects,
    Achievements,
    Contacts
)


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'image', 'address', 'phone', 'email', 'get_complete_projects')
    search_fields = ('name', 'birthday', 'email')

    verbose_name_plural = 'About Me'

    def get_complete_projects(self, obj):
        return obj.complete_projects if obj.complete_projects else None

    get_complete_projects.short_description = 'Complete Projects'


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id','image', )


@admin.register(Education)
class EducationInline(admin.ModelAdmin):
    list_display = ('id','from_year', 'to_year', 'title', 'place', 'description')


@admin.register(Experience)
class ExperienceInline(admin.ModelAdmin):
    list_display = ('id','from_year', 'to_year', 'title', 'place', 'description')


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_top_3', 'current', 'last_week', 'last_month')


@admin.register(Awards)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id','from_year', 'to_year', 'title', 'place', 'description')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'title', 'description')
    search_fields = ('title', 'description')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image', 'category')


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'count')


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'subject', 'message')

