# encoding: utf-8

from django.contrib import admin
from models import Event, Comment


def mark_public(modeladmin, request, queryset):
	queryset.update(public=True)
	modeladmin.message_user(request,
									u'Eventos atualizados com sucesso!')
mark_public.short_description = u"Marcar como público"

def mark_private(modeladmin, request, queryset):
	queryset.update(public=False)
	modeladmin.message_user(request,
									u'Eventos atualizados com sucesso!')
mark_private.short_description = u"Marcar como privado"

class EventAdmin(admin.ModelAdmin):

	list_display 	= ['name', 'type', 'public', 'comments_count']
	search_fields 	= ['name']
	actions 		= [ mark_private ]


admin.site.register(Event, EventAdmin)

admin.site.register([Comment])