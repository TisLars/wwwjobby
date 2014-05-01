from django import forms
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from userprofile.models import CV, Vacancy, Match, UserProfile

# User start #
#class UserProfileAdmin(admin.ModelAdmin):
class UserProfileAdmin(admin.ModelAdmin):
 search_fields = ['location', 'expertise', 'date_of_birth']
 list_filter = ('location', 'expertise', 'date_of_birth')
 list_display = ('location', 'expertise', 'date_of_birth')

admin.site.register(UserProfile)
# User end #

# CVAdmin start #
class CVAdmin(admin.ModelAdmin):
	search_fields = ['job','education_level']
	list_filter = ('province','education_level')
	list_display = ('user', 'job','city','province','education_level')

admin.site.register(CV, CVAdmin)
# CVAdmin end #

# VacancyAdmin start #
class VacancyAdmin(admin.ModelAdmin):
	search_fields = ['user', 'job', 'region', 'sector', 'level']
	list_filter = ('level', 'sector')
	list_display = ('user','job', 'region', 'level')
		
admin.site.register(Vacancy, VacancyAdmin)
# VacancyAdmin stop #

# MatchAdmin start #

admin.site.register(Match)
# MatchAdmin stop #