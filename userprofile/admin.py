from django import forms
from django.forms import ModelForm
from django.contrib import admin
from userprofile.models import User, Usertype, CV


class UserTypeAdmin(admin.ModelAdmin):
	fields = ['typename']

admin.site.register(Usertype, UserTypeAdmin)


# class UserAdminForm(ModelForm):
# 	headline = MyFormField(max_length=200, required=False,
#                            help_text="Use puns liberally")

# 	class Meta:
# 		model = User
# 		fields = ['headline', 'username']



class UserAdmin(admin.ModelAdmin):
	fields = ['userType', 'username', 'password', 'firstname', 'middlename', 'lastname']


admin.site.register(User, UserAdmin)