from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, RedirectView,
    CreateView, UpdateView
)
from django.urls import reverse
from .models import POLL, Option


def poll_list(request):
    polls = POLL.objects.all()
    return render(request, "default/list.html", {
        'poll_list': polls,
        'msg': 'hello!'
    })


class polllist(ListView):
    model = POLL


class pollview(DetailView):
    model = POLL

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['option_list'] = Option.objects.filter(poll_id=self.object.id)
        return ctx


class pollcreate(CreateView):
    model = POLL
    fields = "__all__"
    success_url = "/"


class polledit(UpdateView):
    model = POLL
    fields = "__all__"
    success_url = "/"


class pollvote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("poll_list")