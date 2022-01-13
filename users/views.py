# import hashlib
#
# from django.contrib.auth.hashers import make_password, check_password
import notifications
from django.db.models import Q
# from django.shortcuts import render
#
from notifications.models import Notification
from notifications.signals import notify
from rest_framework.views import APIView
#
# from users.models import newUser, userMessage, followRelation, visitorMessage, directMessages
# from django.utils import timezone
from django.http.response import JsonResponse
# from django.contrib import auth
# from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# # 认证模块
# from django.contrib import auth
#
# # 对应数据库
# from django.contrib.auth.models import User
#
# from users.serializers import newUserSerializer, userMessageSerializer, followRelationSerializer, \
#     visitorMessageSerializer
#
#

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from article.models import article
from users.models import messageContent, userProfile, follow
from users.serializers import userProfileSerializer, followSerializer, messageSerializer, notificationSerializer


def register(request):
    data = json.loads(request.body.decode('utf-8'))
    user = User.objects.filter(username=data['userName']).first()
    if user:
        data = {'code': 500, 'msg': '该用户名已被占用'}
    else:
        user = User.objects.create_user(username=data['userName'], email='', password=data['passWord'])
        nowUser = userProfile()
        nowUser.user = user
        nowUser.save()
        nowArticle = article()
        nowArticle.title = "欢迎新人"
        nowArticle.postMan = nowUser
        nowArticle.save()
        data = {'code': 200, 'msg': '注册成功'}
    return JsonResponse(data)


def logIn(request):
    data = json.loads(request.body.decode('utf-8'))
    user = User.objects.get(username=data['userName'])
    if user:
        checkUser = authenticate(request, username=data['userName'], password=data['passWord'])  # 验证成功之后就会返回这个user对象
        if checkUser:
            login(request, user)
            request.session['username'] = data['userName']
            data = {'code': 200, 'msg': '登陆成功'}
        else:
            data = {'code': 500, 'msg': '用户名与密码不匹配'}
    else:
        data = {'code': 500, 'msg': '用户未注册'}
    return JsonResponse(data)


def logOut(request):
    # request.session.flush()
    logout(request)
    data = {'code': 200, 'msg': '登出成功'}
    return JsonResponse(data)


def modifyUser(request):
    data = json.loads(request.body.decode('utf-8'))
    user = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
    user.sex = data["sex"]
    user.signature = data["signature"]
    user.contact = data["contact"]
    user.school = data["school"]
    user.save()
    data = {'code': 200, 'msg': '修改个人信息成功'}
    return JsonResponse(data)


def modifyIcon(request):
    icon = request.FILES.get('icon')
    user = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
    user.icon = icon
    user.save()
    data = {'code': 200, 'msg': '修改头像成功'}
    return JsonResponse(data)


def relation(request):
    following = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
    followed = userProfile.objects.get(user=User.objects.get(username=request.GET.get('userName')))
    relationship = follow.objects.filter(
        Q(following=following) & Q(followed=followed)).first()
    if (relationship):
        relationship.delete()
        following.decrease_followings()
        followed.decrease_followeds()
        # message = notifications.objects.filter(Q(verb='关注了你') & Q(recipient=followed) & Q(actor=following)).first()
        # message.delete()
        relationship = follow.objects.filter(following=following).all()
        followingSerializer = followSerializer(relationship, many=True)
        data = {'code': 200, 'msg': '取消关注', 'followFlag': '0', 'followingSerializer': followingSerializer.data}
    else:
        relationship = follow()
        relationship.following = following
        relationship.followed = followed
        relationship.save()
        following.increase_followings()
        followed.increase_followeds()
        notify.send(following, recipient=followed.user, verb='关注了你', )
        data = {'code': 200, 'msg': '关注成功', 'followFlag': '1'}
    return JsonResponse(data)


def deleteAllUserMessage(request):
    nowUser = User.objects.get(username=request.session.get('username'))
    userMessages = Notification.objects.filter(recipient=nowUser).all()
    userMessages.delete()
    data = {'code': 200, 'msg': '删除成功'}
    return JsonResponse(data)


class getUserData(APIView):
    def get(self, request):
        user = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
        data = {'code': 200, 'msg': '查询成功', 'userSerializer': userProfileSerializer(user).data}
        return JsonResponse(data)


class getUserFollowed(APIView):
    def get(self, request):
        followed = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
        relationship = follow.objects.filter(followed=followed).all()
        followedSerializer = followSerializer(relationship, many=True)
        data = {'code': 200, 'msg': '获取粉丝成功', 'followedSerializer': followedSerializer.data}
        return JsonResponse(data)


class getUserFollowing(APIView):
    def get(self, request):
        following = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
        relationship = follow.objects.filter(following=following).all()
        followingSerializer = followSerializer(relationship, many=True)
        data = {'code': 200, 'msg': '获取关注成功', 'followingSerializer': followingSerializer.data}
        return JsonResponse(data)


class showUserMessage(APIView):
    def get(self, request):
        reciever = User.objects.get(username=request.session.get('username'))
        # userMessages = reciever.notifications.unread()
        userMessages = Notification.objects.filter(recipient=reciever).all()
        userMessagesSerializer = notificationSerializer(userMessages, many=True)
        data = {'code': 200, 'msg': '用户消息查询成功', 'userMessagesSerializer': userMessagesSerializer.data}
        return JsonResponse(data)


class showVisitorMessage(APIView):
    def get(self, request):
        reciever = userProfile.objects.filter(
            user=User.objects.filter(username=request.GET.get("userName")).first()).first()
        visitorMessages = Notification.objects.filter(Q(verb='给你留言：') & Q(recipient=reciever.user)).all()
        visitorMessagesSerializer = notificationSerializer(visitorMessages, many=True)
        data = {'code': 200, 'msg': '查询留言成功', 'visitorMessagesSerializer': visitorMessagesSerializer.data}
        return JsonResponse(data)


class addVisitorMessage(APIView):
    def get(self, request):
        message = messageContent()
        message.message = request.GET.get("message")
        message.save()
        sender = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
        reciever = userProfile.objects.filter(user=User.objects.filter(username=request.GET.get("to")).first()).first()
        notify.send(sender, recipient=reciever.user, verb='给你留言：', action_object=message)
        visitorMessages = Notification.objects.filter(Q(verb='给你留言：') & Q(recipient=reciever.user)).all()
        visitorMessagesSerializer = notificationSerializer(visitorMessages, many=True)
        reciever.increase_messages()
        data = {'code': 200, 'msg': '留言成功', 'visitorMessagesSerializer': visitorMessagesSerializer.data}
        return JsonResponse(data)


class deleteVisitorMessage(APIView):
    def get(self, request):
        reciever = userProfile.objects.get(user=User.objects.filter(username=request.GET.get("to")).first())
        visitorMessage = Notification.objects.filter(pk=request.GET.get("id")).first()
        visitorMessage.delete()
        visitorMessages = Notification.objects.filter(Q(verb='给你留言：') & Q(recipient=reciever.user)).all()
        visitorMessagesSerializer = notificationSerializer(visitorMessages, many=True)
        data = {'code': 200, 'msg': '删除成功', 'visitorMessagesSerializer': visitorMessagesSerializer.data}
        reciever.decrease_messages()
        return JsonResponse(data)


def addDirectMessage(request):
    data = json.loads(request.body.decode('utf-8'))
    sender = userProfile.objects.get(user=User.objects.get(username=request.session.get('username')))
    reciever = userProfile.objects.get(user=User.objects.filter(username=data["to"]).first())
    message = messageContent()
    message.message = data["message"]
    message.save()
    notify.send(sender, recipient=reciever.user, verb='给你私信：', action_object=message)
    data = {'code': 200, 'msg': '私信成功'}
    reciever.increase_directMessages()
    return JsonResponse(data)
