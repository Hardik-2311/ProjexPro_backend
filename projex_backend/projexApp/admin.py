from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from projexApp.models import *

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'name', 'year', 'enrolment_no', 'is_Member', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'name', 'enrolment_no')
    list_filter = ('is_Member', 'is_staff', 'is_superuser')
    ordering = ('enrolment_no',) 

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'year', 'email', 'enrolment_no', 'profile_pic')}),
        ('Permissions', {'fields': ('is_Member', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Goal)
admin.site.register(Feedback)
admin.site.register(Task)
admin.site.unregister(Group)

