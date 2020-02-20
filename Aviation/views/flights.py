from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from Organizations.common import get_managed_user


class QuickAddFlightForm(forms.Form):
    informal_input = forms.CharField(widget=forms.Textarea(attrs={'autofocus': True}))

    def clean_informal_input(self):
        fi = self.cleaned_data['informal_input']
        # `informal_input` uses `required=True`, so checking here for empty input is not necessary.
        # if not fi:
        #     raise forms.ValidationError("The input cannot be entirely empty.")
        return fi

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


@login_required
def create_view(request, user_id=None):
    mu = get_managed_user(request.user, user_id)

    if request.method == 'POST':
        form = QuickAddFlightForm(request.POST)

        if form.is_valid():
            # flight = create_flight(mu, form.cleaned_data['informal_input'])
            # flight.save()
            messages.success(request, f"The flight has been added.")
          # return redirect('aviation:flight-list', user_id=mu.id)
            return redirect('organizations:user-overview', user_id=mu.id)
    else:
        form = QuickAddFlightForm()

    return render(
        request,
        'Organizations/generic_form_page.html',
        {
            'form': form,
            'title': 'Add flight',
            'submit_button_label': 'Save',
        }
    )
