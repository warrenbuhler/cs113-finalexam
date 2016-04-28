from django import forms


class ChatForm(forms.Form):
    chat = forms.CharField(label = 'chat', max_length = 200, widget=forms.Textarea)
