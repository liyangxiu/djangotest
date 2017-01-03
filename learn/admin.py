#_*_ coding:utf-8 _*_
from django.contrib import admin
from .models import Person
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age','sex','editdate','status',)
    search_fields = ('name',)
    list_filter =  ('status',)
    actions = ['make_published']
    list_editable = ('age',)
    fieldsets = ((None,{"fields":('name',('age','sex','status'))}),
                 ('高级选项',{
                     'classes':('collapse',),
                     'fields':('context',),
                 }),
                 )
    def make_published(self, request, queryset):
        rows_updated= queryset.update(status='p')
        if rows_updated==1:
            message_bit=u'更新1行数据%s'%request.user.username
        else:
            message_bit=u'%s 行更新%s'%(rows_updated,request.user.username)
        self.message_user(request,u'%s 成功标记为已发布'%message_bit)

    def get_actions(self, request):
        actions=super(PersonAdmin,self).get_actions(request)
        del actions['delete_selected']
        return actions

    make_published.short_description = u"标记为已发布"

#admin.site.register(Person,PersonAdmin)
