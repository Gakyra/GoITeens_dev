from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Subject"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Message"}),
        required=True
    )
    from_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.EmailField()