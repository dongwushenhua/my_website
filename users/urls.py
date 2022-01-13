from django.urls import path, include
from users import views
from users.views import getUserData, getUserFollowed, getUserFollowing, showUserMessage, addVisitorMessage, \
    deleteVisitorMessage, showVisitorMessage

urlpatterns = [
    path('register/', views.register),
    path('logIn/', views.logIn),
    path('logOut/', views.logOut),
    path('modifyUser/', views.modifyUser),
    path('modifyIcon/', views.modifyIcon),
    path('follow/', views.relation),
    path('deleteAllUserMessage/', views.deleteAllUserMessage),
    path('addDirectMessage/', views.addDirectMessage),
    path('getUserData/', getUserData.as_view()),
    path('getUserFollowed/', getUserFollowed.as_view()),
    path('getUserFollowing/', getUserFollowing.as_view()),
    path('showUserMessage/', showUserMessage.as_view()),
    path('showVisitorMessage/', showVisitorMessage.as_view()),
    path('addVisitorMessage/', addVisitorMessage.as_view()),
    path('deleteVisitorMessage/', deleteVisitorMessage.as_view()),

    # path('notifications/', include('notifications.urls', namespace='notifications'))

    #     path('visitorMessage/', showVisitorMessage.as_view()),

]
