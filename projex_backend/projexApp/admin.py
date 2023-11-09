from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from projexApp.models import *

class UserAdmin(UserAdmin):
    list_display = (
        "email",
        "name",
        "enrolment_no",
        "username",
        "year",
        "is_member",
        "is_superuser",
    )
    list_filter = ("is_superuser", "is_member")
    fieldsets = (
        (None, {"fields": ("enrolment_no", "email", "username", "year", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_member")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "enrolment_no",
                    "username",
                    "year",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_member",
                ),
            },
        ),
    )
    search_fields = ("email", "enrolment_no", "username")
    ordering = ("enrolment_no",)


admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Goal)
admin.site.register(Feedback)
admin.site.register(Task)
admin.site.unregister(Group)

