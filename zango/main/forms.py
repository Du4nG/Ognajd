from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label='Tên', max_length=10)
    check = forms.BooleanField(required=False)