from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.views.generic import View

# class Invite(View):
#     def get(self,request):
#         return HttpResponse("<h2>Welcome to Class Based Views</h2>")


from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
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



class VoterCreateView(CreateView):
   model = Voter
   fields = "__all__"
   # redirect('')


   # By default template name is voter_form.html
   # By default contex name is form

class VoterUpdateView(UpdateView):
   model = Voter
   fields = "__all__"


from django.urls import reverse_lazy
class VoterDeleteView(DeleteView):
   model = Voter
   success_url = reverse_lazy('vote2')
   # By default template name is voter_confirm_delete.html
   # By default contex name is form
