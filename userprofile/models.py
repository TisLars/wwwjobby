from django.db import models

# Create your models here.
class Usertype(models.Model):
	typename = models.CharField("Type titel",max_length=200)

	def __unicode__(self):
		return self.typename

class User(models.Model):
	userType = models.ForeignKey(Usertype)
	userType.verbose_name = "Soort gebruiker"
	username = models.CharField("Gebruikers naam", max_length=200)
	password = models.CharField("Wachtwoord", max_length=200)
	firstname = models.CharField("Voornaam", max_length=200)
	middlename = models.CharField("Tussenvoegsel", max_length=200, blank=True)
	lastname = models.CharField("Achternaam", max_length=200)

	def __unicode__(self):
		return self.username
	
class CV(models.Model):
	user = models.ForeignKey(User)
	summary = models.TextField()

	def __unicode__(self):
		return self.user

class Vacancy(models.Model):
	user = models.ForeignKey(User)
	summary = models.TextField()

class Match(models.Model):
	user = models.ForeignKey(User)
	cv = models.ForeignKey(CV)
	vacancy = models.ForeignKey(Vacancy)

