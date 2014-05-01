from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user =     				models.OneToOneField(User)
	location =   			models.CharField(('locatie'), max_length=30, blank=False)
	expertise =     		models.CharField(('ervaring'), max_length=30)
	education =     		models.CharField(('opleiding'), max_length=30)
	education_level =   	models.CharField(('niveau'), max_length=30)
	looking_for =   		models.CharField(('opzoek naar'), max_length=30)
	city =    				models.CharField(('stad'), max_length=30)
	province =    			models.CharField(('provincie'), max_length=30)
	sex =     				models.CharField(('geslacht'), max_length=10)
	has_drivers_license =  	models.BooleanField(('rijbewijs'))
	has_car =     			models.BooleanField(('auto'))

	def __unicode__(self):
		return unicode(self.user)
	
def create_profile(sender, instance, created, **kwargs):
	if created:
 		profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
	
class CV(models.Model):	
	user = 				models.ForeignKey(User)
	url = 				models.CharField("URL", max_length=255, unique=True)
	post_date = 		models.DateField()
	job =				models.CharField("Beroep", max_length=200)
	discipline = 		models.TextField()
	experience = 		models.TextField("Ervaring")
	education = 		models.TextField("Opleiding")
	education_level = 	models.CharField("Niveau", max_length=50)
	looking_for = 		models.TextField("Opzoek naar")
	city = 				models.CharField("Stad", max_length=50)
	province =			models.CharField("Provintie", max_length=50)
	sex =				models.CharField("Geslacht", max_length=10)
	date_of_birth =		models.DateField("Geboortedatum")
	drivers_license = 	models.CharField("Rijbewijs", max_length=50)
	car = 				models.CharField("Auto", max_length=10)
	
	def __unicode__(self):
		return unicode(self.user)

    
class Vacancy(models.Model):
	user = 			models.ForeignKey(User)
	url =			models.CharField("URL", max_length=255, unique=True)
	job =			models.CharField("Beroep", max_length=200)
	description = 	models.TextField("Beschrijving")
	region =		models.CharField("Regio", max_length=200)
	sector = 		models.CharField("Sector", max_length=200)
	level = 		models.CharField("Niveau", max_length=200)
	employment =	models.CharField("Dienstverband", max_length=200)
	offer = 		models.CharField("Aanbod", max_length=200)
	properties = 	models.TextField("Eigenschappen")
	demands = 		models.TextField("Eisen")
	knowledge =		models.TextField("Kennis")
	timestamp = 	models.DateTimeField("timestamp")

	def __unicode__(self):
		return unicode(self.user)

class Match(models.Model):
	cv = models.ForeignKey(CV)
	vacancy = models.ForeignKey(Vacancy)
	score = models.CharField("Score", max_length=10)
	is_notified = models.CharField("Notified", max_length=2)

	def __unicode__(self):
		return unicode(self.cv)
