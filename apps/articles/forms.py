from django import forms
from .models import article


class new_article_form(forms.ModelForm):
    class Meta:
        model = article
        fields = ('Title', 'Body', 'Thesis', 'Image', )
    Title = forms.CharField(max_length=120)
    Thesis = forms.CharField(max_length=255, required = False)
    Body = forms.CharField(widget=forms.Textarea)
    Image = forms.ImageField(required = False)