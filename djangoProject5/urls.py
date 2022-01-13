from django.conf.urls import url
from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from django.views.static import serve
from djangoProject5 import settings

urlpatterns = [
    path('website/', include('webData.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('article/', include('article.urls')),
    path('comment/', include('comment.urls')),
    path('tags/', include('tags.urls')),
    path('data/', include('webData.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    # path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), ]
