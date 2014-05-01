from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'location',
            'expertise',
            'education',
            'education_level',
            'looking_for',
            'city',
            'province',
            'sex',
            'has_drivers_license',
            'has_car')