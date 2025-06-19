from django import forms

class VoterForm(forms.Form):
    Voter_id = forms.IntegerField()
    Voter_name = forms.CharField()
    Voter_address = forms.CharField()
    Voter_age = forms.IntegerField()

