from django.conf import settings
from django.apps import apps
from django.contrib import admin
from .models import (Article, Tag, Category, Timeline,
                     Carousel, Silian, Keyword, FriendLink,
                     AboutBlog)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'create_date'

    exclude = ('views',)

    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_date', 'update_date', 'is_top', 'is_publish')

    # 允许直接编辑的字段，对于布尔值的字段，这个非常有用
    list_editable = ('is_top', 'is_publish')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)

    # 激活过滤器，这个很有用
    list_filter = ('create_date', 'category', 'is_top', 'is_publish')

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    filter_horizontal = ('tags', 'keywords')  # 给多选增加一个左右添加的框

    search_fields = ('author__username', 'title')

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        User = apps.get_model(settings.AUTH_USER_MODEL)
        if db_field.name == 'author':
            if request.user.is_superuser:
                kwargs['queryset'] = User.objects.filter(is_staff=True, is_active=True)
            else:
                kwargs['queryset'] = User.objects.filter(id=request.user.id)
        return super(ArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


# 自定义管理站点的名称和URL标题
admin.site.site_header = '网站管理'
admin.site.site_title = '博客后台管理'


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('title', 'side', 'update_date', 'icon', 'icon_color',)
    fieldsets = (
        ('图标信息', {'fields': (('icon', 'icon_color'),)}),
        ('时间位置', {'fields': (('side', 'update_date', 'star_num'),)}),
        ('主要内容', {'fields': ('title', 'content')}),
    )
    date_hierarchy = 'update_date'
    list_filter = ('star_num', 'update_date')
    # 允许直接编辑的字段，对于布尔值的字段，这个非常有用
    list_editable = ('side', 'icon', 'icon_color')


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'content', 'img_url', 'url')


@admin.register(Silian)
class SilianAdmin(admin.ModelAdmin):
    list_display = ('id', 'remark', 'badurl', 'add_date')


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link', 'is_active', 'is_show', 'not_show_reason')
    date_hierarchy = 'create_date'
    list_filter = ('is_active', 'is_show')

    # 允许直接编辑的字段，对于布尔值的字段，这个非常有用
    list_editable = ('is_active', 'is_show')


@admin.register(AboutBlog)
class AboutBlogAdmin(admin.ModelAdmin):
    list_display = ('short_body', 'create_date', 'update_date')

    def short_body(self, obj):
        return '自由编辑 About 页面的内容，支持 markdown 语法。'

    short_body.short_description = 'AboutBlog'

    # 限制用户权限，只能超管可以编辑
    def get_queryset(self, request):
        qs = super(AboutBlogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return None
