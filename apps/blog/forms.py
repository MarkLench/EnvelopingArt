from django import forms
from .models import post


class new_post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = ('Title', 'Body', )
    Title = forms.CharField(max_length=120)
    Body = forms.CharField(widget=forms.Textarea)