from django.contrib import admin
from .models import Profile, WorkHistory, Education, Skill, SocialMedia


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fields = [field.name for field in obj._meta.get_fields()
                  if not field.auto_created]
        fields = [f for f in fields if f not in ('created_at', 'updated_at')]
        return [
            ('Main Information', {'fields': fields}),
            ('Timestamps', {'fields': ('created_at', 'updated_at')}),
        ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',  'phone_number',
                    'is_active', 'created_at')
    list_filter = ('gender', 'state', 'city', 'is_active')
    search_fields = ('user__email', 'slug_id', 'phone_number')
    readonly_fields = ('slug_id', 'created_at', 'updated_at')
    fieldsets = (
        ("Personal Info", {
            'fields': ('slug_id', 'user', 'first_name', 'last_name',  'phone_number', 'age', 'gender', 'profile_image')
        }),
        ("Address", {
            'fields': ('state', 'city', 'address')
        }),
        ("Professional Info", {
            'fields': ('skills', 'description_myself', 'cv_file')
        }),
        ("Other Info", {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'company_name',
                    'start_date', 'end_date')
    list_filter = ('company_name', 'start_date', 'end_date')
    search_fields = ('profile__slug_id', 'job_title', 'company_name')
    date_hierarchy = 'start_date'
    fields = ('user', 'job_title', 'company_name',
              'start_date', 'end_date', 'job_description')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'institution_name', 'degree',
                    'field_of_study', 'start_date', 'end_date')
    list_filter = ('institution_name', 'degree', 'start_date')
    search_fields = ('profile__slug_id', 'institution_name', 'degree')
    date_hierarchy = 'start_date'
    fields = ('user', 'institution_name', 'degree',
              'field_of_study', 'start_date', 'end_date')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
