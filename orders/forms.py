from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, widget=forms.TextInput(attrs={'size' : '50'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(attrs={'size' : '50'}))