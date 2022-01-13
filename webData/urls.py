from django.urls import path
from webData import views
from webData.views import userData

urlpatterns = [
    path('websiteData/', views.websiteData),
    path('userData/', userData.as_view()),
    path('douBanHotMovie/', views.douBanHotMovie),
    path('weibo/', views.weibo),
    path('zhihu/', views.zhihu)
]
