from django import forms
from django.forms import Textarea
from .models import Comment
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment': (''),
        }
        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'Enter your comment here', 'class': 'comment-form'}),
        }
            
    