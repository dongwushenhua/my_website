from rest_framework import serializers
from article.models import article, articleView, articleCollect
from tags.serializers import tagSerializer
from users.serializers import userProfileSerializer


class articleSerializer(serializers.ModelSerializer):
    articleTags = tagSerializer(many=True)
    postMan = userProfileSerializer()

    class Meta:
        model = article
        fields = ['id', 'content', 'title', 'createTime', 'postMan', 'views', 'likes', 'collects', 'comments',
                  'articleTags']


class articleViewSerializer(serializers.ModelSerializer):
    viewMan = userProfileSerializer()

    class Meta:
        model = articleView
        fields = ['id', 'viewMan', 'viewTime']


class articleCollectSerializer(serializers.ModelSerializer):
    collectArticle = articleSerializer()

    class Meta:
        model = articleCollect
        fields = ['id', 'collectArticle', 'collectTime']
