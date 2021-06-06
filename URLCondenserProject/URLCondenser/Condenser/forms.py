from django import forms

class URLDataForm(forms.Form):
    	# taking the imput field
	EnterURL=forms.CharField(label='Enter Your URL ', max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Shorten URL Here'}))
