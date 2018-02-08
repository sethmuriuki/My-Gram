from django import forms
from .models import Images, Comments
#......
class NewStatusForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', 'caption')

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)

class ImagePost(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image','name', 'caption')