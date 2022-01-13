import notification as notification
import notifications
from notifications.models import Notification
from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import follow, userProfile, messageContent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff',
        #           'is_superuser', 'date_joined']
        fields = ['username']


class userProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = userProfile
        fields = ['id', 'user', 'icon','signature']


class followSerializer(serializers.ModelSerializer):
    followed = userProfileSerializer()
    following = userProfileSerializer()

    class Meta:
        model = follow
        fields = ['id', 'followTime', 'followed', 'following']


class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = messageContent
        fields = ['id', 'message']


class notificationSerializer(serializers.ModelSerializer):
    from article.serializers import articleSerializer
    actor = userProfileSerializer()
    action_object = messageSerializer()
    target = articleSerializer()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'action_object', 'target', 'timestamp']


# class commentNotificationSerializer(serializers.ModelSerializer):
#     from comment.serializers import commentSerializer
#     actor = userProfileSerializer()
#     action_object = messageSerializer()
#     target = commentSerializer()
#
#     class Meta:
#         model = Notification
#         fields = ['id', 'actor', 'verb', 'action_object', 'target', 'timestamp']
