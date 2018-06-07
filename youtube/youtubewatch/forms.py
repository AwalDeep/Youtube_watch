from django import forms


class VideoSearch(forms.Form):
    query = forms.CharField(
        help_text='query',
        max_length=400,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Funny',
                'name': 'query'
            })
    )