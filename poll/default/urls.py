
from django.urls import path
from .views import (
     poll_list,
     polllist,
     pollview,
     pollvote,
     pollcreate,
     polledit
)
urlpatterns = [
    path("", poll_list),
    path("list/", polllist.as_view(), name="poll_list"),

    path("<int:pk>/", pollview.as_view(), name="poll_view"),
    path("<int:oid>/vote/", pollvote.as_view(), name="poll_vote"),
    path("add/", pollcreate.as_view(), name="poll_create"),
    path("<int:oid>/edit/", polledit.as_view(), name="poll_edit"),
]