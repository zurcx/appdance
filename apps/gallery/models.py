#encoding: utf-8

from django.db import models

class Album(models.Model):

	title			= models.CharField(max_length=100,
									   verbose_name=u'Título')
	created_on 		= models.DateTimeField(auto_now_add=True,
										   verbose_name=u'Criado em ')

	def __unicode__(self):
		return self.title

class Photo(models.Model):


	album 			= models.ForeignKey(Album, verbose_name=u"Album")
	title			= models.CharField(max_length=255,
										verbose_name=u'Título',
										blank=True)

	image 			= models.ImageField(upload_to='photos',
										verbose_name=u'Imagem')
	primary 		= models.BooleanField(default=False, 
										  verbose_name=u"Principal?")
	created_on		= models.DateTimeField(auto_now_add=True,
											verbose_name=u'Criado em')
	update_on		= models.DateTimeField(auto_now=True, 
											verbose_name=u'Atualizado em')

	def __unicode__(self):
		if self.title:
			return self.title
		return self.image.name.split('/')[-1]