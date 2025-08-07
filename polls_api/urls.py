from django.urls import path
from .views import PollListCreate, PollDetail, VoteView

urlpatterns = [
    path('polls/', PollListCreate.as_view()),
    path('polls/<int:pk>/', PollDetail.as_view()),
    path('polls/<int:pk>/vote/', VoteView.as_view()),
]