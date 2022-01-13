from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from tags.serializers import tagSerializer
from tags.models import tag
from users.models import userProfile


class addTag(APIView):
    def get(self, request):
        nowTag = tag()
        nowTag.tagName = request.GET.get('tagName')
        nowTag.tagCreater = userProfile.objects.filter(
            user=User.objects.filter(username=request.session.get('username')).first()).first()
        nowTag.save()
        tags = tag.objects.filter(tagCreater=nowTag.tagCreater)
        tagsSerializer = tagSerializer(tags, many=True)
        data = {'code': 200, 'msg': '添加成功', 'tagsSerializer': tagsSerializer.data}
        return JsonResponse(data, safe=False)


class deleteTag(APIView):
    def get(self, request):
        nowTag = tag.objects.filter(pk=request.GET.get('tagId')).first()
        nowTag.delete()
        tags = tag.objects.filter(tagCreater=userProfile.objects.filter(
            user=User.objects.filter(username=request.session.get('username')).first()).first()).all()
        tagsSerializer = tagSerializer(tags, many=True)
        data = {'code': 200, 'msg': '删除成功', 'tagsSerializer': tagsSerializer.data}
        return JsonResponse(data, safe=False)


class showPersonalTags(APIView):
    def get(self, request):
        tags = tag.objects.filter(tagCreater=userProfile.objects.filter(
            user=User.objects.filter(username=request.session.get('username')).first()).first())
        if tags:
            tagsSerializer = tagSerializer(tags, many=True)
            data = {'code': 200, 'msg': '查询标签成功', 'tagsSerializer': tagsSerializer.data}
            return JsonResponse(data, safe=False)
        else:
            data = {'code': 200, 'msg': '暂无标签'}
            return JsonResponse(data)
