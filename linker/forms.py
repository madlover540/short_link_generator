from logging import PlaceHolder
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit




class My_Form (forms.Form):
    
    link = forms.CharField(label='insert your link here:')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))