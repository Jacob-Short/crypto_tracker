from django import forms

# models
from member.models import Member


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super(LoginForm, self).clean()

        # get fields from form
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        """
        can use raise ValidationError - although then we 
            cannot set the _errors title with desc

        from django.core.exceptions import ValidationError
        raise ValidationError(
          "Please use a valid domain."
        )
        """

        # TODO:
        # possiblity of giving a few suggestions based off 1st attempt
        # ex: input = dave, possibilities = ['dave0, 'dave1', 'davey']

        # possible validation for password

        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super(RegisterForm, self).clean()

        # get fields from form
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        """
        can use raise ValidationError - although then we 
            cannot set the _errors title with desc

        from django.core.exceptions import ValidationError
        raise ValidationError(
          "Please use a valid domain."
        )
        """

        # IntegreityError: [ UNIQUE contraint failed (username) ]
        existing_usernames = [member.username for member in Member.objects.all()]
        if username in existing_usernames:
            self._errors["existing-username"] = self.error_class(
                ["Username has been taken, please try a new one."]
            )

        # TODO:
        # possiblity of giving a few suggestions based off 1st attempt
        # ex: input = dave, possibilities = ['dave0, 'dave1', 'davey']

        # possible validation for password

        return self.cleaned_data
