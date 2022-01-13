from django.urls import path
from tags.views import showPersonalTags, addTag, deleteTag

urlpatterns = [
    path('addTag/', addTag.as_view()),
    path('deleteTag/', deleteTag.as_view()),
    path('showPersonalTags/', showPersonalTags.as_view())
]
