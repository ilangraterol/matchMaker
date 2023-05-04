from django.contrib import admin

from .models import Profile, Interest


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'birth_date', 'get_interests')
    list_filter = ('location', 'interests')
    search_fields = ('user__username', 'bio', 'location', 'interests__name')

    def get_interests(self, obj):
        return ", ".join([interest.name for interest in obj.interests.all()])

    get_interests.short_description = 'Interests'


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Interest)
