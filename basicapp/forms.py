from django import forms
from django.core import validators


def check_for_z(value):  # user's validator method. value is a keyword and must
    # be passed in exactly
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must start with Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z], label="Name_thinh")
    email_email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')

    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    # required = False :  To specify that a field is not required
    # validator is a list used for validation

    # def clean_botcatcher(self): # check validation of 1 field
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOT YOU BOT!!")
    #     return botcatcher

    # clean is a keyword, you must type exactly "clean"
    def clean(self):  # check validation of all field. clean
        all_clean_data = super().clean()  # return all clean data from the entire form
        email = all_clean_data['email_email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Email is not matched!")
