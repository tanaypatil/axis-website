from django.contrib import admin
from .models import AmishRegistrations, FeedBackFromAndroid, NotifsAndroid


class RegAdmin(admin.ModelAdmin):
    list_display = ['name', 'idnum', 'contact', 'city', 'date_created']
    search_fields = ['name', 'college', 'mail', 'contact']
    list_filter = ['city', 'college']

    class Meta:
        model = AmishRegistrations


class MsgAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'date_created']
    search_fields = ['name']

    class Meta:
        model = FeedBackFromAndroid


class NotifsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = NotifsAndroid


admin.site.register(AmishRegistrations, RegAdmin)
admin.site.register(FeedBackFromAndroid, MsgAdmin)
admin.site.register(NotifsAndroid, NotifsAdmin)
