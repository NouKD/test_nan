from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions.action import Actions

from django.contrib.auth.admin import User
# Register your models here.

class ContactAdmin(Actions):
    list_display = ('nom', 'email', 'sujet', 'date_add', 'date_update','status')
    list_filter = ('status', )
    search_fields = ('nom', 'sujet',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['nom', 'email', 'sujet', 'message']}),
                 ('Standare', {'fields': ['status']})
                 ]

    
class NewsLetterAdmin(Actions):
    list_display = ('email', 'date_add', 'date_update','status')
    list_filter = ('status', )
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['email']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['email', ]}),
                 ('Standare', {'fields': ['status']})
                 ]

    
class SiteInfoAdmin(Actions):
    list_display = ('email', 'date_add', 'date_update','status')
    list_filter = ('status', )
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['email']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['email', 'map_url']}),
                 ('Standare', {'fields': ['status']})
                 ]

    
class PresentationAdmin(Actions):
    list_display = ('nom', 'date_add', 'date_update','status', 'image_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['nom', 'image', 'description']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def image_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class UserAccountAdmin(Actions):
    list_display = ('user', 'date_add', 'date_update','status', 'avatar_view')
    list_filter = ('status', )
    search_fields = ('user', )
    date_hierarchy = 'date_add'
    list_display_links = ['user']
    ordering = ['user']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['user', 'avatar',]}),
                 ('Standare', {'fields': ['status']})
                 ]

    def avatar_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.avatar.url))

class OtherInfoAdmin(Actions):
    list_display = ('contact', 'email', 'site', 'date_add', 'date_update','status',)
    list_filter = ('status', )
    date_hierarchy = 'date_add'
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['addresse', 'contact', 'email', 'site',]}),
                 ('Standare', {'fields': ['status']})
                 ]

    
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.NewsLetter, NewsLetterAdmin)
_register(models.SiteInfo, SiteInfoAdmin)
_register(models.Presentation, PresentationAdmin)
_register(models.UserAccount, UserAccountAdmin)
_register(models.OtherInfo, OtherInfoAdmin)