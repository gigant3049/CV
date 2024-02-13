from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'image', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
            'name': 'name',
            'placeholder': 'Name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'email',
            'name': 'email',
            'placeholder': 'E-mail'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'image',
            'name': 'image',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control w-10',
            'id': 'message',
            'name': 'message',
            'placeholder': "Write Message",
            'cols': 30,
            'rows': 7,
        })