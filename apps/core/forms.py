# encoding: utf-8

from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class ContactForm(forms.Form):

	name			= forms.CharField(label=u"Nome")
	email			= forms.EmailField(label=u"E-mail")
	message			= forms.CharField(label=u"Mensagem",
									  widget=forms.Textarea)

	def send_mail(self):
		subject = u'E-mail de contato de %s' % self.cleaned_data['name']
		context = {
			'name': self.cleaned_data["name"],
			'email': self.cleaned_data["email"],
			'message': self.cleaned_data["message"],
		}
		message = render_to_string("core/contact_mail.txt", context)
		message_html = render_to_string("core/contact_mail.html", context)
		
		msg = EmailMultiAlternatives(subject, message_html,
						  'luizfabiodacruz@gmail.com',
						  ['luizfabiodacruz@gmail.com'])
		msg.content_subtype = "html"
		msg.send()