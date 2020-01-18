from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.password_validation import password_validators_help_texts
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe


class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Keinen Doppelpunkt in Labels verwenden ("Benutzername", nicht "Benutzername:").
        self.label_suffix = ""


class LoginView(auth_views.LoginView):
    authentication_form = LoginForm

    def get_success_url(self):
        """
        Wenn kein `next` Parameter vorhanden ist, leite nicht nach
        `settings.LOGIN_REDIRECT_URL` weiter (der gemeinsame Wert für alle Login Views),
        sondern nach `ma-service:übersicht`.
        """
        url = self.get_redirect_url()
        return url or reverse('organizations:user-overview')


class PCForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Keinen Doppelpunkt in Labels verwenden ("Benutzername", nicht "Benutzername:").
        self.label_suffix = ""

        # Setze vernünftige Hilfetexte ein (https://code.djangoproject.com/ticket/31158).
        self.fields['new_password1'].help_text = mark_safe("<br>".join(password_validators_help_texts()))
        self.fields['new_password2'].help_text = "Die doppelte Eingabe soll helfen, Tippfehler zu vermeiden."


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PCForm
    success_url = reverse_lazy('accounts:password-change-done')
