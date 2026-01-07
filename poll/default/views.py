from django.shortcuts import render
from .models import POLL,Option
from django.views.generic import  ListView,DetailView,RedirectView

# Create your views here.
def poll_list(req):
    polls = POLL.objects.all()
    return render(req,"default/list.html",{'poll_list': polls, 'msg':'hello!'})
class polllist(ListView):
    model = POLL
    #應用程式名稱/資料模型_list.html
    #default/poll_list.html
class pollview (DetailView):
    model=POLL
    def get_context_deta(self,**kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['option_list']=Option.objects.filter(poll_id=self.object.id)
        return ctx
class pollvote(RedirectView):
    pass