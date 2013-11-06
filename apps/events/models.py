#enconding: utf-8

from django.db import models

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


class Comment(models.Model):

	name 		= models.CharField(verbose_name=u"Nome", maxlength=200)
	email		= models.EmailField(verbose_name=u"E-mail", )
	event 		= models.ForeignKey(Event, verbose_name="Evento",
									related_name=u"comments")
	text 		= models.TextField(verbose_name=u"Texto")
	create_on	= models.DateTimeField(verbose_name=u"Criado em", auto_now_add=True)