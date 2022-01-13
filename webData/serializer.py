from rest_framework import serializers

from users.models import userProfile


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ['followeds',
                  'followings',
                  'articles',
                  'comments',
                  'likes',
                  'collects',
                  'directMessages',
                  'messages',
                  'views',
                  'networkTime',
                  'active']
