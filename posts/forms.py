from django import forms


class PostCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=255, min_length=6)
    description = forms.CharField(widget=forms.Textarea())
    rating = forms.FloatField(required=False)

