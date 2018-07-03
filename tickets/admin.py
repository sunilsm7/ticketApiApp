from django.contrib import admin

from .models import Ticket, Category, Comment

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'ticket_id')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Ticket, TicketAdmin)

admin.site.register(Category)

admin.site.register(Comment)
