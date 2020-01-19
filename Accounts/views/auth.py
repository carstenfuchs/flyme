from django.conf import settings
from django.contrib.auth import forms, password_validation, views
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe


class LoginForm(forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Don't append colons to form labels ("Benutzername", nicht "Benutzername:").
        self.label_suffix = ""


class LoginView(views.LoginView):
    authentication_form = LoginForm
    default_next = None

    def get_success_url(self):
        """
        If no `next` parameter is given, the login view normally redirects to
        `settings.LOGIN_REDIRECT_URL`. This doesn't work well though if we have
        several apps that each provide a login view. Thus, allow URL configs to
        provide a custom default for `next`.
        """
        url = self.get_redirect_url()
        return url or resolve_url(self.default_next or settings.LOGIN_REDIRECT_URL)


class LogoutView(views.LogoutView):
    pass


class PasswordChangeForm(forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Don't append colons to form labels ("Benutzername", nicht "Benutzername:").
        self.label_suffix = ""

        # Set proper help texts (https://code.djangoproject.com/ticket/31158).
        self.fields['new_password1'].help_text = mark_safe("<br>".join(password_validation.password_validators_help_texts()))
        self.fields['new_password2'].help_text = "As you cannot see the password as you type, this helps catching typos."
      # self.fields['new_password2'].help_text = "Die doppelte Eingabe soll helfen, Tippfehler zu vermeiden."


class PasswordChangeView(views.PasswordChangeView):
    form_class = PasswordChangeForm


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    pass
