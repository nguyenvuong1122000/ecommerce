from django import forms
from .models import Topic

class NewUserForm(forms.ModelForm):
    user_name = forms.CharField(max_length = 200)
    user_email = forms.CharField(max_length= 200)
    user_password = forms.CharField
    class Meta:
        model = Topic
        fields = ['subject', 'message']
class SearchForm(forms.ModelForm):
    content = forms.CharField(max_length=300)