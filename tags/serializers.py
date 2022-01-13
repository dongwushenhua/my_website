from rest_framework import serializers
from users.serializers import userProfileSerializer
from tags.models import tag


class tagSerializer(serializers.ModelSerializer):
    tagCreater = userProfileSerializer()

    class Meta:
        model = tag
        fields = ['id', 'tagName', 'tagCreater']
