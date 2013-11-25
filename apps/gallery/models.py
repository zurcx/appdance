#encoding: utf-8

from django.db import models
from apps.events.models import Event


class Album(models.Model):

	title			= models.CharField(max_length=100,
									   verbose_name=u'Título')
	event			= models.ForeignKey(Event, null=True, blank=True,
										verbose_name=u'evento',
										related_name='album_set')
	created_on 		= models.DateTimeField(auto_now_add=True,
										   verbose_name=u'Criado em ')
	@models.permalink
	def get_absolute_url(self):
		return('gallery_album', (), {'pk': self.pk})

	def primary_photo(self):
		photos = self.photo_set.all()
		photos_p = photos.filter(primary=True)
		if photos_p.exists():
			return photos_p[0]
		elif photos.exists():
			return photos[0]

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

	class Meta:

		verbose_name = u"Foto"
		verbose_name_plural = u"Fotos"

def photo_post_save(sender, created, instance, **kwargs):
	if instance.primary:
		others = Photo.objects.filter(album=instance.album)
		others = others.exclude(pk=instance.pk)
		others.update(primary=False)
models.signals.post_save.connect(photo_post_save,
								sender=Photo)
