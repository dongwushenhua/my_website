from django.urls import path, include
from article import views
from article.views import showAllArticle, showCollectArticle, searchArticle, showHotArticle, showVisitorArticle, \
    showPersonalArticle, showSpecificArticle


urlpatterns = [
    path('addArticle/', views.addArticle),
    path('deleteArticle/', views.deleteArticle),
    path('modifyArticle/', views.modifyArticle),
    path('likeArticle/', views.likeArticle),
    path('collectArticle/', views.collectArticle),
    path('searchArticle/', searchArticle.as_view()),
    path('showPersonalArticle/', showPersonalArticle.as_view()),
    path('showVisitorArticle/', showVisitorArticle.as_view()),
    path('showCollectArticle/', showCollectArticle.as_view()),
    path('showAllArticle/', showAllArticle.as_view()),
    path('showHotArticle/', showHotArticle.as_view()),
    path('showSpecificArticle/', showSpecificArticle.as_view()),
    path('notifications/', include('notifications.urls', namespace='notifications'))

    #########评论部分#########
    # path('addComment/', views.addComment),
    # path('deleteComment/',views.deleteComment),
]
