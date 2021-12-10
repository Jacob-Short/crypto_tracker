from django import forms


class SendMessageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea())