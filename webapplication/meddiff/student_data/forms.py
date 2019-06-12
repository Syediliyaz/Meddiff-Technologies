from django import forms

class EmailForm(forms.Form):
	Name = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	Roll = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	Age = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	Gender = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	
class DataForm(forms.Form):
	Name = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	Roll = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	Age = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)
	Gender = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,'rows':1}),required=False)