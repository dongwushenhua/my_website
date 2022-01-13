from django.urls import path
from comment import views
from comment.views import addComment

urlpatterns = [
    path('addComment/', addComment.as_view()),
    path('likeComment/', views.likeComment.as_view()),
    path('deleteComment/', views.deleteComment.as_view()),
]
