from django import forms
from django.utils.translation import ugettext_lazy as _


class PersonEditForm(forms.Form):
    years_list = [i for i in range(1960, 2006)]
    list_sex = (("Male", "Male"), ("Female", "Female"))
    first_name = forms.CharField(help_text="First name:")
    last_name = forms.CharField(help_text="Last name:")
    sex = forms.CharField(help_text="Sex:", widget=forms.Select(choices=list_sex))
    date_of_birth = forms.DateField(help_text="Year of birth:", widget=forms.SelectDateWidget(years=years_list))
    current_city = forms.CharField(help_text="Current city:")
    ava_photo = forms.ImageField(label=_(""), widget=forms.FileInput, required=False)

    @staticmethod
    def clean_data(field, value):
        if any(map(str.isdigit, value)):
            raise forms.ValidationError(_('Invalid {0} - this field cannot contain numbers'.format(field)))

    def clean(self):
        super(PersonEditForm, self).clean()
        fst_name = self.cleaned_data['first_name']
        lst_name = self.cleaned_data['last_name']
        cur_city = self.cleaned_data['current_city']
        PersonEditForm.clean_data("first name", fst_name)
        PersonEditForm.clean_data("last name", lst_name)
        PersonEditForm.clean_data("current city", cur_city)
        return self.cleaned_data
