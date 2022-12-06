
from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post to here...",
                "class": "textarea is-success is-small",
            }
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = ("user", )

