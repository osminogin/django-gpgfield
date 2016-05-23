from django import forms

from pgpfield.forms import PGPFormField
from .models import PGPFieldTestModel


class PGPTestForm(forms.Form):
    pgp_data = PGPFormField()
    optional_pgp_data = PGPFormField(required=False)


class PGPTestModelForm(forms.ModelForm):

    class Meta:
        model = PGPFieldTestModel
        exclude = []