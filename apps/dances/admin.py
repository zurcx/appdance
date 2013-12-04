# encoding: utf-8

from django.contrib import admin

from .models import Rhythm, DanceStep, Level

#class DanceStepInline()

class RhythmAdmin(admin.ModelAdmin):

	list_display = ['name', 'public', 'slug', 'dancestep_count']
	search = 'name'

class DanceStepAdmin(admin.ModelAdmin):

	list_display = ['name', 'rhythm', 'level']
	search = 'name'

class LevelAdmin(admin.ModelAdmin):

	list_display = ['name']
	search = 'name'


admin.site.register(Rhythm, RhythmAdmin)
admin.site.register(DanceStep, DanceStepAdmin)
admin.site.register(Level, LevelAdmin)

