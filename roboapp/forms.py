import json
from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field, Hidden
from django import forms
from django.conf import settings
from .models import (UserProfile)


class PointsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PointsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        # self.helper.layout = Layout(
        #     Field('colour_choice', template="classroom/field_layouts/new_design_char_field.html", placeholder="Robot Name"),
        # )

    class Meta:
        model = UserProfile
        exclude = ['user', 'xp', 'robotify_points', 'level', 'wins', 'losses', 'robot_name']
