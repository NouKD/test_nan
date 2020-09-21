from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions.action import Actions

from django.contrib.auth.admin import User
# Register your models here.

class CommentaireInline(admin.StackedInline):
    model = models.Commentaire
    extra = 1


class ArticleAdmin(Actions):
    
    list_display =  ('titre','date_add', 'date_update', 'status','categorie','image_view')
    search_fields = ('titre','categorie',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre',]
    ordering = ['titre',]
    filter_horizontal = ('tag',)
    list_per_page = 10
    readonly_fields = ['detail_image']
    inlines = [
        CommentaireInline
        ]
    fieldsets = [
        ("infocategory",{'fields':['titre','image','description','categorie','contenue','tag', 'auteur']}),
        ("standare",{'fields':['status',]})
        ]    

    def image_view(self,obj):
        return mark_safe("<img src = '{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}/" width ="100px" height ="50px">'.format(url = obj.image.url))

class ArticleInline(admin.TabularInline):
    model = models.Article
    extra = 1

class CategorieArticleAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    readonly_fields = ['detail_image']
    inlines = [
        ArticleInline,
    ]
    fieldsets = [
        ("infocategory",{'fields':['nom','image','description']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))

    def detail_image(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))        

class CathegorieArticleInline(admin.TabularInline):
    model = models.Article
    extra = 1


class TagAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom',]}),
        ("standare",{'fields':['status',]})
        ]


class CommentaireAdmin(Actions):
    list_display =  ('nom', 'site', 'email', 'date_add', 'date_update', 'status')
    list_filter =  ('status',)
    search_fields = ('article', 'nom',)
    date_hierarchy = 'date_add'
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom', 'site','article','commentaire','email']}),
        ("standare",{'fields':['status',]})
        ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.CategorieArticle, CategorieArticleAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)