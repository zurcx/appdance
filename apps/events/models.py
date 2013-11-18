#encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Event(models.Model):

	TYPE_CHOICES = (
		(1,u"Workshop"),
		(2,u"Palestra"),
		(3,u"Dojo"),

	)

	name		= models.CharField(verbose_name=u"Nome", max_length=200)
	type		= models.IntegerField(verbose_name=u"Tipo de Evento", choices=TYPE_CHOICES)
	description	= models.TextField(verbose_name=u"description", blank=True)
	create_on	= models.DateTimeField(verbose_name=u'Criado em ', auto_now_add=True)
	link		= models.URLField(verbose_name=u"Link", blank=True)
	public		= models.BooleanField(verbose_name=u"Público?",
									  default=True)

	def comments_count(self):
		return self.comments.count()
	comments_count.short_description = u"Número de comentários"

	@models.permalink
	def get_absolute_url(self):
		return ('events_details', (), {'pk':self.pk})


	def __unicode__(self):
		return self.name

	
	class Meta:
		verbose_name 		= u"Evento"
		verbose_name_plural = u"Eventos"



class Comment(models.Model):

	name 		= models.CharField(verbose_name=u"Nome", max_length=200)
	email		= models.EmailField(verbose_name=u"E-mail", )
	event 		= models.ForeignKey(Event, verbose_name="Evento",
									related_name=u"comments")
	website 	= models.URLField(verbose_name=u"Perfil do Facebook", blank=True)
	text 		= models.TextField(verbose_name=u"Texto")
	create_on	= models.DateTimeField(verbose_name=u"Criado em", auto_now_add=True)

	def __unicode__(self):
		return self.name

	class META:
		verbose_name 		= u"Comentário"
		verbose_name_plural	= u"Comentários"