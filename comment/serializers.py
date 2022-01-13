from rest_framework import serializers
from comment.models import comment, commentLike
from users.serializers import userProfileSerializer


class commentSerializer(serializers.ModelSerializer):
    user = userProfileSerializer()

    class Meta:
        model = comment
        fields = ['id', 'commentContent', 'user', 'parent', 'commentTime',
                  'commentLikes']


class commentLikeSerializer(serializers.ModelSerializer):
    likeMan = userProfileSerializer()
    likeComment = commentSerializer()

    class Meta:
        model = commentLike
        fields = ['id', 'likeMan', 'likeTime', 'likeComment']
