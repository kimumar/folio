from django.contrib import admin
from . models import ContactMessage
# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email', 'subject','message','status', 'note','updated_at')
    readonly_fields = ('name', 'subject','email', 'message', )
    list_filter= ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email', 'subject','message','status', 'note','updated_at')
    list_per_page = 25


admin.site.register(ContactMessage, ContactMessageAdmin)