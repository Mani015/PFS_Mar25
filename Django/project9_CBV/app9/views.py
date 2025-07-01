from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# class Invite(View):
#     def get(self,request):
#         return HttpResponse("<h2>Welcome to Class Based Views</h2>")


from django.views.generic import ListView,DetailView
from app9.models import Voter
class VoterListView(ListView):
   model = Voter
   # By defaultly context_name is voter_list
   # By defaultly template _name is voter_list.html



# DetailViews
class VoterDetailView(DetailView):
   model = Voter
   # By defaultly context_name is voter
   # By defaultly template _name is voter_detail.html
