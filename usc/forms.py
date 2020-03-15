from django import forms
from usc.models import Assembly

class AssemblyForm(forms.ModelForm):
    class Meta:
        model = Assembly
        fields = ['assembly','mvl_No','qty','fab_date','comments']

   