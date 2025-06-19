from django.shortcuts import render
from app6.forms import VoterForm
# Create your views here.

def Voter(request):
    vote = VoterForm()
    if request.method == 'POST':
        new = VoterForm(request.POST)
        if new.is_valid():
            print('Form successfully worked')
            print('Voterid : ', new.cleaned_data['Voter_id'])
            print('VoterName : ', new.cleaned_data['Voter_name'])
            print('VoterAddress : ', new.cleaned_data['Voter_address'])
            print('VoterAge : ', new.cleaned_data['Voter_age'])
    return render(request,'template/vote.html',{'voter' : vote})