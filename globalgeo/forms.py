from django.forms import ModelForm
from .models import Comment


class ContactForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body','name','email']

